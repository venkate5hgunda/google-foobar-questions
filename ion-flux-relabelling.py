numEl=0
def solution(h,q):
    parents = []
    global numEl
    numEl=(2**h)-1
    for qEl in q:
        parents.append(find_parent(qEl))
    return parents 

dictionary={}
def find_parent(el):
    start=1
    end=numEl
    if(end==el):
        return -1
    if dictionary.get(el,-1)!=-1:
        return dictionary[el]
    while(el>=1):
        end=end-1
        mid=start+(end-start)//2
        if(mid==el or end==el):
            dictionary[el]=end+1
            return end+1
        elif el<mid:
            end=mid
        else:
            start=mid


solution(3,[1,2,3,4,5])
