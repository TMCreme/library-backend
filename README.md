# Library Management System

## Description

## Running Locally
* Make sure docker and docker-compose are installed on your system
* Clone the project and switch to preferred branch
* Start the project with `docker compose up --build`
* When the docker container starts running successfully, visit the Swagger API documentation on `http://localhost:8091/api/docs` via the browser
* To run any migrations, run `docker-compose exec -it app python manage.py migrate`
* To run tests, run `docker-compose exec -it app python manage.py test`

## Deploying 

