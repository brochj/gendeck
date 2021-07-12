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
from fields import create_fields


def generate_id() -> int:
    return random.randrange(1 << 30, 1 << 31)


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
                fields=create_fields(word, definition, example),
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
