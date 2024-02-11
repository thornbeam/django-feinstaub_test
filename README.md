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
get header from csv files
```
python manage.py get_csv_header --url {url} --date {date}
```
generate models.py, admin.py, create_object.py
```
python manage.py generate_models --path sensor_csv_header.json
```
