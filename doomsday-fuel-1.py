# Identify the Terminal States
# Make the diagonal elements identity for terminal states (indicating they're absorbing states)
# Normalize all state probabilities (percentages)
# Restructure the matrix into IORQ State (I: All Terminal States, O: Terminal->Non-Terminal State Probabilities, R: Non-Terminal->Terminal State, Q: Non-Terminal->Non-Terminal State)
# Calculate F: where F is inv(I-Q) where I is Identity of size Q
# Calculate FR: F.R to convert IORQ matrix into I-0-FR-0 matrix which is the terminal state matrix for the given probabilities

import numpy as np
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
    return np.linalg.inv(np.subtract(np.identity(len(q)),q))

def fraction_to_decimal_with_lcm_at_end(fr_arr):
    dr_arr=[]
    denoms=[]
    for num in fr_arr:
        fr=frac(num).limit_denominator()
        dr_arr.append(fr.numerator)
        denoms.append(fr.denominator)
    lcd=1
    for dn in denoms:
        lcd=np.lcm(lcd,dn)
    for i in range(len(dr_arr)):
        dr_arr[i]*=int(lcd/denoms[i])
    dr_arr.append(lcd)
    return dr_arr

def solution(m):
    r_mat,q_mat=get_rq_from_iorq(m)
    f_mat=get_f(q_mat)
    fr_mat=np.dot(f_mat,r_mat)
    return fraction_to_decimal_with_lcm_at_end(fr_mat[0])

print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
