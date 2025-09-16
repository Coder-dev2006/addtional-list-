

TASK_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("📌 Vazifalar ro‘yxati bo‘sh.")
    else:
        print("\n📋 Vazifalar:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    new_task = input("➕ Vazifa nomini kiriting: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Vazifa qo‘shildi.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("❌ O‘chirish uchun vazifa raqamini kiriting: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"✅ \"{removed}\" o‘chirildi.")
    except (ValueError, IndexError):
        print("⚠️ Noto‘g‘ri raqam kiritildi.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-do List ---")
        print("1. Vazifalarni ko‘rish")
        print("2. Vazifa qo‘shish")
        print("3. Vazifa o‘chirish")
        print("4. Chiqish")

        choice = input("Tanlovingiz: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Dastur tugadi.")
            break
        else:
            print("⚠️ Noto‘g‘ri tanlov!")


if __name__ == "__main__":
    main()
