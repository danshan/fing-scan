#!/bin/sh

SCAN_RANGE="192.168.10.1/24"
CURRENT=current.log
PREVIOUS=previous.log

#fing -n "$SCAN_RANGE" -r1 -o log,text | grep "HW Address" | awk -F ' ' '{ print $3 }' | sort > $CURRENT
if [ ! -f "$PREVIOUS" ]; then
  touch "$PREVIOUS"
fi

# device offline
for mac in `diff $PREVIOUS $CURRENT | grep '<' | awk '{print $2}'`; do
    ./send_huginn.py "$mac" "offline"
done

# device online 
for mac in `diff $PREVIOUS $CURRENT | grep '>' | awk '{print $2}'`; do
    ./send_huginn.py "$mac" "online" 
done
