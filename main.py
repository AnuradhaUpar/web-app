import  streamlit as st
import function  as fun


def add_todo():
    todo=st.session_state["new_todo"] + '\n'
    todos.append(todo)
    fun.write_todos(todos)
    print(todo)

st.title("hello Friends")
st.header("My Web App")
st.subheader("Todo List")
st.write("this app is to improve productivity")
todos=fun.get_todos()
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(checkbox)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    
st.text_input(label=" ",placeholder="add todo",on_change=add_todo,key="new_todo")
