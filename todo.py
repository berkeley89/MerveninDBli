import database
from flask import Flask, request, jsonify, render_template
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import uuid
from datetime import datetime



app = Flask(__name__)

schema = {
    "type" : "object",
    "properties" : {
        "todo" : {"type" : "string"}
    }
}

# def todos():
#     connection = database.connect()
#     database.create_tables(connection)
#     return connection

@app.route("/")
def index():
    connection = database.connect()
    todos = database.get_all_todos(connection)
    print(todos)
    connection.close()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
     todo = request.form['message']
     task_id = str(uuid.uuid4())
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     connection = database.connect()
     database.add_todo(connection,task_id,todo,dt_string)
     todos = database.get_all_todos(connection)
     connection.close()
     return render_template("index.html", todos=todos)


#     try:
#         validate(instance=todo, schema=schema)
#         print("Validation successful")
#         global task_id # to use outside of this func
#         task_id = str(uuid.uuid4())
#         todo_item = {"id": task_id, "title": todo["todo"]}
#         now = datetime.now()
#         dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#         database.add_todo(todos(),todo_item["id"], todo_item["title"], dt_string)
#         return todo_item, 201
#     except ValidationError as err:
#         return {"message": f"fuck you bc {err.message}"}, 400

@app.route("/delete", methods=["POST"])
def delete():
    todo = request.form['delete']
    print(todo)
    delete_this = request.args.get('id')
    #print(delete_this)
    connection = database.connect()
    database.delete_todo_by_name(connection, todo)
    todos = database.get_all_todos(connection)
    connection.close()
    return render_template("index.html", todos=todos)
if __name__ == '__main__':
    app.run(debug=True)

