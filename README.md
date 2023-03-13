# spell-check-project
Intro to AI Project - Period 2 by Alex Tago and Maddy Rowe

https://norvig.com/spell-correct.html
Shamelessly basing this project off of Peter Norvig’s project!

Our project is to create a spell checker / auto corrector.
The goal is to be able to input a mispelled word and have the program return possible words with proper spelling.

The plan is to use actual dictionaries or books as training data.
When a mispelled word is entered, the program should first check if the word is spelled correctly. This is done if the word exists in the dictionary.

IF the word does not exist in the dictionary, then it is mispelled. The program should tokenize this word by splitting it into individual letters. 

The program will then take these tokens and compare them to the letters of other words in the dictionary. 

If the count of tokens in the mispelled word is similar to the count of tokens in another word, then that word will be placed in a list of possibly correct words. 

Since this list will be long, the program needs to check which one of these words is most probable to being the correctly spelled word.

To do this, the program could tokenize books and other texts to find how many times a word is used in the dictionary. 

Then, the program could simply determine which word appears the most in the dictionary and use this as the probable correct word.


To take this to the next level, perhaps there could be a way to determine a correct word in a sentence based on context, by first finding the list of probable words, then determining its probable part of speech based on the adjacent words. 
