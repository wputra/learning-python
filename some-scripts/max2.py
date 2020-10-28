#!/usr/bin/python3

def test_max(input):
    m1 = input[0]
    m2 = input[1]
    if m1 < m2:
        m1 = input[1]
        m2 = input[0]
        
    for i in range(2,len(input)):
        if input[i] >= m1:
            m2 = m1
            m1 = input[i]
        elif input[i] > m2:
            m2 = input[i]
                
    print(m2)

input = [5, -5, -1]
#input = [5, 1, 5, 4, 2]

test_max(input)
