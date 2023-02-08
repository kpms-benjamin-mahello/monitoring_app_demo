#!/bin/sh

PID="$(netstat -tulpn 2>/dev/null | grep :5002 | awk '{print $NF}' | awk -F '/' '{print $1}')"
echo $PID

if [ -z $PID ]; then
	echo "You can run the application again.."
else
	kill -9 ${PID}
	echo "Process killed, now try again.. "
fi
