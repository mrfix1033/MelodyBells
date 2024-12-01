class ScheduledTask:
    def __init__(self, task_id, task, seconds_before_run):
        self.task_id = task_id
        self.task = task
        self.seconds_before_run = seconds_before_run
