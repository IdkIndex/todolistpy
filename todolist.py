#starting note
print("========")
print()
print("todolist.exe")
print()
print("========")
print()
print("ver 1.0")

#opts
print("1. Add a task")
print("2. View tasks")
print("3. Mark task as complete")
print("4. Clear all tasks")
print("5. Delete a task")
print("6. Edit a task")
print("0. Exit")
opt = input("Choose an option: ")
tasks = {}

#loop
while opt != "0":
    print()
    if opt == "1":
        task = input("Enter a task: ")
        tasks[task] = "NOT COMPLETE"
        print()
    elif opt == "2":
        print("tasks:")
        for task, status in tasks.items():
            print(f"{task} - {status}")
        print(f"total tasks: {len(tasks)}")
        print()
    elif opt == "3":
        completed = input("what task complete? ")
        if completed in tasks:
            tasks[completed] = "COMPLETE"
        else:
            print("task not found.")
        print()
    elif opt == "4":
        tasks.clear()
        print("all tasks cleared.")
        print()
    elif opt == "5":
        delete = input("which one? ")
        if delete in tasks:
            del tasks[delete]
            print(f"task '{delete}' deleted.")
        else:
            print("task not found.")
        print()
    elif opt == "6":
        edit = input("edit what? ")
        if edit in tasks:
            new_task = input("enter the new task: ")
            tasks[new_task] = tasks.pop(edit)
            print(f"task '{edit}' updated to '{new_task}'.")
        else:
            print("task not found.")
        print()
    else:
        print('wtf')
        print()
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Clear all tasks")
    print("5. Delete a task")
    print("6. Edit a task")
    print("0. Exit")
    opt = input("Choose an option: ")
#ver 1.0
