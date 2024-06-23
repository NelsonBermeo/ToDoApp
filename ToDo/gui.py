import functions
import FreeSimpleGUI as fsg

fsg.theme("Black")

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")
complete_button = fsg.Button("Complete")
edit_button = fsg.Button("Edit")
exit_button = fsg.Button("Exit")
list_box = fsg.Listbox(values = functions.get_todos(), key='todos', enable_events = True, size=[45,10])

window = fsg.Window("My To-Do App", 
layout=[[label],
[input_box, add_button], 
[list_box, edit_button, complete_button],
[exit_button]],
font = ("Helvetica",20))


#there is a list inside a list because they would be on the same row, seperate lists within the main list would create different rows
while True:
    event, values = window.read() #This is a tuple, so when we assign variables to it we set variables equal to the values within this tuple 
    print(event) #input val
    print(values) #data in dictionary ex: {"todo": "hi"}
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]#[0]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item before pressing edit", font=("Helvetica",20))
        case "todos": 
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todos = functions.get_todos()
                todos.remove(values["todo"])
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                fsg.popup("Please select an item before pressing edit", font=("Helvetica",20))
        case "Exit":
            break
        case fsg.WIN_CLOSED:
            break


window.close()
