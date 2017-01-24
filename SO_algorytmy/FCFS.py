#!/usr/bin/env python

from ProcessClass import ReadData
from time import sleep

def printData(queue):
    file = open("Reports/FCFS.txt", 'w')
    print('\n\nProcessName\tArrivalTime\tBurstTime\tWaitTime')
    file.write('\nProcessName\tArrivalTime\tBurstTime\tWaitTime')
    for i in range(len(queue)):
        file.write('\n'+ str(queue[i].index)
                   + "\t\t\t" + str(queue[i].arrival)
                   + "\t\t\t" + str(queue[i].burst)
                   + "\t\t\t" +  str(queue[i].w_time))
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
    print(process_queue[0].s_time)
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
    file = open("Reports/FCFS.txt", 'a')
    file.write('\nTotal wait time= '+str(average_wait))
    print("\nTotal wait time= ", average_wait)
    file.write("\n Average process wait time: "+str(float(average_wait/m)))
    print("Average process wait time: ", float(average_wait / m))
    file.close()

def raport_generator(queue):
    print('Do you want to generate report?')
    x = input("y/n: ")
    if x == "y":
        file = open("Reports/FCFS.txt", "a")
        file.write("printData(queue)")
        file.close()

    elif x == "n":
        pass
    else:
        print("Wrong input")
        raport_generator(queue)

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
    calculate(process_queue)


