import numpy as np
from random import randint
file = r'C:\Users\asdf\AoC22\Inputs\Input_18.txt'


directions = [np.array([1,0,0], dtype=int),
              np.array([-1,0,0], dtype=int),
              np.array([0,1,0], dtype=int),
              np.array([0,-1,0], dtype=int),
              np.array([0,0,1], dtype=int),
              np.array([0,0,-1], dtype=int)]


with open(file) as f:
    data = f.readlines()
 
s = []
for line in data:
    s.append(np.array(eval(line.strip()), dtype=int))

total = 0
for cube in s:
    for d in directions:
        if not np.any(np.all(cube + d == s, axis=1)):
             total += 1

print(total) 


