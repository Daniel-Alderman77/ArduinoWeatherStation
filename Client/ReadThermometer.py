import serial
import sys

temp_array = []

def read_thermometer():
    ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

    while True:
        temp_str = ser.readline()

        # Remove unecessary character from string leaving just temperature
        temp = temp_str[0:5]

        print temp

        sys.stdout.write(temp)
        temp_array.append(temp)

        print temp_array

        sys.stdout.flush()

read_thermometer()