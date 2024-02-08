import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout = "wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    

st.title("Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase our productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        

st.text_input(label = "Enter a todo", placeholder = "type here...",
              on_change = add_todo, key = 'new_todo')

