# The Library

The Library is an app I made to show examples of software development skills using Django, APIs, Swagger, VueJS, Docker, and Git. Using packages like Django Rest Framework, DRF Yasg, Drf Extra Fields.

The back-end is made using Django. It is a Books CRUD API, with authors and categories. And a swagger self generated documentation.

The front-end is made using VueJS, loaded by the back-end at the root index. A books listing, with add/update/delete actions. The same for authors and categories. Use router for that, /books, /authors and /categories, and / with a dashboard or metrics overview. Bootstrap 5 is also used, and modals as well.

The application is running dockerized, with 3 containers, one for the django app, other for a mysql database, and other running nginx as a proxy to the django app.


## To use it you just need to:
- have docker and docker-compose installed on your computer
- keep port 80 available, nginx docker will bind to it
- clone this repository and get into it
- $ docker-compose up -d
- point your browser to http://localhost
- I also suggest you run the unit tests
- - [you@app docker shell]$ ./manage.py test --failfast -v3
