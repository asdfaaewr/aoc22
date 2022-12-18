import time
import numpy as np 
start_time = time.time()

file = r'C:\Users\asdf\AoC22\Inputs\Input_17.txt'

with open(file) as f:
    data = f.read()

global stopped_set, max_hight
stopped_set = {(0+i, 0) for i in range(7)}
max_hight = 0

class rock:
    def __init__(self):
        pass

    def push_right(self):
        if self.lead[0] + self.width < 7:
            if self.lead[1] - self.depths > max_hight:
                self.lead = self.lead[0] + 1, self.lead[1]
            else:    
                old_lead = self.lead
                self.lead = self.lead[0] + 1, self.lead[1]

                if not stopped_set.isdisjoint({*self.get_elements()}):
                    self.lead = old_lead

    def push_left(self):
        if self.lead[0] > 0:
            if self.lead[1] - self.depths > max_hight:
                self.lead = self.lead[0] - 1, self.lead[1]
            else:
                old_lead = self.lead
                self.lead = self.lead[0] - 1, self.lead[1]

                if not stopped_set.isdisjoint({*self.get_elements()}):
                    self.lead = old_lead

    def move_down(self, direction):
        global max_hight, steps
        
        if direction == '>':
            self.push_right()
        else:
            self.push_left()
        
        steps += 1      

        current_elements = {*self.get_elements()}

        self.lead = self.lead[0] , self.lead[1] - 1

        if self.lead[1] - self.depths > max_hight or stopped_set.isdisjoint({*self.get_elements()}):
            return False
        else:
            for element in current_elements:
                stopped_set.add(element)
                max_hight = element[1] if element[1] > max_hight else max_hight
            return True


class shape_0(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 4
        self.width = 4
        self.depths = 0

    def get_elements(self):
        return [(self.lead[0], self.lead[1]), (self.lead[0]+1, self.lead[1]), (self.lead[0]+2, self.lead[1]), (self.lead[0]+3, self.lead[1])]

class shape_1(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 5
        self.width = 3
        self.depths = 1

    def get_elements(self):
        return [(self.lead[0], self.lead[1]), (self.lead[0] + 1, self.lead[1]), (self.lead[0] + 2, self.lead[1]), \
               (self.lead[0] + 1, self.lead[1] + 1), (self.lead[0] + 1, self.lead[1] - 1)]


class shape_2(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 4
        self.width = 3
        self.depths = 0

    def get_elements(self):
        return [(self.lead[0], self.lead[1]), (self.lead[0] + 1, self.lead[1]), (self.lead[0] + 2, self.lead[1]), \
               (self.lead[0] + 2, self.lead[1] + 1), (self.lead[0] + 2, self.lead[1] + 2)]
       

class shape_3(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 7
        self.width = 1
        self.depths = 3

    def get_elements(self):
        return [(self.lead[0], self.lead[1]), (self.lead[0], self.lead[1] - 1), (self.lead[0], self.lead[1] - 2), (self.lead[0], self.lead[1] - 3)]

class shape_4(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 5
        self.width = 2
        self.depths = 1

    def get_elements(self):
        return [(self.lead[0], self.lead[1]), (self.lead[0] + 1, self.lead[1]), (self.lead[0], self.lead[1] - 1), (self.lead[0] + 1, self.lead[1] - 1)]


def create_rock(idx):
    if idx % 5 == 0:
        rock = shape_0()
    elif idx % 5 == 1:
         rock = shape_1() 
    elif idx % 5 == 2:
         rock = shape_2() 
    elif idx % 5 == 3:
         rock = shape_3() 
    elif idx % 5 == 4:
         rock = shape_4() 

    return rock

s = len(data)
steps = 0
n = 300 * 1000000
arr = np.zeros(n, dtype=np.ulonglong)


for idx in iter(range(n)):
    rock = create_rock(idx)
    while not rock.move_down(data[steps % s]):
        pass
    
    if idx > 0 and idx % 1000000 == 0:
        print(idx, max_hight)
        stopped_set = set([item for item in stopped_set if item[1] > max_hight - 1000])

    arr[idx] = max_hight
    del rock

print("Process finished --- %s seconds ---" % (time.time() - start_time))


min_loop = len(data) if (len(data) % 5 == 0) else len(data) * 5
d_out, i_out, e_out = 0, 0, 0
for k in range(1, int(n / (min_loop * 6))):
    d = min_loop * k
    for i in iter(range(1, d)): #len(arr) - 5 * d - 1)):
        dis = arr[i+d] - arr[i]
        if dis == arr[i+2*d] - arr[i+d]  and dis == arr[i+3*d] - arr[i+2*d] and  \
           dis == arr[i+4*d] - arr[i+3*d] and dis == arr[i+5*d] - arr[i+4*d] and \
           dis == arr[i+6*d] - arr[i+5*d]:

            d_out = d 
            i_out = i
            e_out = arr[i+d] - arr[i]
            break
    
    if d_out:
        break

if d_out:
    print((1000000000000 // d_out) * e_out + arr[1000000000000 % d_out - 1])

print("Process finished --- %s seconds ---" % (time.time() - start_time))