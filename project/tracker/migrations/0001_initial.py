# Generated by Django 3.1.2 on 2020-10-14 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LONG', models.DecimalField(blank=True, decimal_places=20, help_text='Longitude', max_digits=50)),
                ('LAT', models.DecimalField(blank=True, decimal_places=20, help_text='Latitude', max_digits=50)),
                ('SHIFT', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift session', max_length=100)),
                ('DATE', models.DateField(help_text='Date of sighting')),
                ('AGE', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='adult or juvenile', max_length=100)),
                ('COLOR', models.CharField(blank=True, choices=[('Grey', 'Grey'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='squirrel color', max_length=100)),
                ('LOCATION', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='squirrel found location', max_length=100)),
                ('SPEC_LOCATION', models.CharField(blank=True, help_text='Any additional comments about location', max_length=200)),
                ('RUNNING', models.BooleanField(default=False, help_text='Running!')),
                ('CHASING', models.BooleanField(default=False, help_text='Chasing!')),
                ('CLIMBING', models.BooleanField(default=False, help_text='Climbing!')),
                ('EATING', models.BooleanField(default=False, help_text='Eating')),
                ('FORAGING', models.BooleanField(default=False, help_text='Foraging')),
                ('Other_activities', models.CharField(blank=True, help_text='any additional comments', max_length=500)),
                ('KUK', models.BooleanField(default=False, help_text='Kuking')),
                ('QUAAS', models.BooleanField(default=False, help_text='Quaaing')),
                ('MOAN', models.BooleanField(default=False, help_text='Moaning')),
                ('TAIL_FLAG', models.BooleanField(default=False, help_text='Flagging tail')),
                ('TAIL_TWITCH', models.BooleanField(default=False, help_text='Twitching tail')),
                ('APPROACH', models.BooleanField(default=False, help_text='Approached humans')),
                ('RUNS', models.BooleanField(default=False, help_text='Runs from humans')),
            ],
        ),
    ]
