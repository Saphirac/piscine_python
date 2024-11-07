import time
from datetime import datetime

f_time = "{:,.4f}".format(time.time())
e_time = "{:.2E}".format(time.time())

print(f_time, e_time)
print(strftime("%a", gmtime()))
