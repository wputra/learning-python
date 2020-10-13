#!/usr/bin/python3

test = "a!!!b.c.d,e'f,ghi"

def reverse(text):
    index = -1

    # range(start, stop, step)
    # only half of the list
    for i in range(len(text)-1, int(len(text)/2), -1):
        if text[i].isalpha():
            temp = text[i]
            #print(f'1: {text[i]}')

            while True:
                index += 1
                # find alphabet then break
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    #print(f'2: {text[i]}')
                    break

    print(text)

# main
print(list(test))
reverse(list(test))
