import serial
import sys

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

while True:
    sys.stdout.write(ser.readline())
    sys.stdout.flush()