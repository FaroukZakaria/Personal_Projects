"""import todo_list
complete = __import__('todo_list').todo_complete
view = __import__('todo_list').todo_view
remove = __import__('todo_list').todo_remove"""

print("(h for help)")
while True:
    interpreter = (str(input("Select your action: ")))
    
    if interpreter == 'h':
        print("""1 for adding a task\n
              2 for completing a task\n
              3 for removing a task\n
              4 for viewing a task\n
              """)
        continue

    elif (interpreter == 'exit' or
    interpreter == 'quit' or
    interpreter == 'q' or
    KeyboardInterrupt):
        print("Bye")
        break

    
    elif interpreter == '1':
        title = input("Enter the title of task: ")
        due_date = input("Enter the due date (ignore for none): ")
        # add(title, due_date=None)
    
    elif interpreter == '2':
        #view()
        task = input("Select task: ")
        #complete(task)
    
    elif interpreter == '3':
        #view()
        task = input("Select task: ")
        #remove(task)
    
    elif interpreter == '4':
        #view()
        pass
    
    else:
        print ("I'm sorry. Invalid answer, try again.")