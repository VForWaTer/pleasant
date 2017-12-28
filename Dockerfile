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

# Copy pleasant sources.
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
