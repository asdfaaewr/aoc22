import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_20.txt'

with open(file) as f:
    data = f.readlines() 

a_ = []
for line in data: 
    a_ += [int(line)] 

a_ = np.array(a_, np.longlong) * 811589153
a = [i for i in range(len(a_))]
s = len(a)
t = a.copy()
for _ in range(10):
    for n in range(s):
        idx = np.where(np.array(t, int)==n)[0][0]
        c = offset = abs(a_[n]) % (s-1) * np.sign(a_[n])

        if c + idx >= s:
            offset = c - (s - 1)

        if c + idx <= 0:
            offset = c + (s - 1)

        if offset > 0:
            t = t[0:idx] + t[idx + 1: idx + 1 + offset] + [t[idx]] + t[idx + 1 + offset:]
        else:
            t = t[0:idx + offset] + [t[idx]] + t[idx + offset: idx] + t[idx + 1:]


arr_out = np.array(a_)[np.array(t)]
idx_out = np.where(arr_out==0)[0][0]

print(sum(np.array([arr_out[(idx_out + x) % s] for x in [1000, 2000, 3000]])))
