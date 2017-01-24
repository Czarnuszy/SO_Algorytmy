#!/usr/bin/env python
from ProcessClass import ReadData
from time import sleep


def printData(queue):
    file = open("Reports/SJF.txt", 'w')
    print('\n\nProcessName\tArrivalTime\tBurstTime\tWaitTime')
    file.write('\nProcessName\tArrivalTime\tBurstTime\tWaitTime')
    for i in range(len(queue)):
        file.write('\n'+ str(queue[i].index)
                   + "\t\t\t" + str(queue[i].arrival)
                   + "\t\t\t" + str(queue[i].burst)
                   + "\t\t\t" + str(queue[i].w_time))
        print('\t', queue[i].index,
              '\t\t', queue[i].arrival,
              '\t\t', queue[i].burst,
              "\t\t\t", str(queue[i].w_time))
    file.close()

def printGrid(queue2):
    for i in range(len(queue2)):
        queue2[i].print()
        sleep(1)
    print('S \t', end='')
    m = len(queue2)
    x = queue2[m - 1].e_time
    for i in range(1, x):
        if i < 10:
            print('| ' + str(i) + " ", end='')
        else:
            print('| ' + str(i), end='')
    print("\n - -> Wait Time \n # -> Burst Time")

def calculate(process_queue):
    start_time = 0
    average_wait = 0
    m = len(process_queue)
    for i in range(0, m):
        if process_queue[i].arrival > start_time:
            start_time = process_queue[i].arrival
            process_queue[i].w_time = 0
        else:
            process_queue[i].w_time = start_time - process_queue[i].arrival
        average_wait += process_queue[i].w_time
        process_queue[i].e_time = start_time + process_queue[i].burst
        start_time += process_queue[i].burst
    printData(process_queue)
    printGrid(process_queue)
    file = open("Reports/SJF.txt", 'a')
    file.write('\nTotal wait time= ' + str(average_wait))
    print("\nTotal wait time= ", average_wait)
    file.write("\n Average process wait time: " + str(float(average_wait / m)))
    print("Average process wait time: ", float(average_wait / m))
    file.close()


def start():
    print("\n-------------------------------")
    print("--------------SJF--------------")
    print("-------------------------------")
    process_queue = []
    queue2 = []
    ReadData(process_queue)
    print("\nData input before sort:")
    printData(process_queue)
    process_queue.sort(key=lambda p_queue: p_queue.arrival)
    queue2.append(process_queue[0])
    for i in range(1, len(process_queue)):
        temp = []
        for j in range(1, len(process_queue)):
            if process_queue[j].arrival <= (queue2[i-1].burst+queue2[i-1].arrival):
                temp.append(process_queue[j])
        temp.sort(key=lambda p_queue: p_queue.burst)
        queue2.append(temp[i-1])
    print("\nData input after sort:")
    calculate(queue2)
