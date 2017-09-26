For authentication we over an app to connect to watts. As Watts authenticaion requies Python 3.6, we use Python 3.6 for the project.

In this project you find several '_default' files (pleasant/settings_default.py, ).

Please remove '_default' from the filename and adjust the file according to your own system.

For details check the respective '_default' file.

# Quick start

Create and activate virtual environment

    python3 -m venv venv
    source venv/bin/activate

Install django

    pip install django

Prepare database

    python manage.py migrate

Start django server

    python manage.py runserver

# Docker

Install [Docker](https://get.docker.com/) and [Compose](https://docs.docker.com/compose/install/).

    $ curl -fsSL get.docker.com -o get-docker.sh
    $ sh get-docker.sh
    $ sudo pip install docker-compose

Start all the things.

    $ docker-compose up
