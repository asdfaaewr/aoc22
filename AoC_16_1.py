import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_16.txt'


d = {}
with open(file) as f:
    data = f.readlines()

for idx, l in enumerate(data):
    line = l.replace(',','').split()
    d.update({line[1]: [int(line[4].split('=')[1].replace(';','')), line[9:], idx]})


is_closed = (1, ) * len(data) #np.zeros(60, dtype=int)
relevant_v = sum(tuple(1 - np.clip([d[k][0] for k in d.keys()],0,1)))

possibility_dict ={}

def open_valve(is_closed, idx):
    l = list(is_closed)
    l[idx] = 0
    return tuple(l)


def max_flow_rate(minutes, valve, is_closed):
    
    if minutes == 1:
        return 0
    
    if sum(is_closed) == relevant_v:
        return 0

    if (minutes, valve, is_closed) in possibility_dict.keys():
        return possibility_dict[(minutes, valve, is_closed)]

    if d[valve][0] == 0:
        q = max([max_flow_rate(minutes-1, v, is_closed) for v in d[valve][1]])
        possibility_dict.update({(minutes, valve, is_closed): q})
        return q
    else:

        a = [is_closed[d[valve][2]] * (minutes - 1) * d[valve][0] \
        + max_flow_rate(minutes-1, valve, open_valve(is_closed, d[valve][2]))]

        q = max(a + [max_flow_rate(minutes-1, v, is_closed) for v in d[valve][1]])
        possibility_dict.update({(minutes, valve, is_closed): q})
        return q


print(max_flow_rate(30, 'AA', is_closed))
#print(possibility_dict)
