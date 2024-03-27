import os
from flask import jsonify
from init import app, db
from models.todo import Todo
from controllers.home_controller import home_bp
from controllers.todo_controller import todo_bp
from controllers.msg_controller import msg_bp

print('This is data from the .env file\n', os.environ['TEST_DATA'])
print("DEBUG ===============> ",app.config['DEBUG'])
print("DEVELOPMENT =========> ",app.config['DEVELOPMENT'])

# register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(todo_bp)
app.register_blueprint(msg_bp)





if __name__ == "__main__":
    app.run(host="0.0.0.0")