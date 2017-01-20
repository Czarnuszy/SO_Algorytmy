import time
import random
import Print

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

def ReadData(queue):
    with open("Data/Data1.csv") as file:
        tab = [list(map(int, row.split(','))) for row in file]
    for i in range(len(tab[0])):
        ind = tab[0][i]
        arr = tab[1][i]
        bur = tab[2][i]
        process = Process(ind, arr, bur)
        queue.append(process)

def processRandomize(queue):
    n = int(input('Insert number of processes to simulate:'))
    for i in range(n):
        ind = random.randint(0, n)
        arr = random.randint(0, 15)
        bur = random.randint(1, 10)
        process = Process(ind, arr, bur)
        queue.append(process)
    return n
