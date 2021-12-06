count = 0

with open('input.txt') as input:
    lines = input.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    for i in range(len(lines)-3):
        sliding_sum_1 = lines[i] + lines[i+1] + lines[i+2]
        sliding_sum_2 = lines[i+1] + lines[i+2] + lines[i+3]
        if sliding_sum_1 < sliding_sum_2:
            count += 1
    print(count)