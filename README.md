# squirrel-tracker
IEOR 4501 Final Project

Authored by Amrith Arunachalam (UNI: aa4053) and Chaoran Gou (UNI: cg3215)
Project Group: Amrith & Chaoran Section 001

Description
-------------------
**Squirrel Tracker** is a web application built in Django Framework to track all known squirrels in Central Park in Manhattan, New York City, NY. Our source data is from [`2018 Central Park Squirrel Census`](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). Users can add, update, and view squirrel data on the web application. 

Features
-------------------
- Import and Export data using csv format: using management commands, we could import data from csv or output data from Django database into csv files. 

```sh
$ python manage.py import_squirrel_data /path/to/file.csv
```
```sh
$ python manage.py export_squirrel_data /path/to/file.csv
```
- View a map of all squirrels in Central Park. Located at `/map`
- See the list of all squirrel sites with their ID. Located at `/sightings`
- Add squirrel sites by clicking **Add** on sightings page. Located at `/sightings/add`
- Edit current squirrel sites. Located at `/sightings/<unique-squirrel-id>`
- See the statistics on current squirrel sites. Located at `/sightings/stats`


Websites
-------------------
- http://34.86.85.64/sightings/
- http://34.86.85.64/sightings/stats/
- http://34.86.85.64/sightings/add/
- http://34.86.85.64/map/
