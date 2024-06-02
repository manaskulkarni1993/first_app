import streamlit as st
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
#print("It is", now)
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    #print(todo)

if __name__ == "__main__":
    st.title("My To-Do App")
    st.write(f"The time is: {now}")
    todos = get_todos()
    for index,i in enumerate(todos):
        checkbox_item = st.checkbox(i, key=i)
        if checkbox_item:
            todos.pop(index)
            write_todos(todos)
            del st.session_state[i]
            st.experimental_rerun()


    st.text_input(label= "Enter a todo item",placeholder="Type here",on_change=add_todo,key="new_todo")



    # print("Hello")

    # st.session_state






