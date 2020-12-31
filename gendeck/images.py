# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:16:41 2020

@author: broch
"""


from bing_image_downloader import downloader


def load_words_list(filename):
    file = open(f"words_lists/{filename}", "r")
    words_list = file.read().split()
    formatted_word_list = []
    if "," in words_list[0]:

        for word in words_list:
            word = word.replace(",", "[", 1)
            index = word.find(",S")
            word = word[:index] + "]" + word[index + 1 :]

            word_values = {
                "word": word[: word.find("[")],
                "type": word[word.find("[") + 1 : word.find("]")],
                "group": word[word.find("]") + 1 :].split(","),
            }

            formatted_word_list.append(word_values)
        words_list = [word[: word.find(",")] for word in words_list if "," in word]
    file.close()
    return formatted_word_list


words = load_words_list("s1.txt")

query_string = "dog"

filters = "+filterui:imagesize-medium+filterui:photo-photo+filterui:aspect-wide&form=IRFLTR&first=1"
filters = "+filterui:photo-clipart+filterui:imagesize-medium&form=IRFLTR&first=1&tsc=ImageBasicHover"

for w in words[:100]:

    downloader.download(
        w["word"],
        limit=5,
        output_dir="images",
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        filters=filters,
    )
