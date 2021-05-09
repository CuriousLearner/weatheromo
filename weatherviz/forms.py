from django import forms

from weatherviz.models import OpenWeatherCity


class CityForm(forms.Form):
    city = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['city'] = forms.ChoiceField(
            choices=[
                (city.open_weather_id, city.name)
                for city in OpenWeatherCity.objects.filter(country="IN").order_by('name')[:1500]
            ]
        )
