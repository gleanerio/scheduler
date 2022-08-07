from crontab import CronTab


cron = CronTab(user='fils')
job = cron.new(command='python /home/fils/src/Projects/gleaner.io/scheduler/crontab/example1.py')
job.minute.every(1)

cron.write()
#cron.remove(job)

for job in cron:
        print(job)

