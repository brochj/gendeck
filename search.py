# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:37:58 2020

@author: broch
"""
# import nltk
from nltk.corpus import wordnet as wn
# nltk.download('wordnet')
dog = wn.synsets('car') 


words = ['car','dog', 'arugula', 'ad', 'cot']

print(dog)
print(dog[0].lemma_names())

dictionary = []

for word in words:
    synsets_list = wn.synsets(word)
    
    dictionary.append({
        'word': word,
        'definition':synsets_list[0].definition()
        }) 
    
    
    for i in range(len(synsets_list)):
        
        found_word = synsets_list[i].name()
        
        if found_word[:found_word.find('.')] == word:
            
        
            print(synsets_list[i].name())
        
            print(i,": ", synsets_list[i].definition())
    
    print('-------')
    
# print(dog[0].definition())
# print(dog[1].definition())
# print(dog[2].definition())
# print(wn.synset('dog.n.02').definition())
# print(wn.synset('frump.n.01').definition())
# print(wn.synset('andiron.n.01').definition())