from mrfix1033.melodybells.scheduler.ScheduledTask import ScheduledTask


class Scheduler:
    def __init__(self):
        self.tasks: dict[int, ScheduledTask] = dict()
        self.next_task_id = 1

    def run_later(self, task, seconds: float) -> ScheduledTask:
        task_id = self.next_task_id
        self.next_task_id += 1
        task = ScheduledTask(task_id, task, seconds)
        self.tasks[task_id] = task
        return task

    def cancel(self, task_id: int):
        del self.tasks[task_id]

    def tick(self):
        for task in self.tasks.values():
            task.seconds_before_run -= 1
            if task.seconds_before_run < 0:
                task.task()
                self.cancel(task.task_id)
