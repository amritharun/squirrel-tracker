# Generated by Django 3.1.2 on 2020-10-14 03:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20201014_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='S_ID',
            field=models.CharField(default='1234', help_text='Unique Sighting ID', max_length=100, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
