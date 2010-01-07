#/usr/bin/python

LOG_FILE="/home/albin/temperatures.log"
SERIAL_DEVICE="/dev/ttyUSB2"
BAUD_RATE=115200

import serial, datetime, time
ser = serial.Serial(SERIAL_DEVICE, BAUD_RATE)

print "beginning logging of temperatures..."
while True:
    indata = ser.readline().partition(",")
    #format is temp,hum\n from arduino
    try: 
        temp = float(indata[0])
        hum = float(indata[2])
        
        if(int(temp) == -40 or hum < 0):
            # invalid values, error occured
            # if temp == -40 or hum is negative, throw an exception
            raise ValueError                    
    except ValueError:
        pass
    else:
        timestamp = time.mktime(datetime.datetime.now().timetuple())

        f = open(LOG_FILE,"a")
        f.write("%f: %f,%f\n" % (timestamp, temp, hum))
        f.close()
        #print "%f: %f,%f\n" % (timestamp, temp, hum)


