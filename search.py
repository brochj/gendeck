# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:37:58 2020

@author: broch
"""
# import nltk
from nltk.corpus import wordnet as wn
import eng_to_ipa as ipa
# nltk.download('wordnet')

dog = wn.synsets('car') 


words = ['car','dog', 'arugula', 'ad', 'cot']

ipa.convert("The quick brown fox jumped over the lazy dog.")

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
    
    

print(dog[0].definition())
print(dog[1].definition())
print(dog[2].definition())
print(wn.synset('dog.n.02').definition())
print(wn.synset('frump.n.01').definition())
print(wn.synset('andiron.n.01').definition())


# class Search:
    
#     def __init__(self, filename):
#         self.filename = filename
#         self.words_list = []
#         self.found_words = []
#         self.not_found_words = []
#         self.new_words_list = []
        
#         self.load_words_list()
#         self.search_words()
    
#     def load_words_list(self):
#         file = open(f"words_lists/{self.filename}", "r")
#         self.words_list = file.read().lower().split()
#         if ',' in self.words_list[0]:
#             self.words_list = [word[:word.find(',')] for word in self.words_list if ',' in word]
#         file.close()
    
#     def search_words(self):
#         for word in self.words_list:
#             synsets_list = wn.synsets(word)
            
#             if len(synsets_list) > 0:
#                 # self.found_words.append(word)
#                 self.new_words_list.append({
#                     'word': word,
#                     'definition':synsets_list[0].definition()
#                     })
                
#                 print(word)
#                 print(synsets_list[0].definition())
                
#             else:
#                 print(f'{word} : NOT FOUND')
#                 self.not_found_words.append(word) 
                
            
#             # for i in range(len(synsets_list)):
                
#             #     found_word = synsets_list[i].name()
                
#             #     if found_word[:found_word.find('.')] == word:
                    
                
#             #         print(synsets_list[i].name())
                
#             #         print(i,": ", synsets_list[i].definition())
            
#             print('-------')
            
            
            
#             # if (word in self.words_list):
                
    



# if __name__ == "__main__":
#     searchInstance = Search('s1.txt')
#     found_words = searchInstance.found_words
#     not_found_words = searchInstance.not_found_words
#     new_words_list = searchInstance.new_words_list