count = 0

with open('input.txt') as input:
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    for i in range(len(lines)-1):
        if lines[i] < lines[i+1]:
            count += 1
    print(count)