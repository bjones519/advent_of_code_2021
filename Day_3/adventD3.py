power_consumption = 0
gamma_rate = ''
epsilon_rate = ''


with open('binary.txt') as input:
    lines = input.readlines()
    for index in range(12):
        zero_count = 0
        one_count = 0
        for i in lines:
            i = i.strip()
            if i[index] == '0':
                zero_count += 1
                
            else: 
                one_count += 1
                
        if zero_count > one_count:
            gamma_rate += '0'
            
        else:
            gamma_rate += '1' 
            
        if zero_count < one_count:
            epsilon_rate += '0'
            
        else:
            epsilon_rate += '1'       
        print((int(gamma_rate,2) * int(epsilon_rate,2)))