import time
import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_16.txt'

start_time = time.time()

d = {}
with open(file) as f:
    data = f.readlines()

for idx, l in enumerate(data):
    line = l.replace(',','').split()
    d.update({line[1]: [int(line[4].split('=')[1].replace(';','')), line[9:], idx]})


is_closed = (1, ) * len(data) #np.zeros(60, dtype=int)
relevant_v = sum(tuple(1 - np.clip([d[k][0] for k in d.keys()],0,1)))
r = np.clip([d[k][0] for k in d.keys()],0,1) == 1

possibility_dict ={}

def open_valve(is_closed, idx):
    l = list(is_closed)
    for i in idx:
        l[i] = 0
    return tuple(l)


def max_flow_rate(minutes, valve_1, valve_2, is_closed):
    
    if minutes == 1:
        return 0
    
    if sum(is_closed) == relevant_v:
        return 0

    if valve_2 < valve_1:
        if (minutes, valve_2, valve_1, tuple(np.array(is_closed)[r])) in possibility_dict.keys():
            return possibility_dict[(minutes, valve_2, valve_1, tuple(np.array(is_closed)[r]))]
    else:
        if (minutes, valve_1, valve_2, tuple(np.array(is_closed)[r])) in possibility_dict.keys():
            return possibility_dict[(minutes, valve_1, valve_2, tuple(np.array(is_closed)[r]))]
    
    if valve_1 == valve_2:
        v_combs = [[d[valve_1][1][i], d[valve_1][1][v]] for v in range(len(d[valve_1][1])) for i in range(v)]

        if d[valve_1][0] == 0:
            q = max([max_flow_rate(minutes-1,*v, is_closed) for v in v_combs])
            possibility_dict.update({(minutes, valve_1, valve_2, tuple(np.array(is_closed)[r])): q})
            return q
        else:
            q = max(
                [is_closed[d[valve_1][2]] * (minutes - 1) * d[valve_1][0] + \
                max_flow_rate(minutes-1, valve_1, v, open_valve(is_closed, [d[valve_1][2]])) for v in d[valve_1][1]]
                +[max_flow_rate(minutes-1,*v, is_closed) for v in v_combs])        

            possibility_dict.update({(minutes, valve_1, valve_2, tuple(np.array(is_closed)[r])): q})

            return q
    else:
        v_combs = [[v_1, v_2] for v_1 in d[valve_1][1] for v_2 in d[valve_2][1]]
        q = max(
            [is_closed[d[valve_1][2]] * (minutes - 1) * d[valve_1][0] + \
             is_closed[d[valve_2][2]] * (minutes - 1) * d[valve_2][0] + \
             max_flow_rate(minutes-1, valve_1, valve_2, open_valve(is_closed, [d[valve_1][2], d[valve_2][2]]))]
            +[is_closed[d[valve_1][2]] * (minutes - 1) * d[valve_1][0] + \
            max_flow_rate(minutes-1, valve_1, v, open_valve(is_closed, [d[valve_1][2]])) for v in d[valve_2][1]]
            +[is_closed[d[valve_2][2]] * (minutes - 1) * d[valve_2][0] + \
            max_flow_rate(minutes-1, v, valve_2, open_valve(is_closed, [d[valve_2][2]])) for v in d[valve_1][1]]
            +[max_flow_rate(minutes-1,*v, is_closed) for v in v_combs])        

        if valve_2 < valve_1:
            possibility_dict.update({(minutes, valve_2, valve_1, tuple(np.array(is_closed)[r])): q})
        else: 
            possibility_dict.update({(minutes, valve_1, valve_2, tuple(np.array(is_closed)[r])): q})
        #possibility_dict.update({(minutes, valve_2, valve_1, tuple(np.array(is_closed)[r])): q})

        return q       


print(max_flow_rate(26, 'AA', 'AA', is_closed))
print("Process finished --- %s seconds ---" % (time.time() - start_time))

