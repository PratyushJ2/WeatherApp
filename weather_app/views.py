import requests

from django.shortcuts import render

def index(request): 

    API_KEY = open("C:\\Users\\praty\\OneDrive\\Desktop\\Coding Projects\\weather_api_key", "r").read()
    city = request.POST.get("city")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    if request.method == "POST":
        response = requests.get(url)
        data = response.json()

        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }

        return render(request, 'index.html', weather_data)
    else:
        return render(request, "index.html")

    
