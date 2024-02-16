#!/usr/bin/env python3

import sys

inputData = sys.stdin.read()

hashVal = 0
for curChar in inputData:
	hashVal += ord(curChar)

print(f"Hash = {hashVal}")

