from django.shortcuts import render
import requests

# Create your views here.

def index_view(request):
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=imperial&lang=en'
    city_name = 'Los Angeles' # default
    api_key = 'a5d8a0047d42974aa80a382161a314e5' # personal API key
    r = requests.get(api_url.format(city_name,api_key)).json() # convert json output requests.get to python dict
    context = {
        'city':city_name,
        'temp':r['main']['temp'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    }
    return render(request, 'weather/weather.html',context)
