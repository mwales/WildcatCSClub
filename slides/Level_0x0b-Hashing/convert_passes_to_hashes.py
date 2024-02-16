#!/usr/bin/env python3

import hashlib
import sys
import time

def compute_md5_hash(input_string):
	# Encode the input string to bytes
	input_bytes = input_string.encode('utf-8')
    
	# Create an MD5 hash object
	hasher = hashlib.md5()
    
	# Update the hash object with the bytes to hash
	hasher.update(input_bytes)
    
	# Get the hexadecimal representation of the digest
	hash_digest = hasher.hexdigest()
    
	return hash_digest

def createHashList(pl):
	retVal = []
	for spw in pl:
		dig = compute_md5_hash(spw)
		retVal.append( (dig, spw) )
	return retVal

def main(args):

	if len(args) != 3:
		print(f"Usage: {sys.argv[0]} password_list_file hashes_file")
		return

	pf = open(args[1], "r")
	pfdata = pf.read()
	passList = pfdata.split("\n")
	pfdata = ""
	pf.close()

	start_time = time.time()
	hl = createHashList(passList)
	stop_time = time.time()
	createTime = stop_time - start_time

	print(f"Time to hash {len(passList)} was {createTime} seconds")

	for i in range(5):
		print(f"{hl[i]}")

	hashLookup = dict()
	start_time = time.time()
	for hi in hl:
		hashLookup[hi[0]] = hi[1]
	stop_time = time.time()
	order_time = stop_time - start_time

	print(f"Time to reorder is {order_time} seconds")

	while(True):
		print("Give me a hash to lookup")
		userHash = sys.stdin.readline().strip()

		passVal = hashLookup.get(userHash, "NOT FOUND")
		print(passVal)



if __name__ == "__main__":
	main(sys.argv)
