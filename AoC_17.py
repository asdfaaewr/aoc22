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
            old_lead = self.lead
            self.lead = self.lead[0] + 1, self.lead[1]

            if not stopped_set.isdisjoint({*self.get_elements()}):
                self.lead = old_lead

    def push_left(self):
        if self.lead[0] > 0:
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
        #print(self.get_elements(), direction)

        self.lead = self.lead[0] , self.lead[1] - 1

        if stopped_set.isdisjoint({*self.get_elements()}):
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

    def get_elements(self):
        return [(self.lead[0] + i,self.lead[1]) for i in range(4)]


class shape_1(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 5
        self.width = 3

    def get_elements(self):
        return [(self.lead[0] + i, self.lead[1]) for i in range(3)] + \
               [(self.lead[0] + 1, self.lead[1] + 1), (self.lead[0] + 1, self.lead[1] - 1)]


class shape_2(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 4
        self.width = 3

    def get_elements(self):
        return [(self.lead[0] + i, self.lead[1]) for i in range(3)] + \
               [(self.lead[0] + 2, self.lead[1] + 1), (self.lead[0] + 2, self.lead[1] + 2)]
       

class shape_3(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 7
        self.width = 1

    def get_elements(self):
        return [(self.lead[0], self.lead[1] - i) for i in range(4)]

class shape_4(rock):
    def __init__(self):
        self.lead = 2,  max_hight + 5
        self.width = 2

    def get_elements(self):
        return [(self.lead[0] + i, self.lead[1] - j ) for i in range(2) for j in range(2)]


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
for idx in range(2022):
    rock = create_rock(idx)
    while not rock.move_down(data[steps % s]):
        pass

print(max_hight)
print("Process finished --- %s seconds ---" % (time.time() - start_time))