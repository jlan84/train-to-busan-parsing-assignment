from string import punctuation
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS
import text_parsing_functions as tpf

if __name__ == '__main__':
    replace = 'person'
    names = set(['suan', 'seongkyeong', 'yonsuk', 'seokwoo', 'ingil', 'yonghuk'
                 'jinhee'])
    filepathr = 'train_to_busan_description.txt'
    clean_text = []
    with open(filepathr) as fp:
        lines = fp.readlines()
        for line in lines:
            clean_text.append(tpf.line_cleaning_pipeline(line, stopwords, names, replace))
    print(clean_text)
    filepathw = "../parsed/train_to_busan.txt"
    with open(filepathw, mode= 'wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(lines))
        