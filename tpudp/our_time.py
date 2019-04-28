import time
import math
from struct import pack


def get_time_in_bin():
    global pack
    # Add seconds from 1900 to 1970
    curTime = int(math.floor(time.time())) + 2208988800
    return pack("!L", curTime)