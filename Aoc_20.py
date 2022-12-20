import numpy as np
file = r'C:\Users\asdf\AoC22\Inputs\Input_20.txt'

with open(file) as f:
    data = f.readlines()

a_ = []
for line in data: 
    a_ += [int(line)]

#a_ = [1,2,-3,3,-2,0,4]
a = [i for i in range(len(a_))]
s = len(a)
t = a.copy()
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

    #print(len(t), idx, offset, c, a[n])
#print(t)

arr_out = np.array(a_)[np.array(t)]
idx_out = np.where(arr_out==0)[0][0]

print(sum(np.array([arr_out[(idx_out + x) % s] for x in [1000, 2000, 3000]])))





a = a_
#a = np.array([1,2,-3,3,-2,0,4])
arr_ind = np.array(range(len(a)))
s = len(a)

for n in range(len(a)):
    offset = c = abs(a_[n]) % (s-1) * np.sign(a_[n])
    idx = n

    if c + arr_ind[idx] >= s:
        offset = c - (s - 1)

    if c + arr_ind[idx] <= 0:
        offset = c + (s - 1)

    if offset > 0:
        arr_ind[(arr_ind > arr_ind[idx])*(arr_ind <= arr_ind[idx] + offset)] -= 1
    else:
        arr_ind[(arr_ind >= arr_ind[idx] + offset)*(arr_ind < arr_ind[idx] )] += 1

    arr_ind[idx] += offset

arr_out = -np.ones(len(a))
for i in range(len(a)): 
    arr_out[arr_ind[np.where(np.array(a)==a[i])[0][0]]] = a[i]

idx_out = np.where(arr_out==0)[0][0]

print(sum(np.array([arr_out[(idx_out + x) % s] for x in [1000, 2000, 3000]])))






    arr_ind[(arr_ind > idx)*(arr_ind <= idx + offset)] -= 1
    arr_ind[0] += offset




a = np.array([4,2,-3,3,-2,0,4])
arr_ind = np.array(range(len(a)))

idx = 4
offset = a[idx]

arr_ind[(arr_ind >= idx + offset)*(arr_ind < idx )] += 1
arr_ind[idx] += offset




