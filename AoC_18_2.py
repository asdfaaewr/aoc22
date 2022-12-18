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
trapped_set = set()

for line in data:
    s.append(np.array(eval(line.strip()), dtype=int))

total = 0

def can_go_outside(cube, n):
    if tuple(cube) in trapped_set:
        return False
    pos = cube.copy()
    for i in range(n):
        d = directions[randint(0, 5)]
        while not np.any(np.all(pos + d == s, axis=1)):
            pos += d
            if is_outside(pos):
                return True        
    trapped_set.add(tuple(cube))
    return False
    

max_values = np.max(s, axis=0)
min_values = np.min(s, axis=0)

def is_outside(pos):
    if np.any(pos > max_values) or np.any(pos < min_values):
        return True
    else: 
        return False
        
counter = 0
for cube in s:
    for d in directions:
        counter += 1; print(counter)
        if not np.any(np.all(cube + d == s, axis=1)):
            if can_go_outside(cube+ d, 500):
                total += 1

print(total) 


