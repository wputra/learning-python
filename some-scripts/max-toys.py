#!/usr/bin/python3
def maximumToys(prices, k):
    s = 0
    for i in prices:
        if i<=k:
            s+=1
            k-=i
        #else:
        #    break


    return s

in1 = "7 50"
in2 = "1 12 5 111 200 1000 10"

n,k = map(int, in1.split())
#prices = sorted(map(int,input().split()))
prices = map(int, in2.split())
print(maximumToys(prices, k))
#print(int(k))
#print(in_list)
