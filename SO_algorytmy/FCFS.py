#!/usr/bin/env python

import time
import Print as P
from ProcessClass import ReadData, processRandomize



def start():
    print("\n--------------------------------")
    print("--------------FCFS--------------")
    print("--------------------------------")
    print('1. Generate random processes.')
    print('2. Read data from file.')
    choice = int(input("(1-2): "))
    process_queue = []
    if choice == 1:
        processRandomize(process_queue)
    elif choice == 2:
        ReadData(process_queue)
    else:
        print("Wrong input")
        start()
    print("\nData input before sort:")
    P.print_process_report(process_queue)
    process_queue.sort(key=lambda process_queue: process_queue.arrival)
    print("\nData input after sort:")
    P.print_process_report(process_queue)
    start_time = 0
    average_wait = 0
    wait_time = 0
    m = len(process_queue)
    for i in range(m):
        if process_queue[i].arrival > start_time:
            start_time = process_queue[i].arrival
            wait_time = 0
        else:
            wait_time = start_time - process_queue[i].arrival
        average_wait += wait_time
        process_queue[i].symulate(wait_time)
        start_time += process_queue[i].burst
    print('S \t', end='')
    for i in range(1, 30):
        if i < 10:
            print('| '+str(i)+" ", end='')
        else:
            print('| ' + str(i), end='')
    print("\nTotal wait time= ", average_wait)
    print("Average process wait time: ", float(average_wait/m))

