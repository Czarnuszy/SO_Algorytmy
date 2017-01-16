#!/usr/bin/env python
import Print, time, random

class Process:
    def __init__(self, index, arrival, burst):
        self.index = index
        self.arrival = arrival
        self.burst = burst

    def symulate(self, s_time,w_time):
        print("\nProcess index: ", self.index)
        print('Arrival time: ', self.arrival)
        print('Process start time: ', s_time)
        print('Process wait time: ', w_time)
        time.sleep(1)
        Print.process_print(self.burst)


def processInput(n, queue):
    n = int(input('Insert number of processes to simulate:'))
    for i in range(n):
        ind = input("\nInsert process index: ")
        arr = int(input('Insert process arrival time: '))
        bur = int(input('Insert process burst time: '))
        process = Process(ind, arr, bur)
        queue.append(process)
    return n


def processRandomize(queue):
    n = int(input('Insert number of processes to simulate:'))
    for i in range(n):
        ind = random.randint(0, n)
        arr = random.randint(0, 15)
        bur = random.randint(1, 10)
        process = Process(ind, arr, bur)
        queue.append(process)
    return n



def start():
    print("\n")
    print('1. Generate random processes.')
    print('2. Insert processes data manually.')
    choice = int(input("(1-2): "))
    process_queue = []
    if choice == 1:
        processRandomize(process_queue)
    elif choice == 2:
        processInput(process_queue)
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

