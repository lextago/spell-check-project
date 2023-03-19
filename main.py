import math, os, pickle,re
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
        self.training_data_directory: str = "test_folder"

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
            print(text)
            token = self.tokenize(text)
            print(token)
            
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

if __name__ == "__main__":
    print("Hello")
    s = spell_check()
    test_list = ["I", "am", "a", "goofy", "goober", "I", "like", "goofy", "goober"]
    test_dict = {}

    s.update_dict(test_list, test_dict)

    print(test_dict)
    print(s.words_dict)