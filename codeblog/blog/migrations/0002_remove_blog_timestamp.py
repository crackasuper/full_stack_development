# Generated by Django 5.0.1 on 2024-03-11 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='timeStamp',
        ),
    ]
