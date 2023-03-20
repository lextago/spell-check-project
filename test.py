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



        """this chunk checks if a the words in a list DO NOT contain the letters of the reference word"""
        # words_list = list((copy.deepcopy(words)).keys())

        # for word in words.keys():
        #     for letters in word:
        #         if letters not in ref:
        #             if word in words_list:
        #                 words_list.remove(word)

        # return words_list
