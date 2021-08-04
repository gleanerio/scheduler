from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

def train_model():
    print('Gleaner Run: %s' % datetime.now())
    time.sleep(60)   # Delays for 1 minute (for no real reason)
    print('Nabu sync, likely part of gleaner run script?: %s' % datetime.now())

def train_model5():
    print('Nabu sync, likely part of gleaner run script?: %s' % datetime.now())

def train_model5():
    print('After Nabu run, need to sync? and stop, start RO blaze and copy over journal file: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(train_model, 'interval', minutes=1) # hours=24 for runs likely
    scheduler.add_job(train_model5, 'interval', minutes=5) # need run after Gleaner..   so just make part of Gleaner? 
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
