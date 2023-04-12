# Generated by Django 4.2 on 2023-04-12 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_night', models.FloatField()),
                ('availability', models.BooleanField(default=True)),
                ('checkin_time', models.TimeField()),
                ('checkout_time', models.TimeField()),
                ('rules', models.TextField()),
                ('hh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.hh')),
            ],
        ),
        migrations.AddField(
            model_name='hh',
            name='owners',
            field=models.ManyToManyField(related_name='hh_owned', to='myapi.owner'),
        ),
    ]
