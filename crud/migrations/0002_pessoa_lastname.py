# Generated by Django 4.2.2 on 2023-06-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='lastName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
