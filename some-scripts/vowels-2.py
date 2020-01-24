#!/usr/bin/python3

text = "You may be sitting quietly in your armchair, but you are far from motionless. I don't mean merely that your heart is beating, your blood is coursing through your veins and you are panting at the prospect of learning so many fascinating things from this book. In short, I don't mean simply that you are physically and mentally alive."
#response = {
#	'a':['apple','april'],
#	'e':['apple','red'],
#	'i':['it','kit']
#	#etc
#	}
# note: a word can exist under multiple keys.
# if possible, remove puncuation and make sure they dont exist twice.

def get_word(letter,sentences):
    sentences = (sentences.lower()).split()
    my_words = []

    for word in sentences:
        if letter in word and word not in my_words:
            my_words.append(word)

    return my_words

def vowels(sentences):
    vowels = "aiueoy"
    dicts = {}

    for vowel in vowels:
        words = get_word(vowel,sentences)
        if len(words) > 0:
            dicts[vowel] = words

    print(dicts)

### MAIN ###
vowels(text)
