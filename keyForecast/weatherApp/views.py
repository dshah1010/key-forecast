from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.

import urllib.request
import json

def index(request):

    if request.method == 'POST':

        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city.replace(' ', '+') + '&units=metric&appid=' + os.getenv('API_KEY')).read() # API Data
        dataList = json.loads(source) # Holds all data from requested information 

        data = {
            "country_code" : str(dataList['sys']['country']),
            "coordinates" : "[" + str(dataList['coord']['lon']) + ', ' + str(dataList['coord']['lat']) + "]",
            "temp" : str(dataList['main']['temp']) + ' °C, ' + str((dataList['main']['temp'] * 9/5) + 32) + " °F",
            "pressure" : str(dataList['main']['pressure']) + " pascals",
            "humidity" : str(dataList['main']['humidity']),
            "wind_speed" : str(dataList['wind']['speed']) + " m/s, " + str(dataList['wind']['speed'] * 2.237) + " miles/h",
            "main" : str(dataList['weather'][0]['main']),
        } # Getting desired data from the API 

    else:
        data = {}

    return render(request, "main/index.html", data)