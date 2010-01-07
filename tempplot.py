#!/usr/bin/python
import math
from pylab import *

LOG_FILE="/home/albin/temperatures.log"

temp_list = []
hum_list = []
time_list = []

f = open(LOG_FILE, 'r')

first_line = False
begin_time=0

for line in f:
    parsed_line = line.partition(":")
    timestamp = float(parsed_line[0])
    temp = float(parsed_line[2].partition(",")[0])
    hum = float(parsed_line[2].partition(",")[2])
    if first_line:
        begin_time = timestamp
    temp_list.append(temp)
    hum_list.append(hum)
    time_list.append(timestamp-begin_time)
f.close()

def plot_temp(time_list, temp_list):
    xlabel("time (s)")
    ylabel("temperature (c)")
    plot(time_list, temp_list, 'b')
    grid(True)
    show()
def plot_hum(time_list, hum_list):
    xlabel("time (s)")
    ylabel("relative humidity (%)")
    plot(time_list, hum_list, 'b')
    grid(True)
    show()

plot_temp(time_list, temp_list)



