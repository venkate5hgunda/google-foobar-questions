# Identify the Terminal States
# Make the diagonal elements identity for terminal states (indicating they're absorbing states)
# Normalize all state probabilities (percentages)
# Restructure the matrix into IORQ State (I: All Terminal States, O: Terminal->Non-Terminal State Probabilities, R: Non-Terminal->Terminal State, Q: Non-Terminal->Non-Terminal State)
# Calculate F: where F is inv(I-Q) where I is Identity of size Q
# Calculate FR: F.R to convert IORQ matrix into I-0-FR-0 matrix which is the terminal state matrix for the given probabilities

from fractions import Fraction as frac

def get_rq_from_iorq(m):
    terminal_states=set()
    for row in range(len(m)):
        if sum(m[row])==0:
            terminal_states.add(row)
    r_mat=[] # non-terminal->terminal
    q_mat=[] # non-terminal->non-terminal
    for row in range(len(m)):
        if row not in terminal_states:
            row_sum = float(sum(m[row]))
            r_row=[]
            q_row=[]
            for col in range(len(m)):
                if col in terminal_states:
                    r_row.append(m[row][col]/row_sum)
                else:
                    q_row.append(m[row][col]/row_sum)
            r_mat.append(r_row)
            q_mat.append(q_row)
    return r_mat,q_mat

def get_f(q):
    return inverse(subtract(identity(len(q)),q))

def fraction_to_decimal_with_lcm_at_end(fr_arr):
    dr_arr=[]
    denoms=[]
    for num in fr_arr:
        fr=frac(num).limit_denominator()
        dr_arr.append(fr.numerator)
        denoms.append(fr.denominator)
    lcd=1
    for dn in denoms:
        lcd=lcm(lcd,dn)
    for i in range(len(dr_arr)):
        dr_arr[i]*=int(lcd/denoms[i])
    dr_arr.append(lcd)
    return dr_arr

def solution(m):
    if len(m)<2:
        return [1,1]
    r_mat,q_mat=get_rq_from_iorq(m)
    f_mat=get_f(q_mat)
    fr_mat=dot(f_mat,r_mat)
    return fraction_to_decimal_with_lcm_at_end(fr_mat[0])


# helper functions to remove numpy dependency
def lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if((greater%a==0) and (greater%b==0)):
            lcm=greater
            break
        greater+=1
    return lcm

def dot(a,b):
    if(len(a[0])!=len(b)): 
        print(len(a[0]))
        print(len(b))
        return []
    a_b=[]
    for i in range(len(a)):
        temp=[]
        for j in range(len(b[0])):
            temp_elem=0.0
            for k in range(len(a)):
                temp_elem+=(a[i][k]*b[k][j])
            temp.append(temp_elem)
        a_b.append(temp)
    return a_b

def identity(s):
    iden=[]
    for i in range(0,s):
        temp=[]
        for j in range(0,s):
            if i==j:
                temp.append(1)
            else:
                temp.append(0)
        iden.append(temp)
    return iden

def subtract(a,b):
    a_b=[]
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(a[0])):
            temp.append(a[i][j]-b[i][j])
        a_b.append(temp)
    return a_b

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
