horizontal_position = 0
depth = 0
aim = 0

with open('course.txt') as input:
    lines = input.readlines()
    for line in lines:
        direction, units = line.split(" ")
        units = int(units)
        if direction == 'forward' and units > 0:
            horizontal_position += units
            depth += aim * units
        if direction == 'up' and units > 0:
             aim -= units
        if direction == 'down' and units > 0:
             aim += units
    print(horizontal_position * depth)
    
            