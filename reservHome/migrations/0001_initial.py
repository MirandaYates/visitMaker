# Generated by Django 2.0.2 on 2018-04-19 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docent', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('people_number', models.PositiveIntegerField()),
                ('tour_time', models.IntegerField(choices=[(9, '9:00am-10:00am'), (10, '10:00am-11:00am'), (11, '11:00am-12:00pm'), (12, '12:00pm-1:00pm'), (1, '1:00pm-2:00pm'), (2, '2:00pm-3:00pm'), (3, '3:00pm-4:00pm')])),
                ('tour_date', models.DateField()),
                ('Special_Accomidations', models.TextField(blank=True)),
            ],
        ),
    ]
