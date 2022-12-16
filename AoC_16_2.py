import time
import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_16.txt'

start_time = time.time()

with open(file) as f:
    data = f.readlines()

valve_list = []
non_zero_list = []
g = -1
for idx, l in enumerate(data):
    line = l.replace(',','').split()
    valve_list.append([line[1],  [int(line[4].split('=')[1].replace(';','')), line[9:], idx]])
    if int(line[4].split('=')[1].replace(';','')) > 0:
        g += 1
    non_zero_list.append(g)

q = np.array([i[0] for i in valve_list])

for idx, line in enumerate(valve_list):
    if valve_list[idx][0] == 'AA':
        index_AA = idx    
    valve_list[idx] = [valve_list[idx][1][0], [np.where(q==s)[0][0] for s in valve_list[idx][1][1]]]

is_closed = (True, ) * 15

possibility_dict = {}

def open_valve(is_closed, idx):
    l = list(is_closed)
    l[non_zero_list[idx]] = False
    return tuple(l)


def max_flow_rate(minutes, valve_1_idx, valve_2_idx, is_closed):

    if minutes == 2:
        if valve_1_idx == valve_2_idx:
            flow_1 = valve_list[valve_1_idx][0]
            return (flow_1 and is_closed[non_zero_list[valve_1_idx]]) * (minutes - 1) * valve_list[valve_1_idx][0]
        else:    
            flow_1 = valve_list[valve_1_idx][0]
            flow_2 = valve_list[valve_2_idx][0]
            nz_1 = non_zero_list[valve_1_idx]
            nz_2 = non_zero_list[valve_2_idx]
            return (flow_1 and is_closed[non_zero_list[valve_1_idx]]) * (minutes - 1) * flow_1 + \
                 (flow_2 and is_closed[non_zero_list[valve_2_idx]]) * (minutes - 1) * flow_2
    
    if valve_1_idx < valve_2_idx:
        if (minutes, valve_1_idx, valve_2_idx, is_closed) in possibility_dict:
            return possibility_dict[(minutes, valve_1_idx, valve_2_idx, is_closed)]
    else:
        if (minutes, valve_2_idx, valve_1_idx, is_closed) in possibility_dict:
            return possibility_dict[(minutes, valve_2_idx, valve_1_idx, is_closed)]
    
    d_1_1 = valve_list[valve_1_idx][1]
    flow_1 = valve_list[valve_1_idx][0]
    open_1 = (flow_1 and is_closed[non_zero_list[valve_1_idx]]) * (minutes - 1) * flow_1

    if valve_1_idx == valve_2_idx:

        temp = [max_flow_rate(minutes-1, d_1_1[j], d_1_1[k], is_closed) for j in range(len(d_1_1)) for k in range(j+1)]

        if open_1 > 0:
            temp += [open_1 + max_flow_rate(minutes-1, valve_1_idx, v, open_valve(is_closed, valve_1_idx)) for v in d_1_1]
   
        q = max(temp)
        possibility_dict.update({(minutes, valve_1_idx, valve_2_idx, is_closed): q})
        return q

    else:
        d_2_1 = valve_list[valve_2_idx][1]
        flow_2 = valve_list[valve_2_idx][0]
        open_2 = (flow_2 and is_closed[non_zero_list[valve_2_idx]]) * (minutes - 1) * flow_2

        temp = [max_flow_rate(minutes-1, v_1, v_2, is_closed) for v_1 in d_1_1 for v_2 in d_2_1]

        if open_1 > 0:
            temp += [open_1 + max_flow_rate(minutes-1, valve_1_idx, v, open_valve(is_closed, valve_1_idx)) for v in d_2_1]
        
        if open_2 > 0:
            temp += [open_2 + max_flow_rate(minutes-1, v, valve_2_idx, open_valve(is_closed, valve_2_idx)) for v in d_1_1]

        
        if open_1 * open_2 > 0 :
            temp += [open_1 + open_2 + max_flow_rate(minutes-1, valve_1_idx, valve_2_idx, open_valve(open_valve(is_closed, valve_1_idx), valve_2_idx))]
            
        q = max(temp)           

        if valve_1_idx < valve_2_idx:
            possibility_dict.update({(minutes, valve_1_idx, valve_2_idx, is_closed): q})
        else: 
            possibility_dict.update({(minutes, valve_2_idx, valve_1_idx, is_closed): q})

        return q       


print(max_flow_rate(26, index_AA, index_AA, is_closed))
print("Process finished --- %s seconds ---" % (time.time() - start_time))

