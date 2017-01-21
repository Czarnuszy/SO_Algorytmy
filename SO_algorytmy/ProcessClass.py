import time
import random
import Print


class Process:
    def __init__(self, index, arrival, burst):
        self.index = index
        self.arrival = arrival
        self.burst = burst

    def symulate(self, w_time):
       Print.process_grid_print(self.index, self.arrival, self.burst, w_time)

def ReadData(queue):
    with open("Data/Data1.csv") as file:
        tab = [list(map(int, row.split(','))) for row in file]
    for i in range(len(tab[0])):
        ind = ("P"+str(tab[0][i]))
        arr = int(tab[1][i])
        bur = int(tab[2][i])
        process = Process(ind, arr, bur)
        queue.append(process)

def processRandomize(queue):
    n = int(input('Insert number of processes to simulate:'))
    for i in range(n):
        ind = ("P"+str(i))
        arr = random.randint(0, 15)
        bur = random.randint(1, 10)
        process = Process(ind, arr, bur)
        queue.append(process)
    return n
