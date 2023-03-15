import math, os, pickle
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
        
        if os.path.isfile(self.words.dat):
            print("Data files found... teehee")
            self.load_file()



if __name__ == "__main__":
    print("Hello")

# _/(o v o)/* oh i think that i found myself a cheerleader
# she is always right there when i need her