# Generated by Django 4.0.6 on 2022-07-28 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='dt_created',
        ),
    ]
