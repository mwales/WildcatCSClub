#!/usr/bin/env -S python3 -u

import sys, time

delay = 1000
for i in range(100):
	print("Sending a really really really long long long mesage {}, gosh, seems like it will never end.  then sleeping {} ms {}".format(i, delay, "a" * 500))
	if (delay):
		time.sleep(delay / 1000.0)
		delay -= 200

print("Done")

