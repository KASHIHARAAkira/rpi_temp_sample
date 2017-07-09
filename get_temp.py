from LM60Pi import lm60

import time

temp = lm60.LM60(0,0,0)

try:
  while True:
    val = temp.read()
    val = int(val * 1000) / 1000
    print(val)
    time.sleep(5)

except KeyboardInterrupt:
  temp.end()
