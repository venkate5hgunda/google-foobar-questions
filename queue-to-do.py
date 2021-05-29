# METHOD 1: THIS IS O(n2) SOLUTION, FOUND A O(n) SOLUTION
# def solution(start,length):
#     xor=0
#     for i in range(0,length):
#         for j in range(0,length-i):
#             xor=xor^((start+length*i)+j)
#     return xor

def solution(start,length):
    xor=0
    for i in range(0,length):
        xor=xor^(XOR(start+length*i+(length-1-i))^XOR(start+length*i-1))
    return xor

def XOR(n):
    if n%4==0:
        return n
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0  

print(solution(234,100))
