# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:08:30 2020

@author: broch
"""

from oxford import Oxford
import time
import csv
import shelve
import copy
import random


def load_words_list(filename):
    file = open(f"../words_lists/{filename}", "r")
    words_list = file.read().split()
    if "," in words_list[0]:

        formatted_word_list = []
        words = []

        for word in words_list:
            words.append(word[: word.find(",")])

            word = word.replace(",", "[", 1)
            index = word.find(",S")
            word = word[:index] + "]" + word[index + 1 :]
            formatted_word_list.append(word)

        words_list = [word[: word.find(",")] for word in words_list if "," in word]

    file.close()
    return formatted_word_list, words


def save_word_to_csv(word_data, filename):
    file = open(filename, "a", newline="", encoding="utf-8")
    fieldnames = ["word", "definitions", "ipa_nam", "ipa_br", "word_type", "word_level"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="|")
    writer.writerow(word_data)
    file.close()
    return

def save_word_to_shelve(index, word_data, filename):
    shelf = shelve.open(filename)
    shelf[str(index)] = copy.deepcopy(word_data)
    shelf.close()
    return

def read_word_from_shelve(filename):
    words_list = []
    shelf = shelve.open(filename)
    key_list = list(shelf.keys())

    for key in key_list:
        word_data = shelf[key]
        words_list.append(word_data)

    shelf.close()
    return words_list



def save_word_not_found(word):
    file = open(WORDS_ERRORS_FILENAME, "a", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow([word])
    file.close()
    return


word_list, words = load_words_list("s1.txt")
words_error = []
word_dict = {}

oxford = Oxford()

words_tests = [
    "actual",
    "car"]
#     "can",
#     "close",
#     "depend",
#     "last",
#     "lead",
#     "live",
#     "minute",
#     "plus",
#     "process",
#     "rid",
#     "ring",
#     "second",
#     "used",
# ]


START = 0
END = 1000

WORDS_ERRORS_FILENAME = f"words_{START}_{END}-errors.txt"
WORDS_FILENAME = f"words_{START}_{END}.shlf"

ENDPOINTS = [
    "_1",
    "_2",
    "_3",
    "_4",
    "_5",
    "1_1",
    "1_2",
    "1_3",
    "1_4",
    "1_5",
    "2_1",
    "2_2",
    "2_3",
    "2_4",
    "2_5",
]

for i, word in enumerate(words):
# for i, word in enumerate(words_tests):
    print(f"\n[{i}]-----{word}---------")

    ## Simple Search
    try:
        oxford.search(word.lower())
        word_dict = oxford.formatted_data
    except:
        words_error.append(word)
        save_word_not_found(word)
        continue

    print("\nSaving Word")
    print('\nWriting on',i, 'key')
    save_word_to_shelve(i, word_dict, WORDS_FILENAME)
    # save_word_to_csv(word_dict, WORDS_FILENAME)

    print("--------------\n")
    time.sleep(random.randint(8,15))

    ## Advanced Search
    ## Usar apenas nas palavras que não foram encotradas pelo metodo acima
    # for ep in ENDPOINTS:
    #     try:
    #         print(f'\nSearching {word + ep}')
    #         oxford.search(word + ep)
    #         word_dict = oxford.formatted_data
    #     except:
    #         print(f'\n{word + ep} not found')
    #         time.sleep(5)
    #         continue

    #     print('\nSaving Word: {word + ep}')
    #     save_word_to_csv(word_dict, WORDS_FILENAME)
    #     time.sleep(5)
    #     continue

    # print('--------------\n')
    # time.sleep(10)




shelf = read_word_from_shelve(WORDS_FILENAME)




#################################


# def advanced_search(word):
#     ENDPOINTS = [
#         "_1",
#         "_2",
#         "_3",
#         "_4",
#         "_5",
#         "1_1",
#         "1_2",
#         "1_3",
#         "1_4",
#         "1_5",
#         "2_1",
#         "2_2",
#         "2_3",
#         "2_4",
#         "2_5",
#     ]

#     for ep in ENDPOINTS:
#         try:
#             print(f"\nSearching {word} as {word + ep}")
#             # oxford.search(word + ep)
#             # word_dict = oxford.formatted_data
#         except:
#             print(f"\n{word + ep} not found")
#             words_error.append(word)
#             # save_word_not_found(word)
#             time.sleep(5)
#             continue

#         save_word_to_csv(word_dict, WORDS_FILENAME)
#         time.sleep(5)
#         print("\nSaving Word: {word + ep}")

#     print("\nSaving Word")
#     # save_word_to_csv(word_dict, WORDS_FILENAME)

#     print("--------------\n")
#     time.sleep(10)
#     pass
