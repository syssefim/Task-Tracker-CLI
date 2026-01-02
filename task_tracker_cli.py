import sys
import json















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
    with open('tasks.json', 'w') as json_file:
        json.dump(description, json_file, indent=4)



if __name__ == "__main__":
    main()