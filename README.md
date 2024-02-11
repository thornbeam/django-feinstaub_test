# Test repo for django-feinstaub

## Installation
```bash
# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py migrate

# start the development server
python manage.py runserver
```
## Use commands
1. get header from csv files
```
python manage.py get_csv_header --url {url} --date {date}
```
2. generate models.py, admin.py, create_object.py
```
python manage.py generate_models --path sensor_csv_header.json
```
3. move models.py and admin.py to app root, create_object.py to app commands modules

4. import data from all csv files
```
python manage.py import_data-all --url {url} --date {date}
```
or import data from csv files of a specific sensor type
```
python manage.py import_data-mono --url {url} --date {date} --type {sensor_type}
```
