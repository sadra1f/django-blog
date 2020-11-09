# Quickstart

Requirements:
- Python 3.7+

#

Clone or download the project files:

    $ git clone https://github.com/Sadra1f/Django-Blog.git
    $ cd Django-Blog

Create a virtual environment:

    $ python -m venv venv
    $ source env/bin/activate  # On Windows use `env\Scripts\activate`

Install required packages:

    $ pip install -r requirements.txt

Sync database:
    
    $ python manage.py makemigrations
    $ python manage.py migrate

#

You will need to create a superuser in order to use admin pannel and create posts:

    $ python manage.py createsuperuser

Now you can start and use the server:

    $ python manage.py runserver
