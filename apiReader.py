import urllib.request
import json
import envBotOne

def ReadPM25Api(region):
    """
    This function returns API values from data.gov.sg
    """
    url = "https://api.data.gov.sg/v1/environment/pm25"
    apikey = envBotOne.GetDataSGApiKey()
    headers = {'api-key' : apikey}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        html = json.loads(response.read().decode())
        pm_two_five = html['items'][0]['readings']['pm25_one_hourly'][region]

    return str(pm_two_five)

def ReadWeatherForecast():
    """
    This function returns the API vales from data.gov.sg for WeatherForecast
    """

    url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
    apikey = envBotOne.GetDataSGApiKey()
    headers = {'api-key' : apikey}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as response:
        html = json.loads(response.read().decode())
        weather_forecast = html['items'][0]['forecasts']
    
    # for i in range(0,len(weather_forecast)):
    #     print(weather_forecast[i]['area'], ":", weather_forecast[i]['forecast'])

    return weather_forecast

