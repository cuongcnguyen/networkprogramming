import time
import math
from struct import pack


def get_time_in_bin():
    global pack
    # Add time between 1900 and 1970
    curTime = int(math.floor(time.time())) + 2208988800
    return pack("!L", curTime)