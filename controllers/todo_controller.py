from flask import jsonify, Blueprint
from models.todo import Todo

todo_bp = Blueprint('todo', __name__)

# Route to return all todos
@todo_bp.route('/todos', methods=['GET'])
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