import streamlit as st

st.title("📝 My To-Do List")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box
new_task = st.text_input("Enter a new task")

# Add task button
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task")

st.subheader("Your Tasks")

# Display tasks
for index, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{index + 1}. {task}")
    if col2.button("❌", key=index):
        st.session_state.tasks.pop(index)
        st.experimental_rerun()
