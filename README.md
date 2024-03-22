# README

- [tutorial link](https://dev.to/yactouat/flask-postgres-sqlalchemy-migrations-dockerized-intro-2f8p)

## Access PSQL docker image

```bash
psql -h localhost -p 5432 -U mario -d todos
```

## using flask shell locally

1. First, make sure your Flask application is running using Docker Compose.

```bash
docker compose up
```

2.  Once your services are up and running, you can access the terminal of your Python container where Flask is running. You can do this using the docker-compose exec command. Open a new terminal window and run:

```bash
docker-compose exec python sh
```

This command will open a shell session within the Python container.

3. Now, within the container's shell session, you can run the Flask shell command:

```bash
flask shell
```

This command will start an interactive Python shell with your Flask application context loaded, allowing you to interact with your application and database.

That's it! You are now inside the Flask shell within your Docker container, and you can execute Python commands within the context of your Flask application.

## using flask migrate

1. Make sure all your services are up and running

```bash
docker compose up
```

2. Access the terminal for your Python container

```bash
docker compose exec python sh
```

1. You are now within the container's shell session. You can setup Flask-Migrate and add support for your current project with the following command

```bash
flask db init
```

This creates a new migrations directory inside your flask_app folder, where all the migration scripts that manage your migrations will be stored.

If you are familiar with Alembic and want to add advanced configurations to your database migration system, you can modify the generated migrations/alembic.ini file. For our purposes, we will leave it as is.

2. You will now perform your first migration, creating your database’s tables

```bash
flask db migrate -m "Initial migration"
```

Because our database has not been created yet, this output informs you that a new table called `todos` was detected, and a migration script called `b74c0907858c_initial_migration` was created inside a directory called versions, where all different migration versions are stored.

3. With the migration script ready, you can now use it to perform an initial upgrade. This will create the app.db database file and the products table. To do this, run the following command:

```bash
flask db upgrade
```

4. If you delete the containers and rebuild from scratch, once the new containers are up and running, use the following command to initialise the database to its previous state (last migration):

```bash
flask db upgrade
```

## Using flask migrate on the deployed Heroku PSQL

Once PSQL is added to the Heroku application, you need to upgrade it with the latest version. This is done by using the following command which created a one off dyno and then uses flask migrate.

```bash
heroku run flask db upgrade
```

## Access flask shell to update DB directly

This was good practice to access the app shell and manipulate the database directly and add some todos. Use the following command to access the heroku deployed app shell

```bash
heroku run flask shell
```

We can then write some code to seed the Todo table with some data

```python
from app import db, Todo
one = Todo(completed=True, description="Singed up for Xtra-clubs", owner="Mario")
two = Todo(completed=True, description="Be weird and cute", owner="Coda")
three = Todo(completed=True, description="Be an awesome person and cute", owner="Ali")
db.session.add_all([one, two, three])
db.session.commit()
```

The database now has 3 records and this shows up at the `/todos` route.

## links

- https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate
- https://dev.to/yactouat/flask-postgres-sqlalchemy-migrations-dockerized-intro-2f8p

```

```
