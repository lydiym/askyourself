import json
import os
import random
from datetime import datetime, timedelta

from kivy.app import App
from kivy.logger import Logger
from plyer import notification

from schedule_utils import schedule_task

questions = [
    "foo",
    "bar"
]

if __name__ == '__main__':
    question = random.choice(questions)

    notification.notify(
        title='Ask the question',
        message=f"{question}?",
        app_name=App.title,
        timeout=0
    )

    schedule_task(datetime.now() + timedelta(minutes=1))
