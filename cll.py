import functions
import time

now = time.strftime("%m - %Y")
print("It is ", now)
while True:
    user_action = input("Type in add, show, edit, complete, or exit: ").strip()
    
    if user_action.startswith("add"):
        todo = (user_action[4:] + "\n").title()
        todos = functions.get_todos() 
        todos.append(todo)
        functions.write_todos(todos)
        
        print("Your task has been added")
    elif user_action.startswith("show"):
        #we can create a dedicated folder for files and todos.txt would be switched to "files/todos.txt"
        todos = functions.get_todos() 
        for i,j in enumerate(todos):
            new_j = j[:-1]
            print(f"{i+1}-{new_j}")
        
    elif user_action.startswith("edit"):
        try:
            edit_num = int(user_action[5:])-1
            todos = functions.get_todos() 
            edit = input("Enter new todo: ")
            todos[edit_num] = edit + "\n"
            functions.write_todos(todos)
            print("The task has been updated")
        except ValueError:
            print("Your command is not valid, please put in a number after edit")
            continue
            #user_action = input("Type in add, show, edit, complete, or exit: ").strip()

    elif user_action.startswith("complete"):
            try:
                remove = int(user_action[9:])-1
                todos = functions.get_todos() 
                removed_element = todos[remove]
                todos.remove(removed_element)
                functions.write_todos(todos)
                print_removed = removed_element[:-1]
                
                print(f"{print_removed} has been marked completed")
            except IndexError:
                print("This task does not exist, value too large")
                continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid!")
        