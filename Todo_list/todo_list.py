def get_latest():
    try:
        with open('Todo_list/tasks.txt', 'r') as file:
            num = 0
            for line in file:
                try:
                    current_number = int(line.split('.')[0])
                except ValueError:
                    continue
                num = max(current_number, num)
    except FileNotFoundError:
        # If the file doesn't exist yet, set latest_number to 0
        num = 0
    return num
def todo_add(task_title, task_due_date=None):
    latest_number = get_latest()
    # Append the new task
    with open('Todo_list/tasks.txt', 'a') as file:
        next_number = latest_number + 1
        file.write(f"{next_number}. {task_title}")
        if task_due_date:
            file.write(f" {task_due_date}")
        file.write("\n")


def todo_complete():
    pass

def todo_view():
    pass

def todo_remove():
    pass

