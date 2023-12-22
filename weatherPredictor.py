import requests
import os
from datetime import datetime

api = "openWeather"
key = os.environ['openWeatherApiKey']

userApi = os.environ['openWeatherApiKey']
location = input("Enter the city name: ")

apiLink = f"https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + userApi

# requests module which helps to make http requests
reqApiLink = requests.get(apiLink)
apiData = reqApiLink.json()


if apiData['cod'] == '404':
    print("Invalid City: {}, Please check your city name".format(location))
else:
    tempCity = ((apiData['main']['temp']) - 273.15)
    weatherDesc = apiData['weather'][0]['description']
    hmdt = apiData['main']['humidity']
    windSp = apiData['wind']['speed']
    dateTime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("--------------------------------------------------------------------")
    print("Weather Stats for {} || {}" .format(location.upper(), dateTime))
    print("--------------------------------------------------------------------")

    print("| Current temperature is      : {:.2f} deg C".format(tempCity))
    print("| Current weather description :", weatherDesc, )
    print("| Current wind speed          :", windSp,"kmph")
    print("| Current humidity            :", hmdt, "%")

