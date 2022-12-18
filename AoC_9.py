direction_dict = {'U' : (1, 0), 'D' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}

class Rope:
    def __init__(self, start_position=(0,0)):
        self.head = Knot(start_position)
        self.tail = Knot(start_position)

    @property
    def touching(self):
        return ((-2 < self.head.position[0] - self.tail.position[0] < 2) and (-2 < self.head.position[1] - self.tail.position[1] < 2))
    
    def move_knots(self, direction, steps):
        for _ in range(int(steps)):
            self.head.move(direction)
            if not self.touching:
                self.tail.position = self.head.history[-2]
                self.tail.history.append(self.tail.position)
    

class Knot:
    def __init__(self, start_position):
        self.position = start_position
        self.history = [start_position]

    @property
    def unique_positions(self):
        return len(set(self.history))

        
    def move(self, direction):
        move = direction_dict[direction]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.history.append(self.position)


if __name__ == "__main__":

    file = r'C:\Users\asdf\AoC22\Inputs\Input_9.txt'

    with open(file) as f:
        data = f.readlines()
    
    rope = Rope()
    
    for line in data:
        rope.move_knots(*line.split())

    print(rope.tail.unique_positions)

