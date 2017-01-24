import serial
import sys

temp_array = []
arduino_string = '/dev/cu.usbmodem1421'


def read_thermometer():
    try:
        ser = serial.Serial(arduino_string, 9600)

        while True:
            temp_str = ser.readline()

            print temp_str

            # Remove unecessary character from string leaving just temperature
            # temp = temp_str[0:5]
            #
            # print temp
            #
            # sys.stdout.write(temp)
            # temp_array.append(temp)
            #
            # print temp_array

            sys.stdout.flush()

    except serial.serialutil.SerialException as e:
        print e
        print ("Could not detect Arduino on port: " + arduino_string)

read_thermometer()
