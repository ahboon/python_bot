import urllib.request
import json
import envBotOne

def ReadPM25Api(region):
    """
    This function returns API values from data.gov.sg
    """
    url = "https://api.data.gov.sg/v1/environment/pm25"
    apiKey = envBotOne.GetDataSGApiKey()
    headers = {'api-key' : apiKey}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        html = json.loads(response.read().decode())
        pm_two_five = html['items'][0]['readings']['pm25_one_hourly'][region]

    return str(pm_two_five)

