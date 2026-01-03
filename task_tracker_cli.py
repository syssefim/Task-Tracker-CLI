import sys
import json
import datetime
import os

#constant so we can easily change the name of the json file if necessary
TASK_FILE = 'tasks.json'













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
        print('registered update')
    elif command == 'delete':
        print('registed delete')
    elif command == 'mark-in-progress':
        print('registed mark-in-progress')
    elif command == 'mark-done':
        print('registered mark-done')
    elif command == 'list':
        print ('registered list')
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


def save_tasks(tasks):
    try:
        with open(TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")





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
                     



if __name__ == "__main__":
    main()