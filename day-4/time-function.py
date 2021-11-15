
###################################################
# This it a time and date function
# The result will be Monday November 15, 2021
import datetime 

def date():
    date = datetime.datetime.now()
    print(date.strftime("%A %B %d, %Y"))


def time():
    time = datetime.datetime.now()
    print(time.strftime("%I:%M:%S "))


date()
time()

