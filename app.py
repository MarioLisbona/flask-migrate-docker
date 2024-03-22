from flask_migrate import Migrate
import os
from flask import jsonify
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# creates an application that is named after the name of the file
app = Flask(__name__)

app.config["SECRET_KEY"] = "some_dev_key"
# Check if running on Heroku
if 'DATABASE_URL' in os.environ:
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL').replace(
        'postgres://', 'postgresql+psycopg2://', 1)
else:
  # Local PostgreSQL database URL
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['LOCAL_DATABASE']

db = SQLAlchemy(app)

# bootstrap database migrate commands
migrate = Migrate(app, db)

print('This is data from the .env file\n', os.environ['TEST_DATA'])

class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String(), nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    owner = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f"<Todo {self.id}, {self.completed}, {self.description}>"
    

# Route to return all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    todo_list = []
    for todo in todos:
        todo_list.append({
            'id': todo.id,
            'completed': todo.completed,
            'description': todo.description,
            'due_date': todo.due_date.isoformat() if todo.due_date else None,
            'owner': todo.owner
        })
    return jsonify(todo_list)

@app.route('/')
def home():
    return jsonify({
        "msg": "Welcome"
    })

@app.route("/message", methods=["GET"])
def get_api_base_url():
    return jsonify({
        "msg": "todos api is up",
        "success": True,
        "data": None
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")