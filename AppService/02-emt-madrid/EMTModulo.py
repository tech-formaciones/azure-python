import requests

urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "timeArrivalBus": "transport/busemtmad/stops/<stopId>/arrives/"
}

def GetToken():
    endpoint = urls["base"] + urls["login"]
    headers = {
        "X-ClientId": "escribe el id de cliente",
        "passKey": "escribe la clave"
    }

    response = requests.get(endpoint, headers=headers)

    if (response.status_code == 200):
        return response.json()["data"][0]["accessToken"]
    else:
        return None

def GetArrivalBus(parada):
    endpoint = urls["base"] + urls["timeArrivalBus"].replace("<stopId>", parada)
    headers = {"accessToken": GetToken()}
    data = {
        "cultureInfo": "ES",
        "Text_StopRequired_YN": "Y",
        "Text_EstimationsRequired_YN": "Y",
        "Text_IncidencesRequired_YN": "N",
        "DateTime_Referenced_Incidencies_YYYYMMDD": "20240514"
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if (response.status_code == 200):
        return map(InfoBus, response.json()["data"][0]["Arrive"])
    else:
        return None
    
def InfoBus(item):
    data = {}
    data["linea"] = item["line"]
    data["distancia"] = item["DistanceBus"]

    if (item["estimateArrive"] < 60):
        data["tiempo"] = "está en la parada."
    else:
        time = item["estimateArrive"] / 60
        if (time >= 20):
            data["tiempo"] = "llegará en 20 min o más."
        else:
            data["tiempo"] = f"llegará aproximadamente en {time:1.0f} min."

    data["mensaje"] = f"el {data['linea']} {data['tiempo']} ({data['distancia']} m.)"

    return data
