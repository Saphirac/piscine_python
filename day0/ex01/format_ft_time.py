import time
from datetime import datetime

now = datetime.now()

f_time = "{:,.4f}".format(time.time())
e_time = "{:.2E}".format(time.time())

print("Seconds since January 1, 1970:",
      f_time, "or", e_time, "in scientific notation")
print(now.strftime("%b %d %Y"))
