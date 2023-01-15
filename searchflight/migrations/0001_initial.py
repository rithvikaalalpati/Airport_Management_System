# Generated by Django 4.1.4 on 2022-12-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flightsearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flight_no', models.CharField(max_length=70)),
                ('Flight_name', models.CharField(max_length=70)),
                ('_from', models.CharField(max_length=70)),
                ('_to', models.CharField(max_length=70)),
                ('Arrival', models.CharField(max_length=70)),
                ('Departure', models.CharField(max_length=70)),
                ('Available_seat', models.IntegerField()),
                ('price', models.IntegerField()),
                ('Staff_id', models.CharField(max_length=70)),
            ],
        ),
    ]
