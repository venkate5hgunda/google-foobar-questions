def solution(n):
    num=int(n)
    steps=0
    while(num!=1):
        if(num%2==0):
            num=num/2
        elif(num!=3 and (num+1)%4==0):
            num+=1
        else:
            num-=1
        steps+=1
    return steps

print(solution("1241532546347347372523526262623632"))
