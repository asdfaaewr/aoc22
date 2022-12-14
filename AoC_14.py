file = r'C:\Users\asdf\AoC22\Inputs\Input_14.txt'

with open(file) as f:
    data = f.readlines()

def add_tiles(start, end):
    a, b = start
    c, d = end
    s.update({(x, y) for x in range(*((a, c + 1) if a < c else (c, a + 1))) 
                     for y in range(*((b, d + 1) if b < d else (d, b + 1)))})
    
s = set()
for line in data: 
    points = [eval(a) for a in line.split('->')]
    for i in range(len(points) - 1):
        add_tiles(points[i], points[i+1])

lowest_tile = max([p[1] for p in s])

for n in iter(range(1000000)):
    i, col = 0, 500
    while i <= lowest_tile:
        if (col, i+1) in s:
            if (col-1, i+1) in s:
                if (col+1, i+1) in s:
                    s.update({(col, i)})
                    break
                else: 
                    col += 1
            else:
                col -= 1
        else:
            i += 1
        

    if i == lowest_tile + 1:
        print(n)
        break


s = set()
for line in data: 
    points = [eval(a) for a in line.split('->')]
    #print(points)
    for i in range(len(points) - 1):
        add_tiles(points[i], points[i+1])
        
add_tiles((-500000, lowest_tile + 2), (500000, lowest_tile + 2))

for n in iter(range(10000000)):
    i, col = 0, 500
    while i <= lowest_tile + 2:
        if (col, i+1) in s:
            if (col-1, i+1) in s:
                if (col+1, i+1) in s:
                    s.update({(col, i)})
                    break
                else: 
                    col += 1
            else:
                col -= 1
        else:
            i += 1
        

    if (500, 0) in s:
        print(n+1)
        break