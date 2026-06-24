'''from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    print("Hello world")
app.run(debug="True")'''
#CREATES A TASK. Asks the user for a title and description, then prints that the task was created successfully
tasks = []
def create_tasks():
    title = input("Enter your Task Title: ")
    description = input("Enter Your Task Description: ")
    tasks.append({"Task Title": title, "Task Description": description})
    print("Task Created Successfully")
#VIEW TASKS. Iterates through the list of tasks, showing the title, then description. If none are available, print such.
def see_tasks():
    if tasks:
        print("Available Tasks")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Task Title: {task['Task Title']}, Task Description: {task['Task Description']}")
    else:
        print("No Tasks Available")
"""UPDATE TASKS. Prints available tasks, and asks the user to give a valid index for a task
 they want to be removed.
They ask the user for a new task title and description"""
def update_tasks():
    see_tasks()
    if tasks:
        try:
            tasks_index = int(input("Provide the Index of your task to be updated: ")) - 1
            if 0 <= tasks_index < len(tasks):
                new_task_title = input("Provide new task title. Press ENTER to keep current title: ")
                new_task_description = input("Provide new description. Press ENTER to keep current description: ")
                if new_task_title:
                    tasks[tasks_index]["Task Title"] = new_task_title
                if new_task_description:
                    tasks[tasks_index]["Task Description"] = new_task_description
                print("Task Update")
            else:
                print("Invalid Index")
        except ValueError:
            print("Enter an expected number")
    else:
        print("No tasks available")
#DELETE TASKS
#Asks for the index of the task to be deleted, iterates through the list, and pops the task.
def delete_tasks():
    see_tasks()
    if tasks:
        tasks_index = int(input("Provide the Index of the task to be deleted: ")) - 1
        if 0 <= tasks_index < len(tasks):
            deleted_task = tasks.pop(tasks_index)
            print(f"Deleted Task: {deleted_task['Task Title']} deleted successfully")
        else:
            print("Invalid Index")
#MAIN MENU. Straightforward enough.
while True:
    print("\nWelcome to the Interactive Task Manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter a number between 1 & 5: ")
    if choice == '1':
        create_tasks()
    elif choice == '2':
        see_tasks()
    elif choice == '3':
        update_tasks()
    elif choice == '4':
        delete_tasks()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid. Select between 1 & 5")
#This is a test for whether Git detects edits that I make.