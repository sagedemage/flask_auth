# Project 3

[![Production Workflow](https://github.com/sagedemage/flask_auth/actions/workflows/prod.yml/badge.svg)](https://github.com/sagedemage/flask_auth/actions/workflows/prod.yml)
* [Production Deployment](https://flask-auth-prod.herokuapp.com/)

[![Development Workflow](https://github.com/sagedemage/flask_auth/actions/workflows/dev.yml/badge.svg)](https://github.com/sagedemage/flask_auth/actions/workflows/dev.yml)
* [Development Deployment](https://flask-auth-dev.herokuapp.com/)

## About

This is the flask web application for Project 3.

## Environmental Variables
Fill in the environmental variables in .env.test file

## Setting up the docker container of the web applicaiton
Build the docker container:
````
docker-compose build
````
Start the docker container:
````
docker-compose up -d
````
To access the docker container shell:
````
docker exec -it $(docker ps -q) /bin/bash
````

## Unit testing the web application
Access the docker container shell:
````
docker exec -it $(docker ps -q) /bin/bash
````
Remove the database with data if it has data in it:
````
rm database/db.sqlite
````
Then create a new empty database:
````
flask create-db
````
