# README

- [tutorial link](https://dev.to/yactouat/flask-postgres-sqlalchemy-migrations-dockerized-intro-2f8p)

- using flask shell

> First, make sure your Flask application is running using Docker Compose. You can start your services with:
> Copy code
> docker-compose up
> Once your services are up and running, you can access the terminal of your Python container where Flask is running. You can do this using the docker-compose exec command. Open a new terminal window and run:
> bash
> Copy code
> docker-compose exec python sh
> This command will open a shell session within the Python container.

> Now, within the container's shell session, you can run the Flask shell command:
> Copy code
> flask shell
> This command will start an interactive Python shell with your Flask application context loaded, allowing you to interact with your application and database.

> That's it! You are now inside the Flask shell within your Docker container, and you can execute Python commands within the context of your Flask application.

- Access PSQL docker instasnce
  - psql -h localhost -p 5432 -U mario -d todos
