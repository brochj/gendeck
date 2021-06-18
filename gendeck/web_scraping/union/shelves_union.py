# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 21:08:30 2020

@author: brochj
"""

import shelve
import copy


def save_to_shelve(key, value, filename):
    with shelve.open(filename) as shelf:
        shelf[str(key)] = copy.deepcopy(value)


def read_from_shelve(filename):
    shelve_list = []
    with shelve.open(filename) as shelf:
        key_list = list(shelf.keys())

        for key in key_list:
            value = shelf[key]
            shelve_list.append(value)

    return shelve_list


def remove_duplicated_values(filename):
    shelve_list = []
    with shelve.open(filename) as shelf:
        key_list = list(shelf.keys())

        for key in key_list:
            value = shelf[key]
            for k in list(shelf.keys()):
                if value == shelf[k] and k != key:
                    print(f'[{k}] ')
                    del shelf[k]
                    break
            else:
                continue
            break


FILENAME_1 = "s1_longman.shlf"
remove_duplicated_values(FILENAME_1)
shelf_1 = read_from_shelve(FILENAME_1)

while True:
    remove_duplicated_values(FILENAME_1)
    shelf_1 = read_from_shelve(FILENAME_1)



# %%
# united_list = []


# FILENAME_1 = "w3_add.shlf"
# FILENAME_2 = "w31_longman.shlf"


# shelf_1 = read_from_shelve(FILENAME_1)
# shelf_2 = read_from_shelve(FILENAME_2)

# united_list = shelf_1 + shelf_2

# for index, value in enumerate(united_list):
#     save_to_shelve(index, value, 'w3_longman.shlf')
