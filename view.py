class TaskView:
    """Консольний інтерфейс. Не містить логіки зберігання даних."""

    def show_tasks(self, tasks_list):
        if not tasks_list:
            print("Список завдань порожній.")
            return

        print("\nВаші завдання:")
        for number, task in enumerate(tasks_list, start=1):
            print(f"{number}. {task}")

    def show_message(self, message):
        print(message)

    def get_user_input(self, prompt="Введіть команду"):
        return input(f"{prompt} (додати / показати / видалити / вийти): ").strip().lower()
