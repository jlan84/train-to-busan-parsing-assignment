from string import punctuation
from sklearn.feature_extraction import stop_words
stopwords = stop_words.ENGLISH_STOP_WORDS

def lowercase_text(text):
    pass

def remove_punctuation(text, punctuation=punctuation):
    pass 

def remove_newline(text):
    pass

def split_text_into_words(text):
    pass

def remove_stopwords(word_lst, stopwords_set):
    pass

def replace_names(word_lst, name_set, replacement_val):
    pass

def create_cleaned_textline_from_words(words):
    pass

def line_cleaning_pipeline(text, stopwords_set, name_set, replace_val):
    text_lc = lowercase_text(text)
    text_np = remove_punctuation(text_lc)
    text_nnl = remove_newline(text_np)
    words = split_text_into_words(text_nnl)
    words_nsw = remove_stopwords(words, stopwords_set)
    words_cleaned = replace_names(words_nsw, name_set, replace_val) 
    line_of_text_cleaned = create_cleaned_textline_from_words(words_cleaned)
    return line_of_text_cleaned

if __name__ == '__main__':
    # to help test functions and pipeline:
    text_str1 = "Seok-woo, a divorced fund manager, is a workaholic and absentee father to \nhis"
    text_str2 = "young daughter, Su-an. For her birthday the next day, she wishes for her father\n"
    text_str3 = "to take her to Busan to see her mother. \nThey board the KTX at Seoul Station."

    # your code below

