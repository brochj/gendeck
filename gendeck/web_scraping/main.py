# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:08:30 2020

@author: broch
"""

from oxford import Definition
import time
import csv
import shelve
import copy
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def load_words_list(filename):
    file = open(f"../words_lists/{filename}", "r")
    words_list = file.read().split()
    if "," in words_list[0]:

        formatted_word_list = []
        words = []
        words_type = []

        for word in words_list:
            words.append(word[: word.find(",")])

            word = word.replace(",", "[", 1)
            index = word.find(",S")
            word = word[:index] + "]" + word[index + 1:]
            formatted_word_list.append(word)

            word_type = word[word.find('['):word.find(']') + 1]
            word_type = word_type.replace('[', '').replace(']', '').split(',')
            words_type.append(word_type)

        words_list = [word[: word.find(",")] for word in words_list if "," in word]

    file.close()
    return formatted_word_list, words, words_type


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


def random_sleep(start=5, stop=10):
    return time.sleep(random.randint(start, stop))


def find_duplicates(lst: list) -> list:
    seen = set()
    duplicates = []
    for item in lst:
        if item not in seen:
            seen.add(item)
        else:
            duplicates.append(item)
    return duplicates


LIST_FILENAME = 's1_longman'

word_list, words, words_type = load_words_list(f"{LIST_FILENAME}.txt")
duplicated_words = sorted(list(set(find_duplicates(words))))
words = list(set(words))


# %%
words_error = []
word_dict = {}

oxford = Definition()

# Palavras que deram errado na primeira vez
w3_add = ['o-clock']
w2_add = ['judgement', 'official', 'sufficient']
s3_add = ['per-cent']
s2_add = ['cell-phone', 'sufficient']


words_tests = [
    'difficult',
    "can",
]

START = 0
END = 500

WORDS_ERRORS_FILENAME = f"{LIST_FILENAME}-errors.txt"
WORDS_FILENAME = f"{LIST_FILENAME}.shlf"


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
    logging.info("-" * 40)
    logging.info("[{i}]----{word}".center(40))
    logging.info("-" * 40)

    # Simple Search
    try:
        oxford.search(word.lower())
        word_dict = oxford.formatted_data
    except Exception:
        # Advanced Search
        # Use only in words that were not found by the above method
        random_sleep()
        for ep in ENDPOINTS:
            try:
                print(f'\nSearching {word + ep}')
                oxford.search(word + ep)
                word_dict = oxford.formatted_data
            except Exception:
                print(f'\n{word + ep} not found')
                random_sleep()
                continue

            print(f'\nSaving Word: {word + ep}')
            word_dict['word'] = word_dict['word'][:len(word)]  # removes ep
            print(word_dict['word'])
            save_word_to_shelve(str(i) + str(ep), word_dict, WORDS_FILENAME)
            random_sleep()

        print('--------------\n')
        random_sleep()

        words_error.append(word)
        save_word_not_found(word)
        continue

    print("\nSaving Word")
    print('\nWriting on', i, 'key')
    save_word_to_shelve(i, word_dict, WORDS_FILENAME)

    print("--------------\n")
    random_sleep()

shelf = read_word_from_shelve(WORDS_FILENAME)

s1_longman = read_word_from_shelve('./dataset/s1_longman.shlf')
s2_longman = read_word_from_shelve('./dataset/s2_longman.shlf')
# shelf = read_word_from_shelve(WORDS_FILENAME)
# shelf = read_word_from_shelve(WORDS_FILENAME)
