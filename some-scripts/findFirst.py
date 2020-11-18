#!/usr/bin/python3

"""
Finds the first character that does not repeat anywhere in the input string
If all characters are repeated, return 0
Given "apple", the answer is "a"
Given "racecars", the answer is "e"
Given "ababdc", the answer is "d"
"""
def findFirst(str):
    #todo: implement solution
    c = 0
    elist = []
    for a in str:
        if a not in elist and str.count(a) == 1:
            c = c +1
            elist.append(a)
            break
    if c == 0:
        a = '0'
    
    
    return a
   

"""
Returns true if all tests pass. Otherwise returns false
"""
def doTestsPass():
    # todo: implement more tests
    doPass = True
    tests = {"racecars":'e', "apple":'a', "ababdc":'d', "abcabc":'0', "": '0'}
    for test in tests.items():
        result = findFirst(test[0])
        if result != test[1]:
            print("Test Failed: " + test[0] + " expected:" + test[1] + " actual: " + result + "\n")
            return False

    return True


if __name__ == "__main__":
    result = doTestsPass()

    if result:
            print("All tests pass\n");
    else:
            print("Tests fail\n");
