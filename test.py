from typing import List

string = "hello"
list = [*string]
print(list)

ref = "hello"

words = ["hi"]

ref_letters = [*ref]

sets = 0
for word in words:
    word_letters = [*ref]
    bw_word_letters = word_letters[::-1]
    for x in range(len(ref_letters)):
        print(x)
    for x in range((len(ref_letters)),-1,-1):
        print(x)
    for x in range(len(bw_word_letters)):
        print(bw_word_letters[x])

