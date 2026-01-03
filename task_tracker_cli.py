import sys
import json
import datetime
import os

#constant so we can easily change the name of the json file if necessary
TASK_FILE = 'tasks.json'







#main function that appropriately calls the correct function based on user input
def main():
    if len(sys.argv) < 2:
            print("Usage: task-cli <command> [arguments]")
            return    
    
    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
                print("Error: Missing task description.")
        else:
            add_task(sys.argv[2])
    elif command == 'update':
        if len(sys.argv) < 3:
                print("Error: Missing task description.")
        else:
            print(sys.argv[2])
            update_task(sys.argv[2], sys.argv[3])
    elif command == 'delete':
        if len(sys.argv) < 2:
                print("Error: Missing task ID.")
        else:
            delete_task(sys.argv[2])
    elif command == 'mark-in-progress':
        if len(sys.argv) < 2:
                print("Error: Missing task ID.")
        else:
            mark_in_progress_task(sys.argv[2])
    elif command == 'mark-done':
        if len(sys.argv) < 2:
                print("Error: Missing task ID.")
        else:
            mark_done_task(sys.argv[2])
    elif command == 'list':
        if len(sys.argv) <= 2:
                list_tasks()
        else:
            list_tasks(sys.argv[2])
    else:
        print ("command not recognized...")














#open tasks.json if it exists and return it, otherwise create tasks.json and return it
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r') as file: #this opens the json file for reading
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

#saves data to tasks.json and then closes it
def save_tasks(tasks):
    try:
        with open(TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")




#function that adds tasks to tasks.json
def add_task(description):
    tasks = load_tasks()

    new_id = 1 if not tasks else max(t['id'] for t in tasks) + 1

    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.datetime.now().isoformat(),
        'updatedAt': datetime.datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")
                     

#function that changes the task description of a task given it's id
def update_task(task_id, new_description):
     tasks = load_tasks()
     for task in tasks:
        if task['id'] == int(task_id): 
            task['description'] = new_description
            task['updatedAt'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
     print(f"Task with ID {task_id} not found.")


#function that deletes a task given it's id
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != int(task_id)]
    
    if len(tasks) == len(new_tasks):
        print(f"Task with ID {task_id} not found.")
    else:
        save_tasks(new_tasks)
        print(f"Task {task_id} deleted successfully.")

#function that marks a task's status as inprogress given it's id
def mark_in_progress_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == int(task_id): 
            task['status'] = "inprogress"
            task['updatedAt'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")

#function that marks a task's status as done given it's id
def mark_done_task(task_id):
     tasks = load_tasks()

     for task in tasks:
        if task['id'] == int(task_id): 
            task['status'] = "done"
            task['updatedAt'] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
     print(f"Task with ID {task_id} not found.")

#function that lists all tasks, optionally filtering by status
def list_tasks(status_filter=None):
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        # If a filter is provided (e.g., 'done'), skip tasks that don't match
        if status_filter and task['status'] != status_filter:
            continue
            
        print(f"[{task['id']}] {task['description']} - {task['status']}")






if __name__ == "__main__":
    main()