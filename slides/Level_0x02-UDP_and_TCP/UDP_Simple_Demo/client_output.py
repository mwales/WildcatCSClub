#!/usr/bin/env -S python3 -u

import sys, time

delay = 1000
for i in range(5):
	print("Sending a mesage {}, then sleeping {} ms".format(i, delay))
	if (delay):
		time.sleep(delay / 1000.0)
		delay -= 200

print("Done")

