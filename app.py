import os
from flask import jsonify
from init import app, db
from models.todo import Todo

print('This is data from the .env file\n', os.environ['TEST_DATA'])
print("DEBUG ===============> ",app.config['DEBUG'])
print("DEVELOPMENT =========> ",app.config['DEVELOPMENT'])

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

@app.route("/msg", methods=["GET"])
def get_api_base_url():
    return jsonify({
        "msg": "todos api is up",
        "success": True,
        "data": None
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")