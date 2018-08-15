import serial
import time
import sys

forward = "\xff\x55\x07\x00\x02\x05\x9c\xff\x64\x00"
stop =    "\xff\x55\x07\x00\x02\x05\x00\x00\x00\x00"

lights = "\xff\x55\x09\x00\x02\x08\x07\x02\x00\x00\xff\xff"


port = serial.Serial("/dev/serial0", baudrate=115200, timeout=3.0)
port.write(lights)
port.write(forward)
time.sleep(2)
port.write(stop)
port.close()