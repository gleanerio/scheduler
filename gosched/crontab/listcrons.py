from crontab import CronTab

cron = CronTab(user='fils')

for job in cron:
        print(job)


