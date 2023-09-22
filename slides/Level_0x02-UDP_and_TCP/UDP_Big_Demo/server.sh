#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage $0 portNumber"
	exit 0
fi

portNumber=$1
echo "Starting UDP server on port $portNumber"

nc -l -k -u $portNumber 


