## Folder Structure:

testing_on_api/
This is the main application and within it there is a folder labeled 'api' which holds the code that needs to be evaluated. The 'testing_on_api' additional folder holds the code for configuring the overarching settings and urls.

api/
Within this folder I would like to direct your main attention to the 'tests' folder and 'views' file.

The views file takes the HTTP methods that a given view should respond to, and within the test folder the 'test_views' file, each HTTP method on the applicable view is tested.

Less important files within the api folder include 'serializers.py' for easy rendering into JSON format, 'models.py' for representing the database fields, and 'urls.py' for the API urls.

## Getting Started:

install -r requirements.txt
python manage.py migrate

## Running the Server:

python manage.py runserver

http://localhost:8000/api/v1/testing_on_api/

## Running Tests

python manage.py test
