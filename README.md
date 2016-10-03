
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://csc394project-ebarns.c9users.io/' and the admin page from 
'https://csc394project-ebarns.c9users.io/admin'.

## Setting up Cloud9 enviroment

Fork a copy of ebarns on github

start a new blank c9 workspace 

type the following on command line:

    nano requirements.txt
	    "django>=1.9,<1.10"

    sudo apt-get update
    
    sudo apt-get upgrade

    sudo apt-get install python3.4-venv

    python3 -m venv env

    env/bin/pip install --upgrade pip

    env/bin/pip install --upgrade -r requirements.txt
    
    env/bin/python manage.py create super user
    
    username: admin
    email : <either your email or admin@localhost>
    password <crate a password>

    to run:
    
    env/bin/python manage.py migrate
    
    env/bin/python manage.py runserver 0.0.0.0:8080


## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver 0.0.0.0:8080
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide