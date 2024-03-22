from init import app, db
from flask_migrate import Migrate

# bootstrap database migrate commands
db.init_app(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String(), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    owner = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<Todo {self.id}, {self.completed}, {self.description}>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")