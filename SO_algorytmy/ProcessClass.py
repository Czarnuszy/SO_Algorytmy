class Process:
    def __init__(self, index, arrival, burst, priority, wait_time=0,
                 s_time=0, end_time=0):
        self.index = index
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.w_time = wait_time
        self.s_time = s_time
        self.e_time = end_time


    def print(self):
        print(self.index + "\t" + '|   ' * (self.arrival-1) + "| - "
              * self.w_time + "| # " * self.burst)

def ReadData(queue):
    with open("Data/Data1.csv") as file:
        tab = [list(map(int, row.split(','))) for row in file]
    for i in range(len(tab[0])):
        ind = ("P"+str(tab[0][i]))
        arr = int(tab[1][i])
        bur = int(tab[2][i])
        pri = int(tab[3][i])
        process = Process(ind, arr, bur, pri)
        queue.append(process)
