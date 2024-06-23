FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Opens default file todos.txt, reads the lines and returns list of todo items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines() 
    return todos_local

def write_todos(todos_local, filepath=FILEPATH):
    """Opens default file todos.txt and a list of edited todo items and overwrites the list into todos.txt"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)
