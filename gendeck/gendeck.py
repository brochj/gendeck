# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:40:11 2020

@author: broch
"""
# Dicionario
# http://www.mso.anu.edu.au/~ralph/OPTED/
import random

import genanki

from sqlite3_orm import SqliteORM
from data_formatter import DefinitionFormatter, ExampleFormatter, WordFormatter
from model import my_model


def generate_id() -> int:
    return random.randrange(1 << 30, 1 << 31)


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


def generate_note(data):
    pass


my_deck = genanki.Deck(generate_id(), "Longman")
sqlite = SqliteORM("longman_levels.db")
sqlite.connect()

words = sqlite.query_all_from_table("words")


for word_tuple in words[:3]:
    word = WordFormatter(word_tuple).create_dict()

    definitions = sqlite.query_definitions_by_word_id(word["id"])

    for def_tuple in definitions:
        definition = DefinitionFormatter(def_tuple).create_dict()

        examples = sqlite.query_examples_by_definition_id(definition["id"])

        for example_tuple in examples:
            example = ExampleFormatter(word["word"], example_tuple).create_dict()

            my_note = genanki.Note(
                model=my_model,
                fields=[
                    example["id"],
                    #
                    word["word"],
                    word["cefr"],
                    word["speaking"],
                    word["writing"],
                    word["word_type"],
                    word["ipa_nam"],
                    word["ipa_br"],
                    #
                    definition["definition"],
                    definition["cefr"],
                    definition["grammar"],
                    definition["def_type"],
                    definition["context"],
                    definition["labels"],
                    definition["variants"],
                    definition["use"],
                    definition["synonyms"],
                    #
                    example["example"],
                    example["context"],
                    example["labels"],
                    # convert_list_to_html_ul(definition["examples"]),
                    f"http://www.google.com/search?q={word['word']}&tbm=isch",
                    f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{word['word']}",
                    f"https://www.ldoceonline.com/dictionary/{word['word']}",
                    '<img src="Image_2.jpg">',
                    " ".join(
                        [
                            word["cefr"],
                            word["speaking"],
                            word["writing"],
                            word["word_type"],
                        ]
                    ),
                ],
                tags=[
                    word["cefr"],
                    word["speaking"],
                    word["writing"],
                    word["word_type"].replace(" ", "-"),
                ],
            )

            my_deck.add_note(my_note)

            my_package = genanki.Package(my_deck)

            my_package.media_files = ["images/a/a_2.jpg"]

            my_package.write_to_file("output.apkg")


sqlite.close()
