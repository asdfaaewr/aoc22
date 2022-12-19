file = r'C:\Users\asdf\AoC22\Inputs\Input_19.txt'

with open(file) as f:
    data = f.readlines()

pol_list = []
for line in data:
    l = line.split('costs')
    pol_list.append([(-int(l[1].split(' ')[1]), 0, 0, 0), (-int(l[2].split(' ')[1]), 0, 0, 0),
                     (-int(l[3].split(' ')[1]), -int(l[3].split(' ')[4]), 0, 0), (-int(l[4].split(' ')[1]), 0, -int(l[4].split(' ')[4]), 0)])

#pol_list = pol_list[:3]

#print(pol_list)

def t_add(t_1, t_2):
    return tuple(map(lambda x, y: x + y, t_1, t_2))

robots = (1, 0, 0, 0)
mats = (0, 0, 0, 0)
rob_pol =[(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

def number_geodes(policies, t=24):
    max_robs = [max([-p[i] for p in policies]) for i in range(3)]
    s={}
    def value_function(t, robots, mats):

        if (t, robots, mats) in s:
            return s[(t, robots, mats)]

        mats_new = t_add(mats, robots)

        if t == 1:
            return mats_new[-1]

        mats_temp = t_add(mats, policies[3])
        if min(mats_temp) >= 0:
            res = value_function(t-1, t_add(robots, rob_pol[3]), t_add(mats_new, policies[3]))
            s.update({(t, robots, mats) : res})
            return res

        option_list = []

        for i in range(3):
            if robots[i] < max_robs[i]:
                mats_temp = t_add(mats, policies[i])
                if min(mats_temp) >= 0:
                    option_list += [value_function(t-1, t_add(robots, rob_pol[i]), t_add(mats_new, policies[i]))]
        
        if len(option_list) == 0 or mats_new[0] + robots[0]<= max_robs[0] * 2:
            option_list += [value_function(t-1, robots, mats_new)]

        res = max(option_list)
        s.update({(t, robots, mats) : res})
        return res  

    return value_function(t, robots, mats) 


total = 0
for idx, policy in enumerate(pol_list):
    total += (idx + 1) * number_geodes(policy)
  
print(total)

total = 1
for idx, policy in enumerate(pol_list[:3]):
    total *= number_geodes(policy, t = 32)

print(total)


  