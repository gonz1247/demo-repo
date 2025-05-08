from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from dotenv import dotenv_values

# Create your views here.

CONFIG_ENV = dotenv_values('.env')

def index_view(request):
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=imperial&lang=en'

    print(CONFIG_ENV)
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = list()

    for city in cities:
        city_name = city.name
        api_key = CONFIG_ENV['API_KEY']
        r = requests.get(api_url.format(city_name,api_key)).json() # convert json output requests.get to python dict
        city_weather = {
            'name':city_name,
            'temp':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    print(weather_data)
    context = {
        'weather_data':weather_data,
        'form':form,
    }
    return render(request, 'weather/weather.html',context)
