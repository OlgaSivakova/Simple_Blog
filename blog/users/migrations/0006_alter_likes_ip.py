# Generated by Django 4.1.5 on 2023-09-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_likes_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='ip',
            field=models.CharField(max_length=100, verbose_name='IP-адрес'),
        ),
    ]
