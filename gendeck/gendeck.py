# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:40:11 2020

@author: broch
"""
# Dicionario
# http://www.mso.anu.edu.au/~ralph/OPTED/
import sys

import genanki
import shelve

import random
from model import my_model

from sqlite3_orm import SqliteORM


def generate_id() -> int:
    return random.randrange(1 << 30, 1 << 31)


def convert_list_to_html_ul(word_list: list) -> str:
    """
    Parameters
    ----------
    word_list : LIST

        Example: ['a','b','c']

    Returns
    -------
    String:
        '<ul>
            <li>a</li>
            <li>b</li>
            <li>c</li>
        </ul>'

    """
    if not word_list:
        return ""
    new_list = [f"<li>{item}</li>" for item in word_list]
    ul = "<ul>" + "".join(new_list) + "</ul>"
    return ul


def format_definition(def_dict: dict) -> str:
    """
    Parameters
    ----------
    def_dict : DICT
        example: {
                'definition': str,
                'examples': list,
                'extra_examples': list
                'grammar': str,
                'labels': list
                ...
            }

    Returns
    -------
    f'{variants} {grammar} {use} {dis_g} {labels} {definition}'
    """
    variants = "".join(def_dict["variants"])
    definition = def_dict["definition"]
    grammar = "".join(def_dict["grammar"])
    use = "".join(def_dict["use"])
    dis_g = "".join(def_dict["dis_g"])
    labels = "".join(def_dict["labels"])
    def_word_level = "".join(def_dict["def_word_level"])
    return f"{def_word_level.upper()} {grammar} {use}{dis_g}{variants}{labels} {definition}"


def random_pick(example_list: list) -> object:
    if not example_list:
        return ""
    return random.choice(example_list)


def format_example(word: str, example: str) -> str:
    word = word.lower()
    capitalized_word = word.capitalize()
    example_words = example.split()
    formatted_example = []

    for w in example_words:
        if word in w:
            formatted_example.append(w.replace(word, "{{c1::" + word + "}}"))
        elif capitalized_word in w:
            formatted_example.append(
                w.replace(capitalized_word, "{{c1::" + capitalized_word + "}}")
            )
        else:
            formatted_example.append(w)

    return " ".join(formatted_example)


def pick_an_example(word: str, examples: list) -> str:
    example = random_pick(examples)
    formatted = format_example(word, example)
    return formatted


def generate_note(data):
    pass


my_deck = genanki.Deck(generate_id(), "Longman")
sqlite = SqliteORM("longman_levels.db")
sqlite.connect()

words = sqlite.query_all_from_table("words")


for word_tuple in words[:3]:
    word_id = word_tuple[0]
    word = word_tuple[1]

    definitions = sqlite.query_definitions_by_word_id(word_id)

    for def_tuple in definitions:
        definition_id = def_tuple[0]

        examples = sqlite.query_examples_by_definition_id(definition_id)

        for example_tuple in examples:
            example_id = example_tuple[0]

            my_note = genanki.Note(
                model=my_model,
                fields=[
                    str(example_id),
                    #
                    word_tuple[1],
                    word_tuple[2].upper(),
                    word_tuple[3],
                    word_tuple[4],
                    word_tuple[5],
                    word_tuple[6],
                    word_tuple[7],
                    #
                    def_tuple[1],
                    def_tuple[2].upper(),
                    def_tuple[3],
                    def_tuple[4],
                    def_tuple[5],
                    def_tuple[6],
                    def_tuple[7],
                    def_tuple[8],
                    def_tuple[9],
                    #
                    example_tuple[1],
                    example_tuple[2],
                    example_tuple[3],
                    # convert_list_to_html_ul(definition["examples"]),
                    f"http://www.google.com/search?q={word}&tbm=isch",
                    f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{word}",
                    f"https://www.ldoceonline.com/dictionary/{word}",
                    '<img src="Image_2.jpg">',
                    " ".join(
                        [
                            word_tuple[2].upper(),
                            word_tuple[3],
                            word_tuple[4],
                            word_tuple[5],
                        ]
                    ),
                ],
                tags=[
                    word_tuple[2].upper(),
                    word_tuple[3],
                    word_tuple[4],
                    word_tuple[5].replace(" ", "-"),
                ],
            )

            my_deck.add_note(my_note)

            my_package = genanki.Package(my_deck)

            my_package.media_files = ["images/a/a_2.jpg"]

            my_package.write_to_file("output.apkg")


sqlite.close()
# for i, word_def in enumerate(words_dict[:10]):
#     print("\n", i)

#     for key, definition in word_def["definitions"].items():
#         print("def", key, word_def["word"])
#         for word in words_list:
#             if word_def["word"] == word["word"]:

#                 example = pick_an_example(
#                     word["word"], definition["examples"] + definition["extra_examples"]
#                 )

#                 formatted_def = str(key + 1) + ". " + format_definition(definition)

#                 my_note = genanki.Note(
#                     model=my_model,
#                     fields=[
#                         word_def["word_level"].upper(),
#                         word["word"],
#                         example,
#                         formatted_def,
#                         word_def["ipa_nam"],
#                         word_def["ipa_br"],
#                         # word_def["word_level"].upper(),
#                         word_def["word_type"],
#                         " ".join(word["group"]),
#                         convert_list_to_html_ul(definition["examples"]),
#                         convert_list_to_html_ul(definition["extra_examples"]),
#                         f'http://www.google.com/search?q={word["word"]}&tbm=isch',
#                         f'https://www.oxfordlearnersdictionaries.com/us/definition/english/{word["word"]}',
#                         f'https://www.ldoceonline.com/dictionary/{word["word"]}',
#                         '<img src="Image_2.jpg">',
#                         " ".join(
#                             word["group"]
#                             + list(word_def["word_level"].upper().split())
#                             + word_def["word_type"].split()
#                         ),
#                     ],
#                     tags=word["group"]
#                     + list(word_def["word_level"].upper().split())
#                     + word_def["word_type"].split(),
#                 )

#                 my_deck.add_note(my_note)

#                 my_package = genanki.Package(my_deck)

#                 my_package.media_files = ["images/a/a_2.jpg"]

#                 my_package.write_to_file("output.apkg")
