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

# oxford.search('umbrella')

words_tests = ['umbrella', 'round', 'drink', 'computer', 'water']


for word in words[:200]:
    print(f'-----{word}---------')

    oxford.search(word)
    
    
    try:
        word_dict = {
            'word': word,
            'definitions' : oxford.definitions[0],
            'examples' : oxford.examples[0][0],
            'nam' : oxford.ipa_nam,
            'br' : oxford.ipa_br,
            'word_type' : oxford.word_type,
            'word_level' : oxford.word_level
        }
    except:
        words_error.append(word)
        continue
    
    
    file =  open('words_200.txt', 'a', newline='', encoding='utf-8')
    fieldnames = ['word', 'definitions', 'examples', 'nam', 'br', 'word_type', 'word_level']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='|')
    writer.writerow(word_dict)   
    
    file.close
    
    time.sleep(8)
    print('--------------')















