# Generated by Django 2.0.2 on 2018-04-30 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservHome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='creation_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]