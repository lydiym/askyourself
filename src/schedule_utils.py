import json
from datetime import datetime

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
PythonService = autoclass('org.kivy.android.PythonService')

TaskScheduler = autoclass('org.atq.atq.TaskScheduler')


def _to_millis(time: datetime):
    return int(time.timestamp() * 1000)


def schedule_task(task_time: datetime):
    context = PythonActivity.mActivity or PythonService.mService

    task_time = _to_millis(task_time)
    task_scheduler = TaskScheduler(context)

    task_scheduler.scheduleTask(task_time)
