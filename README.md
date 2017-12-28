# Platform for Environmental And Spatial Analysis Tools

Pleasant is a django web-application with apps for easy interaction with WPS and data containing geographic information. 

# Installation

There a few requirements for Pleasant and it's easy running it right on the spot. All you need is python 3 and pip. As an alternative for simple and reproducable testing, Docker files are provided.

## Quick start

Create and activate virtual environment

    $ python3 -m venv venv
    $ source venv/bin/activate

Install requirements

    $ pip install -r requirements.txt

Prepare database

    $ python manage.py migrate

Start django server

    $ python manage.py runserver

## Docker and Compose

Install Docker

    $ curl -fsSL get.docker.com -o get-docker.sh
    $ sh get-docker.sh

Install Docker-Compose

    $ sudo pip install docker-compose

Run Pleasant through docker

    $ docker-compose up
