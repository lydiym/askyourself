import datetime

import plyer
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

SCHEDULE = '*/1 * * * *'

scheduler = BlockingScheduler()
trigger = CronTrigger.from_crontab(SCHEDULE)


def notify():
    msg = f'hello {datetime.datetime.now()}?'
    plyer.notification.notify(title='Ask the question', message=msg)


def main():
    notify()

    scheduler.add_job(notify, trigger=trigger)
    scheduler.start()


if __name__ == '__main__':
    main()
