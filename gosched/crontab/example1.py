from datetime import datetime

myFile = open('/tmp/append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))
