power_consumption = 0
gamma_rate = []
epsilon_rate = []
zero_count = 0
one_count = 0

with open('binary.txt') as input:
    lines = input.readlines()
    for i in lines:
        if i[0] == '0' and zero_count > one_count:
            zero_count += 1
            gamma_rate = ['0']
        else: 
            one_count += 1
            gamma_rate = ['1']
        print(gamma_rate)
