FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1

# Need to install libpq-dev for psycopg2 (postgres driver)
RUN apt-get update -y
RUN apt-get install -y libpq-dev

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - fifo_inventory.wsgi:application
