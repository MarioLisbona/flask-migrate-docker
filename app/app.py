from init import app, db
from flask_migrate import Migrate
import os
from flask import jsonify

# bootstrap database migrate commands
db.init_app(app)
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")