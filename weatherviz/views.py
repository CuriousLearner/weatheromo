from django.shortcuts import render

from .services import get_weather_data_for_city
from .forms import CityForm


def view_weather_data_for_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_id = form.cleaned_data.get("city", 1273294)
            weather_data = get_weather_data_for_city(city_id=city_id)
    else:
        form = CityForm()
        weather_data = None

    return render(
        request,
        "weatherviz/index.html",
        context={
            "weather_data": weather_data,
            "form": form
        }
    )
