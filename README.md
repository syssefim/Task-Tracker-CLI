# This is one of the beginner projects from the backend developer roadmap from the website [roadmap.sh](https://roadmap.sh/projects/task-tracker). 



💻 Installation \& Setup:

* Clone the repository in the terminal as so:

      git clone https://github.com/syssefim/Task-Tracker-CLI

      cd task-tracker-cli

* In the terminal navigate to the folder containing the project
* Now you're ready for the 📖 Usage Guide











📖 Usage Guide

1. Add a task:
   	(To add a task write)
   
         python task\_tracker\_cli.py add "Buy groceries"
3. List all tasks or filter by status (todo, in-progress, done):
   	(To either list all tasks or list tasks by their status write)
   
   		# List all
   		python task\_tracker\_cli.py list

   		# List by status
   		python task\_tracker\_cli.py list done
   		python task\_tracker\_cli.py list todo
5. Update a task:
   	(To change the description of a task given it's id write)
   
   		# Usage: update <id> <new\_description>
   		python task\_tracker\_cli.py update 1 "Buy groceries and cook dinner"
7. Delete a task:
   	(To delete a task given it's id write)
   
   		# Usage: delete <id>
   		python task\_tracker\_cli.py delete 1
9. Change task status:

   (You can change the status of any given task either to "in progress" or "done". To do so write)

         # Mark as In Progress
         python task\_tracker\_cli.py mark-in-progress 1

         # Mark as Done
         python task\_tracker\_cli.py mark-done 1

