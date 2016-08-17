import serial
import sys

temp_array = []

def read_thermometer():
    try:
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

    except serial.serialutil.SerialException:
        print "Could not detect Arduino on port: /dev/cu.usbmodem1411"

read_thermometer()