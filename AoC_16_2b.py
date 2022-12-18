import time
import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_16_test.txt'

start_time = time.time()

d = {}
with open(file) as f:
    data = f.readlines()

#non_zero_list = np.zeros(len(data), dtype=int)
non_zero_list = {}
g = -1
for idx, l in enumerate(data):
    line = l.replace(',','').split()
    d.update({line[1]: [int(line[4].split('=')[1].replace(';','')), line[9:], idx]})
    if int(line[4].split('=')[1].replace(';','')) > 0:
        g += 1
    #non_zero_list[idx] = g
    non_zero_list.update({idx: g})

r = np.clip([d[k][0] for k in d.keys()],0,1) == 1
is_closed = (True, ) * sum(r) #np.zeros(60, dtype=int)
#relevant_v = sum(tuple(1 - np.clip([d[k][0] for k in d.keys()],0,1)))


possibility_dict ={}

def open_valve(is_closed, idx):
    l = list(is_closed)
    l[non_zero_list[idx]] = False
    return tuple(l)


def max_flow_rate(minutes, valve_1, valve_2, is_closed):

    if valve_2 < valve_1:
        if (minutes, valve_2, valve_1, is_closed) in possibility_dict.keys():
            return possibility_dict[(minutes, valve_2, valve_1, is_closed)]
    else:
        if (minutes, valve_1, valve_2, is_closed) in possibility_dict.keys():
            return possibility_dict[(minutes, valve_1, valve_2, is_closed)]
    
    d_1_1 = d[valve_1][1]
    d_1_2 = d[valve_1][2]
    d_2_1 = d[valve_2][1]
    d_2_2 = d[valve_2][2]
    open_1 = (r[d_1_2] and is_closed[non_zero_list[d_1_2]]) * (minutes - 1) * d[valve_1][0]
    open_2 = (r[d_2_2] and is_closed[non_zero_list[d_2_2]]) * (minutes - 1) * d[valve_2][0]
    

    if valve_1 == valve_2:
        if minutes == 2:
            return open_1

        v_combs = [[d_1_1[i], d_1_1[v]] for v in range(len(d_1_1)) for i in range(v+1)]

        temp = [max_flow_rate(minutes-1,*v, is_closed) for v in v_combs]

        if open_1 > 0:
            temp += [open_1 + max_flow_rate(minutes-1, valve_1, v, open_valve(is_closed, d_1_2)) for v in d_1_1]
   
        q = max(temp)
        possibility_dict.update({(minutes, valve_1, valve_2, is_closed): q})
        return q

    else:
        if minutes == 2:
            return open_2 + open_1

        v_combs = [[v_1, v_2] for v_1 in d_1_1 for v_2 in d_2_1]
        temp = [max_flow_rate(minutes-1,*v, is_closed) for v in v_combs]

        if open_1 > 0:
            temp += [open_1 + max_flow_rate(minutes-1, valve_1, v, open_valve(is_closed, d_1_2)) for v in d_2_1]
        
        if open_2 > 0:
            temp += [open_2 + max_flow_rate(minutes-1, v, valve_2, open_valve(is_closed, d_2_2)) for v in d_1_1]

        
        if open_1 * open_2 > 0 :
            temp += [open_1 + open_2 + max_flow_rate(minutes-1, valve_1, valve_2, open_valve(open_valve(is_closed, d_1_2), d_2_2))]
            
        q = max(temp)           

        if valve_2 < valve_1:
            possibility_dict.update({(minutes, valve_2, valve_1, is_closed): q})
        else: 
            possibility_dict.update({(minutes, valve_1, valve_2, is_closed): q})

        return q       


print(max_flow_rate(26, 'AA', 'AA', is_closed))
print("Process finished --- %s seconds ---" % (time.time() - start_time))

