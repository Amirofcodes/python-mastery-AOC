

def display_menu():
    print("\n" + "=" * 40)
    print("📝 To-Do List Manager v1.0")
    print("=" * 40)
    print("1) Add task")
    print("2) List tasks")
    print("3) Toggle done by id")
    print("4) Delete by id")
    print("5) Clear all")
    print("6) Quit")
    print("=" * 40)


def add_task(tasks, next_id):
    title = input("Enter your task Title: ").strip()
    if title:
        task = {"id": next_id, "title": title, "done": False}
        tasks.append(task)
        print(f"✅ Added task #{next_id}: {title}")
        return next_id + 1
    else:
        print("❌ Task title cannot be empty")
        return next_id


def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet!")
        return
    print(f"\n You have {len(tasks)} Total")
    for task in tasks:
        status = "[X]" if task["done"] else "[ ]"
        print(f"[{task['id']}] {status} {task['title']}")


def toggle_by_id(tasks):
    task_id = int(input("Choose a task ID: "))
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            return
    print(f"❌ Task with ID {task_id} not found")


def delete_by_id(tasks):
    task_id = int(input("Choose a task ID: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
    print(f"❌ Task with ID {task_id} not found")


def clear_all(tasks):
    if tasks:
        count = len(tasks)
        tasks.clear()
        print(f"✅ Cleared {count} tasks")
    else:
        print("📭 No tasks to clear")


def run_todo_manager():
    tasks = []
    next_id = 1

    while True:
        display_menu()
        choice = int(input("Choose an option: "))
        if choice < 1 or choice > 6:
            print("❌ Invalid choice. Please choose 1-6.")
            continue
        if choice == 6:
            print("Thank you for using To-Do List Manager v1.0 !")
            break
        if choice == 1:
            next_id = add_task(tasks, next_id)
        elif choice == 2:
            list_tasks(tasks)
        elif choice == 3:
            toggle_by_id(tasks)
        elif choice == 4:
            delete_by_id(tasks)
        elif choice == 5:
            clear_all(tasks)


if __name__ == "__main__":
    run_todo_manager()
