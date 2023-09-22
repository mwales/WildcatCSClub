#!/usr/bin/env -S python3 -u

import sys, time

delay = 3000
for i in range(6):
	print("Sending a short message {}, then sleeping {} ms".format(i, delay))
	if (delay):
		time.sleep(delay / 1000.0)
		delay -= 1000

print("Done")

