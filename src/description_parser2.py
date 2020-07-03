from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS
import text_parsing_functions as tpf
import argparse
from string import punctuation

def read_lines(filepathr, stopwords, names, replace):
    clean_text = []    
    with open(filepathr) as fp:
        for line in fp:
            clean_line = tpf.line_cleaning_pipeline(line, stopwords, names, replace)
            clean_text.append(clean_line)
    return clean_text


def write_lines(lst, filepathw):
    with open(filepathw, mode= 'wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(clean_text))
    return myfile


if __name__ == '__main__':
    replace = 'person'
    names = set(['suan', 'seongkyeong', 'yonsuk', 'seokwoo', 'ingil', 'yongguk'
                 'jinhee', 'sanghwa'])
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, required=True)
    parser.add_argument('--output','-o', type=str, required=True)
    args = parser.parse_args()

    file_in = args.input
    clean_text = read_lines(file_in, stopwords, names, replace)

    file_out = args.output
    write_lines(clean_text, file_out)