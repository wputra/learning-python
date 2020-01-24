#!/usr/bin/python3

#Count the number of vowels that exist in a word and return that value.
#>> vowels('cradle')
#['a','e']
#
text = "You may be sitting quietly in your armchair, but you are far from motionless. I don't mean merely that your heart is beating, your blood is coursing through your veins and you are panting at the prospect of learning so many fascinating things from this book. In short, I don't mean simply that you are physically and mentally alive."


def get_letter(letter,word):
    word = word.lower()
    my_vowels = []

    for i in word:
        if i in letter:
            my_vowels.append(i)

    return my_vowels

def vowels(word):
    vowels = "aiueoy"
    letter = get_letter(vowels,word)
    dicts = {}

    for i in vowels:
        c = letter.count(i)
        if c > 0:
            dicts[i] = c

    print(dicts)

### MAIN ###
vowels(text)
