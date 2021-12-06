horizontal_position = 0
depth = 0

with open('course.txt') as input:
    lines = input.readlines()  
    for line in lines:
        direction, units  = line.split(" ")
        units = int(units)
        if direction == 'forward' and units > 0:
            horizontal_position += units
        if direction == 'up' and units > 0:
            depth -= units
        if direction == 'down' and units > 0:
            depth += units
    print(horizontal_position * depth)
    
    # with open("day2.txt") as puzzle_input:
    # x = y = 0
    # for line in puzzle_input:
    #     match line.split(" "):
    #         case ["forward", steps]:
    #             x += int(steps)
    #         case ["up", steps]:
    #             y -= int(steps)
    #         case ["down", steps]:
    #             y += int(steps)
    
    # print(x * y)
            