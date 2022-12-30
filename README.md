# The Library

The Library is an app made to show examples of how to develop using Django, APIs, Swagger, VueJS, Docker, and Git. Using packages like Django Rest Framework, DRF Yasg, Drf Extra Fields.

The back-end, in Django, is a Books library CRUD API, with authors and categories. A swagger auto generated documentation is also implemented using drf-yasg.

Front-end is made using VueJS, fully detached from the back-end. A books listing, with add/update/delete actions. And the same actions for authors and categories. Uses vue-router for that, /books, /authors and /categories, and / with a dashboard or metrics overview. Bootstrap 5 is also used, and modals as well.

The application is running dockerized, with 4 containers, django app, mysql database, nginx as a proxy to the django app, and another running the VueJS application with vue-cli.

The user points the browser to the vue application (http://localhost:8080) and the vue app consumes the django API through the NGINX:80. Django API is exposed to the host machine through nginx only, and it's API and also the swagger documentation can be accessed directly also in http://localhost/api/documentation/.


## To use it you just need to:
- have docker and docker-compose installed on your computer
- keep ports 80 and 8080 available, nginx and vuejs containers will bind to them
- clone this repository and get into it
- $ docker-compose up -d
- point your browser to http://localhost:8080
- I also suggest you run the unit tests
- - [you@app docker shell]$ ./manage.py test --failfast -v3
