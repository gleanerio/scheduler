from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

def run_gleanernabu():
    print('Gleaner Run: %s' % datetime.now())
    time.sleep(60)   # Delays for 1 minute (for no real reason)
    print('Nabu sync, likely part of gleaner run script?: %s' % datetime.now())

def run_gleaner():
    print('Just run gleaner, dont trigger nabu: %s' % datetime.now())

def run_sourcechecks():
    print('Looks for source by heading the sitemap: %s' % datetime.now())

def run_gleanerDomain():
    print('run for a specific domain: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_gleaner, 'interval', minutes=45) # hours=24 for runs likely
    scheduler.add_job(run_gleanernabu, 'interval', minutes=60) # need run after Gleaner..   so just make part of Gleaner? 
    scheduler.add_job(run_gleanerDomain, 'interval', minutes=120) # need run after Gleaner..   so just make part of Gleaner? 

    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
