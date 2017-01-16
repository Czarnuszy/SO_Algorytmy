import sys,FCFS,SJF,RoundRobin,Priority
#FCFS.fcfsClosedbase()
#FCFS.fcfsOpenbase()

def menu():
    print("\nWhat algorithm you want to launch?")
    print('1. FCFS')
    print('2. SJF')
    print('3. Round Robin')
    print('4. End')
    z = int(input('(1-4):'))
    if z == 1:
        FCFS.start()
menu()