import time
import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_16.txt'

start_time = time.time()

d = {}
with open(file) as f:
    data = f.readlines()

non_zero_list = []
g = -1
for idx, l in enumerate(data):
    line = l.replace(',','').split()
    d.update({line[1]: [int(line[4].split('=')[1].replace(';','')), line[9:], idx]})
    if int(line[4].split('=')[1].replace(';','')) > 0:
        g += 1
    non_zero_list.append(g)

r = np.clip([d[k][0] for k in d.keys()],0,1) == 1
is_closed = (True, ) * sum(r) #np.zeros(60, dtype=int)
relevant_v = sum(tuple(1 - np.clip([d[k][0] for k in d.keys()],0,1)))


possibility_dict ={}

def open_valve(is_closed, idx):
    l = list(is_closed)
    for i in idx:
        l[non_zero_list[i]] = False
    return tuple(l)


def max_flow_rate(minutes, valve_1, valve_2, is_closed):
    
    if minutes == 1:
        return 0
    
    if sum(is_closed) == 0:
        return 0

    if valve_2 < valve_1:
        if (minutes, valve_2, valve_1, is_closed) in possibility_dict.keys():
            return possibility_dict[(minutes, valve_2, valve_1, is_closed)]
    else:
        if (minutes, valve_1, valve_2, is_closed) in possibility_dict.keys():
            return possibility_dict[(minutes, valve_1, valve_2, is_closed)]
    
    if valve_1 == valve_2:
        v_combs = [[d[valve_1][1][i], d[valve_1][1][v]] for v in range(len(d[valve_1][1])) for i in range(v)]

        if d[valve_1][0] == 0:
            q = max([max_flow_rate(minutes-1,*v, is_closed) for v in v_combs])
            possibility_dict.update({(minutes, valve_1, valve_2, is_closed): q})
            return q
        else:
            q = max(
                [(r[d[valve_1][2]] and is_closed[non_zero_list[d[valve_1][2]]]) * (minutes - 1) * d[valve_1][0] + \
                max_flow_rate(minutes-1, valve_1, v, open_valve(is_closed, [d[valve_1][2]])) for v in d[valve_1][1]]
                +[max_flow_rate(minutes-1,*v, is_closed) for v in v_combs])        

            possibility_dict.update({(minutes, valve_1, valve_2, is_closed): q})

            return q
    else:
        v_combs = [[v_1, v_2] for v_1 in d[valve_1][1] for v_2 in d[valve_2][1]]
        q = max(
            [(r[d[valve_1][2]] and is_closed[non_zero_list[d[valve_1][2]]]) * (minutes - 1) * d[valve_1][0] + \
             (r[d[valve_2][2]] and is_closed[non_zero_list[d[valve_2][2]]]) * (minutes - 1) * d[valve_2][0] + \
             max_flow_rate(minutes-1, valve_1, valve_2, open_valve(is_closed, [d[valve_1][2], d[valve_2][2]]))]

            +[(r[d[valve_1][2]] and is_closed[non_zero_list[d[valve_1][2]]]) * (minutes - 1) * d[valve_1][0] + \
            max_flow_rate(minutes-1, valve_1, v, open_valve(is_closed, [d[valve_1][2]])) for v in d[valve_2][1]]

            +[(r[d[valve_2][2]] and is_closed[non_zero_list[d[valve_2][2]]]) * (minutes - 1) * d[valve_2][0] + \
            max_flow_rate(minutes-1, v, valve_2, open_valve(is_closed, [d[valve_2][2]])) for v in d[valve_1][1]]

            +[max_flow_rate(minutes-1,*v, is_closed) for v in v_combs])        

        if valve_2 < valve_1:
            possibility_dict.update({(minutes, valve_2, valve_1, is_closed): q})
        else: 
            possibility_dict.update({(minutes, valve_1, valve_2, is_closed): q})

        return q       


print(max_flow_rate(12, 'AA', 'AA', is_closed))
print("Process finished --- %s seconds ---" % (time.time() - start_time))

