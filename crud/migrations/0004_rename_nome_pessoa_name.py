# Generated by Django 4.2.2 on 2023-06-25 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_pessoa_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='nome',
            new_name='name',
        ),
    ]
