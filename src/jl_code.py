from string import punctuation
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import argparse

class TextParser():

    def __init__(self, file, name_lst, replacement_val, write_file):
        self.file = file
        self.name_lst = name_lst
        self.replacement_val = replacement_val
        self.write_file = write_file
        self.parser = argparse.ArgumentParser()

    def read_file(self):
        self.parser.add_argument('--file', '-f', type=str, required=True)
        self.parser.add_argument('--out', '-o', type=str, required=True)
        self.args = self.parser.parse_args()
        with open(self.args.file, 'r') as f:
            self.txt = f.read()
        
    def lower_case(self):
        self.txt = self.txt.lower()
        
    def remove_punct(self):
        self.txt = ''.join([ch for ch in self.txt if ch not in punctuation])
    
    def remove_stop_words(self):
        self.txt.replace('\n',' ')
        words = self.txt.split(' ')
        self.txt_lst = [word for word in words if word not in ENGLISH_STOP_WORDS]
        self.txt = ' '.join(self.txt_lst)
        
    def word_count(self):
        self.top_words = Counter(self.txt_lst).most_common(10)
    
    def replace_names(self):
        self.txt_lst = [self.replacement_val if word in 
                        self.name_lst else word for word in self.txt_lst]
        self.txt = ' '.join(self.txt_lst)

    def write(self):
        lst = self.txt.split('\n')
        with open(self.args.out, 'w') as f:
            for line in lst:
                f.write(line + '\n')

    def pipeline(self):
        self.read_file()
        self.lower_case()
        self.remove_punct()
        self.remove_stop_words()
        self.replace_names()
        self.write()


if __name__ == "__main__":
    name_lst = set(['suan', 'seongkyeong', 'yonsuk', 'seokwoo', 'ingil', 'yonghuk'
                 'jinhee'])
    replacement_val = 'person'
    tp = TextParser('../data/train_to_busan_description.txt', name_lst, 
                    replacement_val, '../parsed/train_to_busan2.txt')
    tp.pipeline()
    
    
    
    

    

    

