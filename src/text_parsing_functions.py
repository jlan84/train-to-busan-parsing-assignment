from string import punctuation

def lowercase_text(text):
    '''Lowercases all characters in the text

       Parameters:
       text: a string containing uppercase and lowercase characters

       Returns:
       lowercase_text: a string containing only lowercase characters
    ''' 
    return text.lower() 

def split_text_into_words(text):
    '''Splits a long string into a list of separate words using a space as the
       delimiter

       Parameters:
       text: a string containing words separated by spaces

       Returns:
       words: a list of the separated words
    '''
    return text.split(' ')

def remove_punctuation(word_lst):
    '''Removes punctuation from each word in the word-list

       Parameters:
       word_lst: a list of words where some words contain punctuation

       Returns:
       word_lst_no_punc: a list of words where punctuation has been removed from
                         each word
    '''
    words = []
    for word in word_lst:
        words.append(''.join([c for c in word if c not in punctuation]))
    return words

def remove_stopwords(word_lst, stopwords_set):
    '''Removes words in the word_lst if they are in the stopwords_set

       Parameters:
       word_lst: a list of words
       stopwords_set: a set of words that are so common that they should be removed
    '''
    return [word for word in word_lst if word not in stopwords_set]

def lemmatize_words(word_lst, lemmatization_dict):
    '''Replaces a word in the words_lst with its lemmatized form if the word is 
       in the lemmatization_dict

       Parameters:
       word_lst: a list of words
       lemmatization_dict: a dictionary where the keys are the words that need to replaced
                           and the values are the lemmatized version that should replace them
    '''
    return [lemmatization_dict[word] if word in lemmatization_dict else word for word in word_lst] 



if __name__ == '__main__':
    lemmatization_dict = {'divorced': 'divorce',
                          'seokwoo': 'person',
                          'suan': 'person',
                          'wishes': 'wish'}

    text_str1 = "Seok-woo, a divorced fund manager, is a workaholic and absentee father to his"
    text_str2 = "young daughter, Su-an. For her birthday the next day, she wishes for her father"
    text_str3 = "to take her to Busan to see her mother. They board the KTX at Seoul Station."


    text = lowercase_text(text_str1)
    words0 = split_text_into_words(text)
    words1 = remove_punctuation(words0)
    words2 = remove_stopwords(words1, stopwords_set)



