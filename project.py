task = []
def add_task(task):
  """
  Add a new task to the to-do list
  """
  task=task + ""
  print (f"Added task:{task}")
  
  
def remove_task(task):
  """
  Remove a task from to-do list
  """
  if "task" in task:
    task.remove("task")
    print(f"Remove task:{task}")
  else:
    print(f"{task} not found")
    
    
def view_task():
  """
  view all tasks in list
  """
  
  print("To-do list:")
  global task
  for i, task in enumerate(task):
    print(f"{i+1}.{task}")
    
#Main program loop
while True:
  print("\nWhat you want to do")
  print("1. Add a task")
  print("2. Remove a task")
  print("3. View a task")
  print("4. Exit")
  
  choice = input("Enter choice: ")
  
  if choice == "1":
    task = input("Enter a new task: ")
    add_task(task)
  elif choice == "2":
    task = input("Enter task to remove: ")
    remove_task(task)
  elif choice == "3":
    view_task()
  elif choice == "4":
    print("Exiting")
    break
  else:
    print("Invalid choice")
