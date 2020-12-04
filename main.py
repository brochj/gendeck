# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:40:11 2020

@author: broch
"""
# Dicionario
# http://www.mso.anu.edu.au/~ralph/OPTED/

import genanki
import random

model_id = random.randrange(1 << 30, 1 << 31)
deck_id = random.randrange(1 << 30, 1 << 31)

my_model = genanki.Model(
  1962161376,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])


words = [
    {'word': "water", "definition": "liquid"},
    {'word': "fire", "definition": "hot"},
    ]

my_deck = genanki.Deck(
        2106080373,
      'Longman')

for word in words:
    
    my_note = genanki.Note(model=my_model, fields=[word['word'], word['definition']])    
    
    my_deck.add_note(my_note)

    genanki.Package(my_deck).write_to_file('output.apkg')



# class Search:
    
#     def __init__(self, unique_words, filename):
#         self.unique_words = unique_words
#         self.filename = filename
#         self.words_list = []
#         self.found_words = []
#         self.not_found_words = []
#         self.found_words_pct = 0.0
#         self.not_found_words_pct = 0.0
        
#         self.load_words_list()
#         self.search_words()
#         self.calc_pct()
    
#     def load_words_list(self):
#         file = open(f"words_lists/{self.filename}", "r")
#         self.words_list = file.read().lower().split()
#         if ',' in self.words_list[0]:
#             self.words_list = [word[:word.find(',')] for word in self.words_list if ',' in word]
#         file.close()
    
#     def search_words(self):
#         for word in self.unique_words:
#             if (word in self.words_list):
#                 self.found_words.append(word)
#             else:
#                 self.not_found_words.append(word)     
    
#     def calc_pct(self):
#         self.found_words_pct = round((len(self.found_words)/len(self.unique_words))*100,1)
#         self.not_found_words_pct = round((len(self.not_found_words)/len(self.unique_words))*100,1)
        



# if __name__ == "__main__":
#     searchInstance = Search()