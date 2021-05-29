import math

def solution(n):
    steps=0
    num=n
    while(len(num)!=1 or num[0]!='1'):
        steps+=1
        if(is_divisible_by_two(num)):
            num=divide(num,2)
        else:
            num=convert_to_divisible_by_four(num)
    return steps

def is_divisible_by_two(num):
    if((ord(num[len(num)-1])-ord('0'))%2!=0):
        return False
    return True

def convert_to_divisible_by_four(num): # convert into 4 divisible number by adding/subtracting a number
    ans=""
    if(len(num)<2):
        ans+=chr((ord(num[0])-ord('0')-1)+ord('0') if (ord(num[0])-ord('0')-1)%4==0 else (ord(num[0])-ord('0')+1)+ord('0'))
    else:
        idx=len(num)-1
        temp=(ord(num[idx-1])-ord('0'))*10+(ord(num[idx])-ord('0'))
        if((temp+1)%4==0):
            ans=chr((int(((ord(num[idx])-ord('0'))+1)%10))+ord('0'))
            carry=((ord(num[idx])-ord('0'))+1)//10
            idx-=1
            while(idx>=0 or carry!=0):
                if(idx<0):
                    ans=(chr((int(carry%10))+ord('0')))+ans
                    carry=0
                else:
                    ans=(chr((int(((ord(num[idx])-ord('0'))+carry)%10))+ord('0')))+ans
                    carry=((ord(num[idx])-ord('0'))+carry)//10
                    idx-=1
        else:
            ans=chr((int(((ord(num[idx])-ord('0'))-1)%10))+ord('0'))
            carry=((ord(num[idx])-ord('0'))-1)//10
            idx-=1
            while(idx>=0 or carry!=0):
                if(idx<0):
                    ans=(chr((int(carry%10))+ord('0')))+ans
                    carry=0
                else:
                    ans=(chr((int(((ord(num[idx])-ord('0'))+carry)%10))+ord('0')))+ans
                    carry=((ord(num[idx])-ord('0'))+carry)//10
                    idx-=1
    return ans

def divide(num,div):
    i=0
    temp=0
    while(temp<div):
        temp=temp*10+(ord(num[i])-ord('0'))
        i+=1
    ans=""
    while(i<len(num)):
        ans+=chr(int(temp/div)+ord('0'))
        temp=(temp%div)*10+(ord(num[i])-ord('0'))
        i+=1
    ans+=chr(int(temp/div)+ord('0'))
    if(len(ans)==0):
        return "0"
    else:
        return ans

print("steps:",solution("12312415535212481986195816295826195695"))
