direction_dict = {'U' : (1, 0), 'D' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}

class Rope:
    def __init__(self, start_position=(0,0), num_knots=2):
        self.knot_list = [Knot(start_position)]
        for _ in range(num_knots-1):
            self.knot_list.append(Knot(start_position, followed_by=self.knot_list[-1]))
    
    def move_knots(self, direction, steps):
        for _ in range(int(steps)):
            self.knot_list[-1].move(direction)
            #print([knot.position for knot in self.knot_list])

class Knot:
    def __init__(self, start_position, followed_by=None):
        self.position = start_position
        self.history = [start_position]
        self.followed_by = followed_by

    @property
    def unique_positions(self):
        return len(set(self.history))

    def touching(self, knot_2):
        return ((-2 < self.position[0] - knot_2.position[0] < 2) and (-2 < self.position[1] - knot_2.position[1] < 2))

    
    def leader_diagonal(self, leader):
        leader_direction = (leader.position[0] - leader.history[-2][0], leader.position[1] - leader.history[-2][1])
        if leader_direction in {(1, 1), (-1, 1), (1, -1), (-1, -1)}:
            
            relative_position = (leader.position[0] - self.position[0], leader.position[1] - self.position[1])
            if relative_position[0]==0 or relative_position[1]==0:
                return (True, (relative_position[0] / 2, relative_position[1] / 2))
            else:
                return (True, leader_direction)
        else:
            return (False, (0,0))
    
    def move(self, direction):
        move = direction_dict[direction]
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.history.append(self.position)
        if self.followed_by is not None and not self.touching(self.followed_by):
            self.followed_by.follow(self)
    
    def follow(self, leader):
        if self.leader_diagonal(leader)[0]:
            self.position = (self.position[0] + self.leader_diagonal(leader)[1][0], self.position[1] + self.leader_diagonal(leader)[1][1])
        else:        
            self.position = leader.history[-2]
            
        self.history.append(self.position)
        if self.followed_by is not None and not self.touching(self.followed_by):
            self.followed_by.follow(self)
             


if __name__ == "__main__":

    file = r'C:\Users\asdf\AoC22\Inputs\Input_9.txt'

    with open(file) as f:
        data = f.readlines()
    
    rope = Rope(num_knots=10)
    
    for line in data:
        #print([knot.position for knot in rope.knot_list] + ['----------'])
        rope.move_knots(*line.split())
        
    print(rope.knot_list[-2].unique_positions)
    print(rope.knot_list[0].unique_positions)

