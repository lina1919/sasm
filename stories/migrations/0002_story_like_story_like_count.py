# Generated by Django 4.0 on 2022-03-11 08:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='story',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
