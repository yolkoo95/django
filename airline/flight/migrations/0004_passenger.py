# Generated by Django 3.0.4 on 2020-03-31 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20200331_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flight.Flight')),
            ],
        ),
    ]
