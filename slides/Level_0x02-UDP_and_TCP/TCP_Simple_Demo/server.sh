#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage $0 portNumber"
	exit 0
fi

portNumber=$1
echo "Starting TCP server on port $portNumber"

nc -l -k $portNumber 


