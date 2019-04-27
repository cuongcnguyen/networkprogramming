from datetime import datetime


def print_time(timeStamp):
    print(datetime.utcfromtimestamp(timeStamp - 2208988800).strftime('%Y-%m-%d %H:%M:%S'))