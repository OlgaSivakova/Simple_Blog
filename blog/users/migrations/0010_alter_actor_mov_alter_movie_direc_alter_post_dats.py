# Generated by Django 4.1.5 on 2023-10-09 12:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_director_dressingroom_alter_post_dats_movie_actor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='mov',
            field=models.ManyToManyField(related_name='connect', to='users.movie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='direc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moviess', to='users.director'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dats',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 9, 15, 9, 25, 479507)),
        ),
    ]