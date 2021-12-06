count = 0
with open('input.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    for i in range(len(lines)-1):
        if lines[i] < lines[i+1]:
            count += 1
    print(count)