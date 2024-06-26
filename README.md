# nourishcampus

# Introduction

This is the repo for Nourish Campus project.

- The directory nourish_campus is the main module for the project. We implement code inside this module.
- The file requirements.txt defines the packages for running the service of the project.
- The file models.py defines the DB schema of the tables.

- # How To Run
1. Install `virtualenv` if it is not installed. It only needs to be installed once, so in most cases you can skip this step.
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command. Use deactivate or 'source deactivate' to exit the venv
```
$ source ./env/bin/activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Create the database in "Create DB" section

6. Set the environment variable FLASK_APP. The following command is for the project nourish_campus.
```
$ (env) export FLASK_APP=nourish_campus
```

7. Finally start the web server:
```
$ (env) flask run
```

## Create DB
1. Open a terminal in the project root directory and run the following, which removes the old db and creates a new one:
```
$ python db_init.py
```

## Query DB
1. Open a terminal in the project root directory and run:
```
$ sqlite3 nourish_campus/db.sqlite3
```
2. View the tables in DB
```
sqlite> .tables
```
3. View the schema in DB
```
sqlite> .schema
```
4. Run SQL queries
```
sqlite> select * from personal_info;
```

# Tutorials and References
- [How to Use Flask-SQLAlchemy With Flask Blueprints](https://www.youtube.com/watch?v=WhwU1-DLeVw). A video about Flask code structure and database models.
- [Learn Flask for Python - Full Tutorial](https://youtu.be/Z1RJmh_OqeA?si=RZDIhkaCRJwQjdLJ&t=1182). A video about database models and REST API. Watch this for CRUD.
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/2.0.x/blueprints/). Check out the section "Blueprint Resources".
- [Query string arguments in REST APIs with Flask](https://blog.teclado.com/query-string-arguments-in-flask-rest-apis/)
- [Normal forms in DB](https://www.geeksforgeeks.org/normal-forms-in-dbms/). We believe that the DB schema conforms to 3NF and BCNF although we did not prove it.
- [Sending and retrieving form data](https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data)
- [Hot to fix favicon.ico 404 errors](https://appwrk.com/resolving-favicon-ico-404-errors)
- [SQLAlchemy ORM for insert, delete and update](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records)
- [CSRF token issue](https://stackoverflow.com/questions/71725166/bad-request-csrf-token-not-found-csrf-handling-for-flask-wtf)
- [What is CSRF (Cross-site request forgery)](https://portswigger.net/web-security/csrf#what-is-csrf)
