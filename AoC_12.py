import numpy as np; import pandas as pd
file = r'C:\Users\asdf\AoC22\Inputs\Input_12.txt'
cols = len(pd.read_fwf(file).values[0][0])
data = pd.read_fwf(file, widths = [1] * cols, header=None).values

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = tuple([int(i) for i in (np.where(data=='S'))])
goal = tuple([int(i) for i in (np.where(data=='E'))])
data[start] = 'a'; data[goal] = 'z'

steps = -np.ones(data.shape, dtype=int)
steps[start] = 0

goal_found = False
current_list = [start]
n_x, n_y = data.shape

def valid_step(x, y, new_x, new_y):
    return 0 <= new_x < n_x and 0 <= new_y < n_y and steps[new_x, new_y] == -1 \
        and ord(data[new_x, new_y]) - ord(data[x, y]) <= 1

while not goal_found:
    new_list = []
    for idx in current_list:
        x, y = idx
        for d1, d2 in directions:
            new_x, new_y = x + d1, y + d2
            if valid_step(x, y, new_x, new_y):
                steps[new_x, new_y] = steps[x, y] + 1
                if (new_x, new_y) == goal:
                    goal_found = True
                new_list.append((new_x, new_y))

    current_list = new_list

print(steps[goal])


## Part 2

steps = -np.ones(data.shape, dtype=int)
steps[goal] = 0

goal_found = False
current_list = [goal]
n_x, n_y = data.shape

def valid_step_2(x, y, new_x, new_y):
    return 0 <= new_x < n_x and 0 <= new_y < n_y and steps[new_x, new_y] == -1 and ord(data[new_x, new_y]) - ord(data[x, y]) >= -1

while not goal_found:
    new_list = []
    for idx in current_list:
        x, y = idx
        for d1, d2 in directions:
            new_x, new_y = x + d1, y + d2
            if valid_step_2(x, y, new_x, new_y):
                steps[new_x, new_y] = steps[x, y] + 1
                if data[new_x, new_y] == 'a':
                    print(steps[x, y] + 1)
                    exit(0)
                new_list.append((new_x, new_y))

    current_list = new_list
