# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:40:11 2020

@author: broch
"""
# Dicionario
# http://www.mso.anu.edu.au/~ralph/OPTED/

import genanki
import ast

# import random


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


def load_words_dict(filename):
    file = open(f"dict/{filename}", "r", encoding="utf8")
    words_dict = file.readlines()
    formatted_word_list = []

    for word in words_dict:
        word = word.split("|")

        formatted_word_list.append(
            {
                "word": word[0],
                "definition": word[1],
                "example": word[2],
                "ipa_nam": word[3],
                "ipa_br": word[4],
                "word_type": word[5],
                "word_level": word[6].strip(),
            }
        )
    file.close()
    return formatted_word_list


words_list = load_words_list("s1.txt")
words_dict = load_words_dict("words_200.txt")

# model_id = random.randrange(1 << 30, 1 << 31)
# deck_id = random.randrange(1 << 30, 1 << 31)

my_model = genanki.Model(
    1962161376,
    "Cloze wordlist",
    fields=[
        {"name": "Word"},
        {"name": "Example"},
        {"name": "Definition"},
        # # {'name': 'id'},
        {"name": "IPA NAm"},
        {"name": "IPA Br"},
        {"name": "English Level"},
        {"name": "Word Type"},
        {"name": "Word Group"},
        # # {'name': 'Audio_word'},
        {"name": "Google_images"},
        {"name": "Dict_link"},
        {"name": "Longman_link"},
        {"name": "Image"},
        {"name": "Tags"},
    ],
    templates=[
        {
            "name": "Card",
            "qfmt": "{{cloze::Example}}<br/><br/><b>Def:</b> {{Definition}}<br/><br/>{{Image}}",
            "afmt": '{{cloze::Example}}<br/><br/><b>Def:</b> {{Definition}}<br/><br/>{{Image}}<hr id="answer"><word>{{Word}}</word> <sub><i>{{Word Type}}</i></sub><br/><b>{{IPA NAm}}</b><br/><br/>Oxford Level: <level>{{English Level}}</level><br/>Longman Group: <wordgroup>{{Word Group}}</wordgroup><br/><br/><a href="{{Dict_link}}" class="oxfordButton">Oxford Dictionary</a><a href="{{Longman_link}}" class="longmanButton">Longman Dictionary</a><a href="{{Google_images}}" class="googleButton">Google Images</a>',
        },
    ],
    css=".card{font-family: arial;font-size: 20px;text-align: center;color: #000;background-color: #fff}.cloze{font-weight: 700;color: #00f}word{font-weight: 700;color: #00f}level{font-weight: 700;color: #1e90ff}.oxfordButton{background: linear-gradient(to bottom, #3d94f6 5%, #1e62d0 100%);background-color: #3d94f6;border-radius: 6px;border: 1px solid #094793;display: inline-block;cursor: pointer;color: #fff;font-family: Arial;font-size: 15px;font-weight: 700;padding: 6px 24px;text-decoration: none;margin:10px}.oxfordButton:hover{background: linear-gradient(to bottom, #1e62d0 5%, #3d94f6 100%);background-color: #1e62d0}.oxfordButton:active{position: relative;top: 1px}.longmanButton{background:linear-gradient(to bottom, #3d94f6 5%, #314089 100%);background-color:#3d94f6;border-radius:6px;border: 1px solid #094793;display:inline-block;cursor:pointer;color:#ffffff;font-family:Arial;font-size:15px;font-weight:bold;padding:6px 24px;text-decoration:none;margin:10px}.longmanButton:hover{background:linear-gradient(to bottom, #314089 5%, #3d94f6 100%);background-color:#314089}.longmanButton:active{position:relative;top:1px}.googleButton{background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);background-color:#f9f9f9;border-radius:6px;border:1px solid #dcdcdc;display:inline-block;cursor:pointer;color:#666666;font-family:Arial;font-size:15px;font-weight:bold;padding:6px 24px;text-decoration:none;margin:10px}.googleButton:hover{background:linear-gradient(to bottom, #e9e9e9 5%, #f9f9f9 100%);background-color:#e9e9e9}.googleButton:active{position:relative;top:1px}img{max-width:400px;height:auto;border-radius: 20px}wordgroup{font-weight: 700;color: #F1431E}",
)


words = [
    {"word": "water", "definition": "liquid", "tags": ["tag1", "tag2"]},
    {"word": "fire", "definition": "hot", "tags": ["tag1", "tag2"]},
]

my_deck = genanki.Deck(2106080373, "Longman")

for word_def in words_dict:
    for word in words_list:
        if word_def["word"] == word["word"]:
            print(word)
            my_note = genanki.Note(
                model=my_model,
                fields=[
                    word["word"],
                    word_def["example"].replace(
                        word["word"], "{{c1::" + word["word"] + "}}"
                    ),
                    word_def["definition"],
                    word_def["ipa_nam"],
                    word_def["ipa_br"],
                    word_def["word_level"].upper(),
                    word_def["word_type"],
                    " ".join(word["group"]),
                    f'http://www.google.com/search?q={word["word"]}&tbm=isch',
                    f'https://www.oxfordlearnersdictionaries.com/us/definition/english/{word["word"]}',
                    f'https://www.ldoceonline.com/dictionary/{word["word"]}',
                    '<img src="Image_2.jpg">',
                    " ".join(
                        word["group"]
                        + list(word_def["word_level"].upper().split())
                        + word_def["word_type"].split()
                    ),
                ],
                tags=word["group"]
                + list(word_def["word_level"].upper().split())
                + word_def["word_type"].split(),
            )

            my_deck.add_note(my_note)

            my_package = genanki.Package(my_deck)

            my_package.media_files = ["images/dog/Image_2.jpg"]

            my_package.write_to_file("output.apkg")
