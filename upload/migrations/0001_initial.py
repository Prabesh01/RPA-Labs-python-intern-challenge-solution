# Generated by Django 4.0.6 on 2022-07-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('filesize', models.FloatField()),
                ('duration', models.FloatField()),
                ('filetype', models.CharField(max_length=6)),
                ('up_date', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
            ],
        ),
    ]