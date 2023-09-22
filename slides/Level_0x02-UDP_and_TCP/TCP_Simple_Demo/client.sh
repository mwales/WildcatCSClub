#!/bin/bash

if [ $# -ne 2 ]; then
	echo "Usage $0 ip portNumber"
	exit 0
fi

remoteAddr=$1
portNumber=$2
echo "Starting TCP client to connect to $remoteAddr :  $portNumber"

./client_output.py | nc -q 5 -N $remoteAddr $portNumber


