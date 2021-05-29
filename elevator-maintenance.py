def solution():
    input_ver = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.1.2","1.0.2"]
    for inp in input_ver:
        print(calc_priority(inp))

def calc_priority(subject):
    sub_split=[-1,-1,-1]
    temp=subject.split('.')
    for i in range(0,len(temp)):
        sub_split[i]=(int)(temp[i])

    print('Length of Split: ',len(sub_split),sub_split)
    value=0.0
    for i in range(3,3-(len(sub_split)),-1):
        print((int(sub_split[3-i])*(10**(i-1))))
        value=value+(int(sub_split[3-i])*(10**(i-1)))
    value=value+(0.1*len(sub_split))
    return value

solution()
