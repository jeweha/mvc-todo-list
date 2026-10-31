class TaskModel:
    """Модель даних: зберігає завдання та виконує операції над ними."""

    def __init__(self):
        self._tasks = []

    def add_task(self, task_text):
        """Додає нове завдання."""
        task_text = task_text.strip()
        if not task_text:
            return False
        self._tasks.append(task_text)
        return True

    def get_tasks(self):
        """Повертає копію поточного списку завдань."""
        return self._tasks.copy()

    def delete_task(self, task_index):
        """Видаляє завдання за індексом, який починається з 0."""
        if 0 <= task_index < len(self._tasks):
            del self._tasks[task_index]
            return True
        return False

    def save_to_file(self, filename="tasks_db.txt"):
        """Зберігає поточний список завдань у текстовий файл."""
        with open(filename, "w", encoding="utf-8") as file:
            for task in self._tasks:
                file.write(task + "\n")
