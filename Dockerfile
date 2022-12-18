FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#communicate with a PostgreSQL database
RUN # apt-get -y install libpq-dev gcc && pip install psycopg2-binary

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN #python manage.py migrate
