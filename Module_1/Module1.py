

urgent_queue = []
normal_queue = []
backlog_queue = []

def enqueue_task(task, priority):
    if priority == "urgent":
        urgent_queue.append(task)
    elif priority == "normal":
        normal_queue.append(task)
    elif priority == "backlog":
        backlog_queue.append(task)
    else:
        print("INVALID PRIORITY")

def dequeue_task(priority):
    if priority == "urgent" and urgent_queue:
        return urgent_queue.pop(0)
    elif priority == "normal" and normal_queue:
        return normal_queue.pop(0)
    elif priority == "backlog":
        return backlog_queue.pop(0)
    else:
        return "No task available or invalid priority"
    

def view_task():
    print("\n--- TASK LIST ---")
    print("Urgent:", urgent_queue)
    print("Normal:", normal_queue)
    print("Backlog:", backlog_queue)
    print("---------------\n")

enqueue_task("Fix production bug", "urgent")
enqueue_task("Finish homework", "normal")
enqueue_task("Clean desk", "backlog")
enqueue_task("Prepare presentation", "urgent")

view_task()

print("Complated", dequeue_task("urgent"))
view_task()