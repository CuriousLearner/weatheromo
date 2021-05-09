from django.shortcuts import render

from .services import get_weather_data_for_city


def view_weather_data_for_city(request):

    weather_data = get_weather_data_for_city(city_id=2654411)

    return render(
        request,
        "weatherviz/index.html",
        context={
            "weather_data": weather_data
        }
    )
