from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    content: str


class IdGenerator:
    def __init__(self):
        self._id = 1

    def get_next_id(self):
        current_id = self._id
        self._id += 1
        return current_id


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.id_generator = IdGenerator()

    def add_task(self, title, content="empty_content"):
        task_id = self.id_generator.get_next_id()
        self.tasks[task_id] = {"task": Task(task_id, title, content), "toggled": False}

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def delete_task(self, task_id: int):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError(f"Задача с id: {task_id} не найдена")

    def toggle_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["toggled"] = not self.tasks[task_id]["toggled"]
        else:
            ValueError(f"Задача с id: {task_id} не найдена")


task_manager = TaskManager()
task_manager.add_task("task1", "content_of_task1")
task_manager.add_task("task2")
task_manager.add_task("task3", "content_of_task3")
task_manager.add_task("task4", "content_of_task4")
print(task_manager.tasks)
print(task_manager.get_task(1))
print(task_manager.get_task(1)["toggled"])
print(task_manager.get_task(2))
print(task_manager.get_task(2)["toggled"])
print(task_manager.get_task(3))
print(task_manager.get_task(3)["toggled"])
task_manager.toggle_task(3)
task_manager.delete_task(4)
print(task_manager.tasks)
