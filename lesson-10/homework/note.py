# Homework 1. ToDo List Application

# 1. Define Task Class
class Task:
    def __init__(self, task_title, description, due_date, status='Incomplete'):
        self.task_title = task_title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.task_title} | {self.description} | Due: {self.due_date} | Status: {self.status}"


# 2. Define ToDoList Class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.task_title}' added successfully!")

    def mark_task_complete(self, task_title):
        for task in self.tasks:
            if task.task_title.lower() == task_title.lower():
                task.mark_complete()
                print(f"Task '{task_title}' marked as complete.")
                return
        print("Task not found!")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nAll Tasks:")
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete:
            print("No incomplete tasks!")
        else:
            print("\nIncomplete Tasks:")
            for task in incomplete:
                print(task)


# 3. Main Program
def main():
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (e.g. 2025-10-10): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)

        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

# Homework 2. Simple Blog System

# 1 Define Post Class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 2 Define Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = {'title': title, 'content': content, 'author': author}
        self.posts.append(post)
        print(f" '{title}' post qo‘shildi!")

    def list_all_posts(self):
        if not self.posts:
            print(' Hozircha hech qanday post yo‘q!')
        else:
            print("\n--- Barcha postlar ---")
            for i, post in enumerate(self.posts, 1):
                print(f"{i}. {post['title']} (muallif: {post['author']})")

    def display_posts_by_author(self, author_name):
        found = [p for p in self.posts if p['author'].lower() == author_name.lower()]
        if not found:
            print(f"'{author_name}' muallifining posti topilmadi.")
        else:
            print(f"\n--- {author_name} muallifining postlari ---")
            for post in found:
                print(f" {post['title']}\n{post['content']}\n")

    def delete_post(self, title):
        for p in self.posts:
            if p['title'].lower() == title.lower():
                self.posts.remove(p)
                print(f" '{title}' posti o‘chirildi.")
                return
        print(f"'{title}' nomli post topilmadi.")

    def edit_post(self, title, new_content):
        for p in self.posts:
            if p['title'].lower() == title.lower():
                p['content'] = new_content
                print(f"'{title}' posti tahrirlandi.")
                return
        print(f"'{title}' nomli post topilmadi.")

    def display_latest_posts(self, n=3):
        if not self.posts:
            print(" Hozircha hech qanday post mavjud emas.")
        else:
            print(f"\n So‘nggi {n} ta post:")
            for p in self.posts[-n:]:
                print(f" {p['title']} (muallif: {p['author']})\n{p['content']}\n")


# 3 Create Main Program (CLI)
def main():
    blog = Blog()
    while True:
        print("\n--- BLOG SYSTEM MENU ---")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlarni ko‘rish")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. So‘nggi postlarni ko‘rish")
        print("7. Chiqish")

        choice = input("Tanlang (1–7): ")

        if choice == '1':
            title = input("Sarlavha: ")
            content = input("Matn: ")
            author = input("Muallif: ")
            blog.add_post(title, content, author)

        elif choice == '2':
            blog.list_all_posts()

        elif choice == '3':
            author = input("Muallif nomi: ")
            blog.display_posts_by_author(author)

        elif choice == '4':
            title = input("O‘chiriladigan post nomi: ")
            blog.delete_post(title)

        elif choice == '5':
            title = input("Tahrirlanadigan post nomi: ")
            new_content = input("Yangi matn: ")
            blog.edit_post(title, new_content)

        elif choice == '6':
            blog.display_latest_posts()

        elif choice == '7':
            print(" Dastur yakunlandi.")
            break
        else:
            print(" Noto‘g‘ri tanlov, qayta urinib ko‘ring.")


# 4 Test the Application
def test_blog():
    print("\n--- BLOG SYSTEM TEST ---")
    blog = Blog()
    blog.add_post("Python asoslari", "Python dasturlash tili eng mashhur tillardan biri.", "Edward")
    blog.add_post("OOP tushunchasi", "Klass va obyektlar haqida tushuntiriladi.", "Jake")
    blog.add_post("SQL darslari", "Ma'lumotlar bazasi bilan ishlash usullari.", "Edward")
    blog.add_post("Machine Learning", "ML — bu sun'iy intellektning muhim sohasi.", "Josh")

    blog.list_all_posts()
    blog.display_posts_by_author("Edward")
    blog.edit_post("SQL darslari", "Yangi SQL mavzusi: GROUP BY va HAVING.")
    blog.delete_post("Machine Learning")
    blog.display_latest_posts(2)


if __name__ == "__main__":
    test_blog()  


# Homework 3. Simple Banking System



# Define Account Class
class Account:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance


# Define Bank Class
class Bank:
    def __init__(self, name="Nomlanmagan bank"):
        self.name = name
        self.accounts = []

    def add_account(self, account_number, account_holder_name, balance=0):
        for acc in self.accounts:
            if acc.account_number == account_number:
                print(" Bu raqamdagi hisob allaqachon mavjud!")
                return
        new_account = Account(account_number, account_holder_name, balance)
        self.accounts.append(new_account)
        print(f" {account_holder_name} uchun yangi hisob yaratildi! (Hisob raqami: {account_number})")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f" {acc.account_holder_name} hisobidagi balans: {acc.balance} so‘m")
        else:
            print(" Bunday hisob topilmadi!")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.balance += amount
            print(f" {amount} so‘m muvaffaqiyatli qo‘yildi. Yangi balans: {acc.balance} so‘m")
        else:
            print(" Hisob topilmadi!")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            if amount > acc.balance:
                print(" Mablag‘ yetarli emas! Overdraft holati.")
            else:
                acc.balance -= amount
                print(f" {amount} so‘m yechildi. Qolgan balans: {acc.balance} so‘m")
        else:
            print(" Hisob topilmadi!")

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)
        if not from_acc or not to_acc:
            print(" Hisoblardan biri topilmadi!")
            return
        if amount > from_acc.balance:
            print(" Mablag‘ yetarli emas, o‘tkazma amalga oshirilmadi.")
        else:
            from_acc.balance -= amount
            to_acc.balance += amount
            print(f" {amount} so‘m {from_acc.account_holder_name} hisobidan {to_acc.account_holder_name} hisobiga o‘tkazildi.")

    def show_account_details(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"\n Hisob tafsilotlari:")
            print(f"Hisob raqami: {acc.account_number}")
            print(f"Hisob egasi: {acc.account_holder_name}")
            print(f"Balans: {acc.balance} so‘m\n")
        else:
            print(" Bunday hisob topilmadi!")



bank = Bank("Milliy Bank")

bank.add_account("1001", "Asadbek", 500_000)
bank.add_account("1002", "Javohir", 300_000)
bank.add_account("1003", "Malika", 150_000)

print("\n--- Balansni tekshirish ---")
bank.check_balance("1001")
bank.check_balance("1002")

print("\n--- Pul qo‘yish ---")
bank.deposit("1001", 200_000)
bank.deposit("1002", 50_000)

print("\n--- Pul yechish ---")
bank.withdraw("1001", 100_000)
bank.withdraw("1002", 500_000) 
print("\n--- Pul o‘tkazish ---")
bank.transfer("1001", "1003", 250_000)

print("\n--- Hisob ma'lumotlari ---")
bank.show_account_details("1001")
bank.show_account_details("1002")
bank.show_account_details("1003")

