# Python Task Manager

A simple command-line task manager built with Python.  
This project allows users to add, view, update, and delete tasks, while also saving tasks to a text file so they can be loaded again when the program starts.

## Features
- Add new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Save tasks to a text file
- Load saved tasks when the program starts
- Validate due dates using `YYYY-MM-DD` format

## Technologies Used
- Python
- File handling
- Lists
- Dictionaries
- `datetime` module

## How It Works
The program displays a menu with five options:

1. Add Task  
2. View Tasks  
3. Update Task  
4. Delete Task  
5. Exit  

Each task contains:
- name
- description
- priority
- due date

Tasks are stored in a text file using this format:

```text
TaskName|Description|Priority|DueDate


How to Run

Make sure Python 3 is installed, then run:

python task_manager.py

If your file still uses the original name, run:

python "Python code_W2153584.py"
File Structure
task_manager.py   # Main Python program
test1.txt         # Saved task data
README.md         # Project documentation
Example Task Data

Example saved tasks from the text file:

Tution|Tution fees|Medium|2025-4-2
Cook|Cook dinner|Medium|2025-4-1
watering|watering plants|low|2025-6-7
Gym|Workout|High|2025-4-3
Watch|Watch a movie|Low|2025-3-31
Requirements
Python 3

No external libraries are required.

Future Improvements
Add JSON storage
Add task search and sorting
Build a graphical user interface
Author : Rivithi Mahendra

