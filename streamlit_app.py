import streamlit as st

st.set_page_config(page_title="To Do List", page_icon="📝")

st.title("📝 To Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box
new_task = st.text_input("Add a new task:")

# Add button
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added!")

st.write("---")

# Display tasks
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {task}")
    if col2.button("❌", key=i):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()
