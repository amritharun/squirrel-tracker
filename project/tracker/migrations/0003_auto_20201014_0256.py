# Generated by Django 3.1.2 on 2020-10-14 02:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20201014_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='S_ID',
            field=models.CharField(help_text='Unique Sighting ID', max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
