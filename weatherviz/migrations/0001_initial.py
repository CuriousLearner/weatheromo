# Generated by Django 3.2.2 on 2021-05-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenWeatherCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='City Name')),
                ('country', models.CharField(max_length=10, verbose_name='Country')),
                ('open_weather_id', models.IntegerField(verbose_name='Open Weather ID')),
            ],
            options={
                'verbose_name': 'Open Weather City',
                'verbose_name_plural': 'Open Weather Cities',
            },
        ),
    ]
