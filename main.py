import math, os, pickle,re, copy
from typing import Tuple, List, Dict

class spell_check:
    """"spell check class
    
    Variables:
    
        words_dict[Word, Frequency] - dictionary of correcty spelled words and their frequency
        user_sentence - sentence sent as input (should be iterated thru)
    
    
    """ 
    """ this constructor initializes 
    """
    
    def __init__(self):
        self.words_dict: Dict[str, int] = {}
        self.words_filename: str = "words.dat"
        self.training_data_directory: str = "sentences/"

        if os.path.isfile(self.words_filename):
            print("Data files found - teehee...")
            self.words_dict = self.load_dict(self.words_filename)
        else:
            print("Data files not found - running training...")
            self.train()


    def train(self) -> None:
        _, __, files = next(os.walk(self.training_data_directory), (None, None, []))
        if not files:
            raise RuntimeError(f"Couldn't find path {self.training_data_directory}")
        
        for index, filename in enumerate(files, 1): # type: ignore
            print(f"Training on file {index} of {len(files)}")

            text = self.load_file(os.path.join(self.training_data_directory, filename))
            print(filename)
            token = self.tokenize(text)
            
            self.update_dict(token, self.words_dict)

        self.save_dict(self.words_dict, self.words_filename)



    def load_file(self, filepath: str) -> str:
        with open(filepath, "r", encoding='utf8') as f:
            return f.read()

    def save_dict(self, dict: Dict, filepath: str) -> None:
        print(f"Dictionary saved to file: {filepath}")
        with open(filepath, "wb") as f:
            pickle.Pickler(f).dump(dict)

    def load_dict(self, filepath: str) -> Dict:
        print(f"Loading dictionary from file: {filepath}")
        with open(filepath, "rb") as f:
            return pickle.Unpickler(f).load()

    def tokenize(self, text: str) -> List[str]:
        tokens = []
        token = ""
        for c in text:
            if (
                re.match("[a-zA-Z0-9]", str(c)) != None
                or c == "'"
                or c == "_"
                or c == "-"
            ):
                token += c
            else:
                if token != "":
                    tokens.append(token.lower())
                    token = ""
                if c.strip() != "":
                    tokens.append(str(c.strip()))
        if token != "":
            tokens.append(token.lower())
        return tokens
    
    def update_dict(self, words: List[str], freqs: Dict[str, int]) -> None:
        for word in words:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1

    def contains_letters(self, ref: str, words: Dict[str,int], rang:int) -> List[str]:    
        copy_words = list((copy.deepcopy(words)).keys())
        words_list = copy.deepcopy(copy_words)

        """this chunk checks if a the words in a list DO NOT contain the letters of the reference word"""
        # words_list = list((copy.deepcopy(words)).keys())

        # for word in words.keys():
        #     for letters in word:
        #         if letters not in ref:
        #             if word in words_list:
        #                 words_list.remove(word)

        # return words_list

        """this chunk checks if the words in a list DO contain the letters of the reference word"""
        for letters in ref:
            for word in copy_words:
                if letters not in word:
                    if word in words_list:
                        words_list.remove(word)

        # print(words_list)

        new_words_list = copy.deepcopy(words_list)

        for word in new_words_list:
            # print(word)
            word_letters = []
            for letters in word:
                word_letters.append(letters)
            # print(word_letters)

            '''list of letter differences between word from list and reference word'''
            diff_list = []

            for letters in word_letters:
                if letters not in ref:
                    diff_list.append(letters)
            # print(diff_list)

            if len(diff_list) > rang:
                if word in words_list:
                    words_list.remove(word)

        return words_list
            
   
    def spell_frequency(self, ref: str, words: List[str]) -> Dict[str, int]:
        ''' finds how many same letters exist in a reference word and a different word
        
        input:
            ref - reference word
            words - list of words to be compared
        
        output:
            dictionary of words with number of same letters as values
        '''
        words_corrections_rating = {}

        ref_letters = [*ref]
        bw_ref_letters = [*ref][::-1]

        for word in words:
            word_letters = [*word]
            # print(word_letters)
            bw_word_letters = word_letters[::-1]
            # print(bw_word_letters)
            sets = 0
            for x in range(min(len(ref), len(word))):
                # print("fw")
                # print(ref_letters[x])
                # print(word_letters[x])
                if ref_letters[x] == word_letters[x]:
                    sets += 1
                # print("bw")
                # print(bw_ref_letters[x])
                # print(bw_word_letters[x])
                if bw_ref_letters[x] == bw_word_letters[x]:
                    sets += 1
            words_corrections_rating[word] = sets

        return words_corrections_rating
    

    def most_frequent(self, words_list: List[str], words_dict: Dict[str,int]) -> Dict[str, int]:
        '''orders a dictionary by values in descending order'''
        converted_dict = {}

        for word in words_list:
            converted_dict[word] = words_dict[word]

        sorted_dict = sorted(converted_dict.items(), key=lambda x:x[1], reverse=True)
        sorted_dict = dict(sorted_dict)
            
        return sorted_dict
    
    def calculate_final_freqency(self, spell_freq: Dict[str, int], usage_freq: Dict[str, int], rang: int) -> Dict[str,int]:
        '''calculates final frequency/possibility of word using naive bayes. uses spelling frequency and usage frequency as input'''
        final_freq = {}

        for word in list(spell_freq.keys())[:rang]:
            if(spell_freq[word] != 0) and usage_freq[word] != 0:
                final_freq[word] = math.log(spell_freq[word] / sum(spell_freq.values())) + math.log(usage_freq[word] / sum(usage_freq.values()))

        return self.most_frequent(list(final_freq), final_freq)
    

    def search_recommendations(self, word: str)
        pass


if __name__ == "__main__":
    print("Hello")
    s = spell_check()

    """Testing on test list and dict"""

    test_list = ["I", "am", "a", "goofy", "goober", "I", "like", "goofy", "goober", "hello", "hellonc", "helo", "heo", "hello", "hello", "helaso", "helo"]
    test_dict = {}

    s.update_dict(test_list, test_dict)
    assert test_dict["I"] == 2, "testing dictionary"

    test_contain = s.contains_letters("he", test_dict, 2)

    print(test_contain)

    test_correction = s.spell_frequency("hello", test_contain)

    print(test_correction)

    test_freq_dict = s.most_frequent(test_contain, test_dict)

    print(test_freq_dict)

    test_freq_words = s.most_frequent(test_contain, test_correction)

    print(test_freq_words)

    test_final_freq = s.calculate_final_freqency(test_freq_words, test_freq_dict, 10)

    print(test_final_freq)

    """Testing on actual data"""

    print(s.words_dict["hello"])

    test_contain_2 = s.contains_letters("banana", s.words_dict, 2)

    # print(test_contain_2)

    test_correction_2 = s.spell_frequency("banana", test_contain_2)

    # print(test_correction_2)

    '''finds frequency of words spelled within 2 letters'''
    test_freq_2 = s.most_frequent(test_contain_2, test_correction_2)

    # print(test_freq_2)

    '''finds frequency of word use in the words_dict from data'''
    test_freq_3 = s.most_frequent(test_contain_2, s.words_dict)

    # print(test_freq_3)

    '''finda final frequency of word based on letter correction and word usage!'''

    # print(len(test_freq_2))
    # print(len(test_freq_3))

    test_final_freq_2 = s.calculate_final_freqency(test_freq_2, test_freq_3, 10)

    # print(test_final_freq_2)

    query = "Did you mean:"
    for x in test_final_freq_2.keys():
        query = query + " " + x + ","

    print(query + "?")