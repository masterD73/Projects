# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer:
# AI2 InfinityLabs.
# ----------------------------
from time import sleep

import pause
import itertools
from random import randint
from attr import dataclass
from heapq import heappush, heappop
from typing_extensions import Callable
from datetime import datetime, timedelta


class PriorityQueue:
    def __init__(self):
        self.tasks = []
        self.counter = itertools.count()

    def push(self, priority, task, frequency):
        """Add a new task or update the priority of an existing task"""
        count = next(self.counter)
        heappush(self.tasks, (priority, count, task, frequency))

    def pop(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        return heappop(self.tasks)

    def task_manager(self, tasks: list):
        for priority, task, frequency in tasks:
            self.push(priority, task, frequency)

    def __str__(self):
        return str(self.tasks)

    def __len__(self):
        return len(self.tasks)

    def peek(self):
        return self.tasks[0]

    def is_empty(self):
        return len(self) == 0


def example():
    while True:
        print("I am example")
        if randint(0, 1) == 1:
            yield 2
        else:
            break
    yield


def example1():
    while True:
        print("I am example1")
        if randint(0, 1) == 1:
            yield 2
        else:
            break
    yield


def example2():
    while True:
        print("I am example2")
        if randint(0, 1) == 1:
            yield 2
        else:
            break
    yield


class Sleep:
    def __init__(self, seconds):
        self.seconds: int = 0

    def wait(self):
        sleep(self.seconds)

    def time_object(self):
        return timedelta(seconds=self.seconds)


high = 0
medium = 1
low = 2

gen1, gen2, gen3 = example(), example1(), example2()

queue = PriorityQueue()
tasks = [(datetime.now() + timedelta(seconds=1), gen1, timedelta(seconds=2)),
         (datetime.now() + timedelta(seconds=5), gen2, timedelta(seconds=1)),
         (datetime.now() + timedelta(seconds=3), gen3, timedelta(seconds=4))]
queue.task_manager(tasks)
for task in sorted(tasks):
    assert queue.pop()[0] == task[0]


@dataclass
class Tasks:
    time_point: datetime
    call: Callable


class Scheduler:
    def __init__(self):
        self.queue = PriorityQueue()

    def add(self, time_point, action_func, frequency):
        task = Tasks(time_point, action_func)
        self.queue.push(task.time_point, task.call, frequency)

    def run(self):
        while self.queue.tasks:
            time, counter, action, frequency = self.queue.pop()
            print(f"The time is {time} and everything is alright.")
            pause.until(time)
            try:
                result = timedelta(seconds=next(action) or 0)
                self.add(time + result, action, result)
            except StopIteration:
                print(f"iteration of generator {action} has ended.")


timer = Scheduler()
for element in tasks:
    timer.add(element[0], element[1], element[2])
timer.run()
