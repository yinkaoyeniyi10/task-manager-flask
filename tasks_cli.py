#CREATES A TASK. Asks the user for a title and description, then prints that the task was created successfully
tasks = []
def create_tasks(title, description):
    tasks.append({"Task Title": title, "Task Description": description});
#VIEW TASKS. Iterates through the list of tasks, showing the title, then description. If none are available, print such.
def see_tasks():
    return tasks
def update_tasks(index, new_title=None, new_description=None):
    see_tasks()
    if 0 <= index < len(tasks):
        new_title = input("Provide new task title. Press ENTER to keep current title: ")
        new_description = input("Provide new description. Press ENTER to keep current description: ")
        if new_title:
            tasks[index]["Task Title"] = new_title
        if new_description:
            tasks[index]["Task Description"] = new_description
            print("Task Update")
        return True
    return False
def delete_tasks(index):
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            return deleted
        return None