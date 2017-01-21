import sys, FCFS, SJF, Priority


def menu():
    print("\nWhat algorithm you want to launch?")
    print('1. FCFS')
    print('2. SJF')
    print('3. Priority')
    print('4. End')
    z = int(input('(1-4):'))
    if z == 1:
        FCFS.start()
    elif z == 2:
        SJF.start()
    elif z == 3:
        Priority.start()
    elif z == 4:
        sys.exit(0)
    else:
        print("Wrong input")
        menu()
while(True):
    menu()

