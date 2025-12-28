#!/usr/bin/env python3

import time
import threading
from typing import Any, Callable

class PeriodicTask:
    def __init__(self, callback: Callable[..., Any], interval: float):
        self.callback = callback
        self.interval = interval
        self.nextRun = 0.0

class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: PeriodicTask):
        self.tasks.append(task)

    def run(self):
        for task in self.tasks:
            current_time = time.time()

            if current_time >= task.nextRun:
                thread = threading.Thread(target=task.callback)
                thread.start()

                task.nextRun = current_time + task.interval