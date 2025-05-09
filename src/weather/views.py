from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from dotenv import dotenv_values

# Create your views here.

CONFIG_ENV = dotenv_values('.env')
API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=imperial&lang=en'

def single_view(request):

    weather_data = list()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            city_name = city.name
            if not city.unique_city_name():
                city.delete()
            api_key = CONFIG_ENV['API_KEY']
            r = requests.get(
                API_URL.format(city_name, api_key)).json()  # convert json output requests.get to python dict
            # Valid form but need to check if get valid response from API
            if r['cod'] == '404':
                city.delete()
            else:
                city_weather = {
                    'name': city_name,
                    'temp': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                }
                weather_data.append(city_weather)

    form = CityForm()

    context = {
        'weather_data':weather_data,
        'form':form,
    }
    return render(request, 'weather/single_city.html',context)

def all_view(request):

    form = CityForm()
    cities = City.objects.all()
    weather_data = list()

    for city in cities:
        city_name = city.name
        api_key = CONFIG_ENV['API_KEY']
        r = requests.get(API_URL.format(city_name,api_key)).json() # convert json output requests.get to python dict
        city_weather = {
            'name':city_name,
            'temp':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {
        'weather_data':weather_data,
        'form':form,
    }
    return render(request, 'weather/all_cities.html',context)