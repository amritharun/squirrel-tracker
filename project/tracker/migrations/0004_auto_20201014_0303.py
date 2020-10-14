# Generated by Django 3.1.2 on 2020-10-14 03:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20201014_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='S_ID',
            field=models.CharField(default='1234', help_text='Unique Sighting ID', max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]