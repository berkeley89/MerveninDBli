import sqlite3

CREATE_TODOS_TABLE = "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, uuid TEXT, name TEXT, datetime TEXT);"
INSERT_TODO = "INSERT INTO todos (uuid, name, datetime) VALUES (?, ?, ?);"
GET_ALL_TODOS = "SELECT * FROM todos;"
GET_TODOS_BY_NAME = "SELECT * FROM todos WHERE name = ?;"
DELETE_TODO_BY_NAME = "DELETE FROM todos WHERE uuid = ?;"


def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TODOS_TABLE)

def add_todo(connection, uuid, name, dt):
    with connection:
        connection.execute(INSERT_TODO, (uuid, name, dt))

def get_all_todos(connection):
    with connection:
        return connection.execute(GET_ALL_TODOS).fetchall()

def get_todos_by_name(connection, name):
    with connection:
        return connection.execute(GET_TODOS_BY_NAME, (name)).fetchall()

def delete_todo_by_name(connection, uuid):
    with connection:
        connection.execute(DELETE_TODO_BY_NAME, (uuid,))







