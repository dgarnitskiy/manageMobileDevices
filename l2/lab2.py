#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import numpy as np

time_arr = []
bytes_arr = []
sum_bytes = 0

text = os.popen('nfdump -o "fmt:%te|%sa|%da|%byt" -r '+'nfcapd.202002251200').readlines()
time = '0'
bytes = 0

def graph(x, y, x_label="", y_label=""):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, linewidth = 1.2, color = 'black')

    ax.set_facecolor('red')
    ax.set_title('graph')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig('graph', fmt='png')

for line in text:
	if ('192.168.250.59' in line):
		s = line[(line.rfind('|')+1):]
		b = 0
		if ('M' in s):
			b = int(float(s[:-3])*1000000)
		else:
			b = int(s)
		if (time != line[:(line.find('|'))]):
			time_arr.append(line[:(line.find('|'))])
			bytes_arr.append(bytes)
			bytes = 0
			time = line[:(line.find('|'))]
		else:
			bytes += b
		sum_bytes += b
k0 = 0.5
k1 = 1		
sum = 0	
if (sum_bytes/1000000 < 500):
	sum_bytes/= 1000
else:
	sum_bytes/= 1000000
if (sum_bytes > 500):
	sum = k0*500+k1*(sum_bytes-500)
else:
	sum = k0*sum_bytes

graph(time_arr, bytes_arr, "time", "bytes")
file = open('output.txt', 'w')
file.write('Total sum: ' + str(sum) + ' rub')
file.close()
