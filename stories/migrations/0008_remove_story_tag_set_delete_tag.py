# Generated by Django 4.0 on 2022-03-15 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_remove_comment_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='tag_set',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
