#!/usr/bin/env python
import random
import time


def fcfsClosedbase():
    process_queue = []
    wtime = 0
    exetime = 0
    n = int(input('Enter the total no of processes: '))
    for i in range(n):
        process_queue.append([])  # append a list object to the list
        process_queue[i].append(input('Enter p_name: '))
        process_queue[i].append(int(input('Enter p_BurstTime: ')))
        process_queue[i].append(wtime)
        wtime += process_queue[i][1]
        exetime += process_queue[i][1]
        process_queue[i].append(exetime)
        print('')

    print('ProcessName:\tBurstTime:\tWait time:\tExecution time:')
    for i in range(n):
        print(process_queue[i][0], '\t\t\t\t', process_queue[i][1], '\t\t\t\t', process_queue[i][2], '\t\t\t\t', process_queue[i][3])

    print('Total waiting time: ', process_queue[n-1][2])
    print('Average waiting time: ', round((process_queue[n-1][2] / n), 2))
    print('Total execution time: ', exetime)
    print('Average execution time: ', round((exetime / n), 2))

    return 0


'''def fcfsOpenbase():
    proces_queue=[]
    wtime = 0
    exectime = 0
    n = 0

    return 0'''