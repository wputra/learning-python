#!/usr/bin/python3
def solution(A):
    k = 0
    for i in range(len(A)):
        val = A[i]
        nval = 0 - val
        if val > k and nval in A:
            k = int(val)
    print(k)

test = [3,2,-2,5,-3]
solution(test)
