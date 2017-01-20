#!/usr/bin/env python

import time
from ProcessClass import ReadData, processRandomize



def start():
    print("\n")
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
    process_queue.sort(key=lambda process_queue: process_queue.arrival)
    start_time = 0
    average_wait = 0
    wait_time = 0
    m = len(process_queue)
    for i in range(m):
        time.sleep(1)
        if process_queue[i].arrival > start_time:
            start_time = process_queue[i].arrival
            wait_time = 0
        else:
            wait_time = start_time - process_queue[i].arrival
        average_wait += wait_time
        process_queue[i].symulate(start_time, wait_time)
        time.sleep(1)
        start_time += process_queue[i].burst

    print("Total wait time= ", average_wait)
    print("Average process wait time: ", float(average_wait/m))

