import  streamlit as st
import function  as fun


def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo)
    fun.write_todos(todos)
    print(todo)


st.title("hello Friends")
st.header("My Web App")
st.subheader("Todo List")
st.text("this app is to improve productivity")
todos=fun.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="add todo",placeholder="add todo",on_change=add_todo,key="new_todo")

st.session_state
print("hello")