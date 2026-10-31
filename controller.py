class TaskController:
    """Контролер координує взаємодію моделі та інтерфейсу."""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            command = self.view.get_user_input()

            if command == "додати":
                task_text = input("Введіть текст завдання: ").strip()
                if self.model.add_task(task_text):
                    self.view.show_message("Завдання успішно додано.")
                else:
                    self.view.show_message("Порожнє завдання не можна додати.")

            elif command == "показати":
                self.view.show_tasks(self.model.get_tasks())

            elif command == "видалити":
                tasks = self.model.get_tasks()
                self.view.show_tasks(tasks)
                if not tasks:
                    continue
                try:
                    number = int(input("Введіть номер завдання для видалення: "))
                    if self.model.delete_task(number - 1):
                        self.view.show_message("Завдання успішно видалено.")
                    else:
                        self.view.show_message("Завдання з таким номером не існує.")
                except ValueError:
                    self.view.show_message("Потрібно ввести ціле число.")

            elif command == "вийти":
                self.model.save_to_file()
                self.view.show_message("Завдання збережено у tasks_db.txt. До побачення!")
                break

            elif command == "":
                self.view.show_message("Введіть одну з доступних команд.")

            else:
                self.view.show_message("Невідома команда. Спробуйте: додати, показати, видалити або вийти.")
