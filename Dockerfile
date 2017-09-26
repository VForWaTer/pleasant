FROM ubuntu:16.04

# Install python3 and geolibs, see
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/install/geolibs/
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    binutils \
    libproj-dev \
    gdal-bin

# Installing python gdal bindings is not straight forward (compare
# https://gist.github.com/cspanring/5680334) so let's just install
# them from the system repositories.
RUN apt-get update && apt-get install -y \
    python3-gdal

# We'll use netcat to check if the (remote) database is already up.
RUN apt-get update && apt-get install -y \
    netcat

# Someone already patched django-wfs for python3 (and more).
# Install this version from github sources.
RUN apt-get update && apt-get install -y \
    git
RUN mkdir /wfs
WORKDIR /wfs
RUN git clone https://github.com/it-thematic/django-wfs.git
WORKDIR /wfs/django-wfs
RUN pip3 install .

ADD . /code
WORKDIR /code

RUN pip3 install -r requirements.txt

EXPOSE 8000
#CMD python3 manage.py runserver 0.0.0.0:8000
