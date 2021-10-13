from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

def run_gleanernabu():
    print('Gleaner Run: %s' % datetime.now())
    os.system('/root/cliDocker -cfg oih_local')
    time.sleep(60)   # Delays for 1 minute (for no real reason)
    print('Nabu Sync: %s' % datetime.now())

def run_gleanernabudiff():
    print('Gleaner Run: %s' % datetime.now())
    os.system('/root/cliDocker -cfg oih_local -mode diff')
    time.sleep(60)   # Delays for 1 minute (for no real reason)
    print('Nabu Sync: %s' % datetime.now())

def run_gleanerDomain():
    print('run for a specific domain: %s' %  datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_gleanerDomain, 'interval', minutes=1) # hours=24 for runs likely
    scheduler.add_job(run_gleanernabudiff, 'interval', hours=48) # hours=24 for runs likely
    scheduler.add_job(run_gleanernabu, 'interval', days=14) # hours=24 for runs likely

    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()

