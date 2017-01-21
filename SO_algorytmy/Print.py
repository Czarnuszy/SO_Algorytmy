

def process_grid_print(p_name, arrival, bust, w_time):
    print(p_name+"\t"+'|   '*(arrival)+"| # "*w_time+"| * "*bust)

def print_process_report(queue):
    print('\n\nProcessName\tArrivalTime\tBurstTime')
    for i in range(len(queue)):
        print('\t', queue[i].index, '\t\t', queue[i].arrival, '\t\t', queue[i].burst)

