#!/usr/bin/env python

from ProcessClass import ReadData

def printData(queue):
    print('\n\nProcessName\tArrivalTime\tBurstTime')
    for i in range(len(queue)):
        print('\t', queue[i].index, '\t\t', queue[i].arrival, '\t\t', queue[i].burst)


def calculate(process_queue):
    start_time = 0
    average_wait = 0
    m = len(process_queue)
    print(process_queue[0].s_time)
    for i in range(0, m):
        if process_queue[i].arrival > start_time:
            start_time = process_queue[i].arrival
            process_queue[i].w_time = 0
        else:
            process_queue[i].w_time = start_time - process_queue[i].arrival
        average_wait += process_queue[i].w_time
        process_queue[i].print()
        process_queue[i].e_time = start_time + process_queue[i].burst
        start_time += process_queue[i].burst

    print('S \t', end='')
    x = process_queue[m - 1].e_time
    y = process_queue[0].arrival
    for i in range(y, x):
        if i < 10:
            print('| ' + str(i) + " ", end='')
        else:
            print('| ' + str(i), end='')
    print("\nTotal wait time= ", average_wait)
    print("Average process wait time: ", float(average_wait / m))

def start():
    print("\n--------------------------------")
    print("--------------FCFS--------------")
    print("--------------------------------")
    process_queue = []
    ReadData(process_queue)
    print("\nData input before sort:")
    printData(process_queue)
    process_queue.sort(key=lambda process_queue: process_queue.arrival)
    print("\nData input after sort:")
    printData(process_queue)
    calculate(process_queue)


