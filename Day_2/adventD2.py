horizontal_position = 0
depth = 0

with open('course.txt') as f:
    lines = f.readlines()
    print(lines)
    
    for line in lines:
        direction, step  = line.split(" ")
        step = int(step)
        if direction == 'forward' and step > 0:
            horizontal_position += step
        if direction == 'up' and step > 0:
            depth -= step
        if direction == 'down' and step > 0:
            depth += step
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
            