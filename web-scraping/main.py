# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:08:30 2020

@author: broch
"""

from oxford import Oxford
import time
import csv


def load_words_list(filename):
    file = open(f"../words_lists/{filename}", "r")
    words_list = file.read().split()
    if ',' in words_list[0]:
        
        formatted_word_list = []
        words = []
        
        for word in words_list:
            words.append(word[:word.find(',')])
            
            word = word.replace(',', '[', 1)
            index = word.find(',S')
            word = word[:index] + ']' + word[index + 1:]
            formatted_word_list.append(word)
            
        
        words_list = [word[:word.find(',')] for word in words_list if ',' in word]

    file.close()
    return formatted_word_list , words


word_list, words = load_words_list('s1.txt')
words_error = []

oxford = Oxford()

words_tests = ['afternoon']



WORDS_ERRORS_FILENAME = 'words_200_500_errors.txt'
WORDS_FILENAME = 'words_200_500.txt'


for word in words[200:500]:
# for word in words_tests:    
    print(f'\n-----{word}---------')
    
    # Oxford Word Endpoints
    # _1 , _2, 1_1, 1_2, 1_3, 1_4, 2_1
    # Examples: word_1, word1_1
    
    

    try:
        oxford.search(word)
        word_dict = oxford.formatted_data
    except:
        words_error.append(word)      
        file =  open(WORDS_ERRORS_FILENAME, 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow([word])
        file.close
        continue
    
    
    file =  open(WORDS_FILENAME, 'a', newline='', encoding='utf-8')
    fieldnames = ['word', 'definitions', 'ipa_nam', 'ipa_br', 'word_type', 'word_level']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='|')
    writer.writerow(word_dict) 
    file.close
    
    print('\n--------------\n')
    time.sleep(10)
    















