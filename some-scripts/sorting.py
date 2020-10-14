#!/usr/bin/python3
test = "62764375878243736423747364782198595017830"

def test_sort(input):
    #print(f'llll: {len(input)}')
    for i in range(0, len(input)):
        #print(f'1: {i}')
        for j in range(i+1, len(input)):
            #print(f'  2: {j}')
            if input[j] < input[i]:
                temp = input[j]
                input[j] = input[i]
                input[i] = temp

    print(input)

# main
test_sort(list(test))
