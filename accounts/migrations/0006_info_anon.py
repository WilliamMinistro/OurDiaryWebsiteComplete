# Generated by Django 3.1.4 on 2020-12-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_info_emotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='anon',
            field=models.BooleanField(default=False),
        ),
    ]
