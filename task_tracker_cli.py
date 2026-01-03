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







def add_task(description):
    new_task = {
        'id': 1,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.datetime.now().isoformat(),
        'updatedAt': datetime.datetime.now().isoformat()
    }


    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            data = json.load(file)

            data.append(new_task)
    else:
        data = [new_task]

    with open(description, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Successfully added data to {description}")
                     



if __name__ == "__main__":
    main()