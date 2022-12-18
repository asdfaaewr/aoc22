import AoC_16

import time
import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_16_test.txt'

start_time = time.time()

with open(file) as f:
    data = f.readlines()

valve_list = []
r = []
non_zero_list = []#{}
g = -1
for idx, l in enumerate(data):
    line = l.replace(',','').split()
    valve_list.append([line[1],  [int(line[4].split('=')[1].replace(';','')), line[9:], idx]])
    if int(line[4].split('=')[1].replace(';','')) > 0:
        g += 1
    non_zero_list.append(g)
    r.append(1 if valve_list[idx][1][0] > 0 else 0)
    #non_zero_list.update({idx: g * (valve_list[idx][1][0] > 0)})

#r = np.zeros(len(data), dtype=int)
q = np.array([i[0] for i in valve_list])

for idx, line in enumerate(valve_list):
    if valve_list[idx][0] == 'AA':
        index_AA = idx    
    valve_list[idx] = [valve_list[idx][1][0], [np.where(q==s)[0][0] for s in valve_list[idx][1][1]]]

nz_int = np.array(non_zero_list, dtype=int)
flow = np.array([v[0]for v in valve_list], dtype=int)
tunnel = np.array([v[1]for v in valve_list], dtype=list)
print(AoC_16.test(nz_int, flow, tunnel))