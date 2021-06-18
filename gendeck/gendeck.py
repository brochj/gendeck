# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:40:11 2020

@author: broch
"""
# Dicionario
# http://www.mso.anu.edu.au/~ralph/OPTED/

import genanki
import shelve

import random


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
                "definitions": word[1],
                "ipa_nam": word[2],
                "ipa_br": word[3],
                "word_type": word[4],
                "word_level": word[5].strip(), # strip to remove \n
            }
        )
    file.close()
    return formatted_word_list

def read_word_from_shelve(filename):
    words_list = []
    shelf = shelve.open(filename)
    key_list = list(shelf.keys())

    for key in key_list:
        word_data = shelf[key]
        words_list.append(word_data)

    shelf.close()
    return words_list


words_list = load_words_list("s1.txt")
# words_dict = load_words_dict("word_dict.txt")
words_dict = read_word_from_shelve("dict/s1_longman.shlf")
#%%
# model_id = random.randrange(1 << 30, 1 << 31)
# deck_id = random.randrange(1 << 30, 1 << 31)

my_model = genanki.Model(
    1962161376,
    "Cloze wordlist",
    fields=[
        {"name": "English Level"},
        {"name": "Word"},
        {"name": "Example"},
        {"name": "Definition"},
        # # {'name': 'id'},
        {"name": "IPA NAm"},
        {"name": "IPA Br"},
        # {"name": "English Level"},
        {"name": "Word Type"},
        {"name": "Word Group"},
        # # {'name': 'Audio_word'},
        {"name": "Examples"},
        {"name": "Extra_examples"},
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


# words = [
#     {"word": "water", "definition": "liquid", "tags": ["tag1", "tag2"]},
#     {"word": "fire", "definition": "hot", "tags": ["tag1", "tag2"]},
# ]

my_deck = genanki.Deck(2106080373, "Longman")


def convert_list_to_html_ul(word_list: list) -> str:
    '''
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

    '''
    if not word_list: return ''
    new_list = [f'<li>{item}</li>' for item in word_list]
    ul = '<ul>' + ''.join(new_list) + '</ul>'
    return ul



def format_definition(def_dict: dict) -> str:
    """
    Parameters
    ----------
    def_dict : DICT
        Example: {
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
    variants = ''.join(def_dict['variants']) # Tenho que rodar o Cralwer de novo para ter o variants
    definition = def_dict['definition']
    grammar = ''.join(def_dict['grammar'])
    use = ''.join(def_dict['use'])
    dis_g = ''.join(def_dict['dis_g'])
    labels = ''.join(def_dict['labels'])
    def_word_level = ''.join(def_dict['def_word_level'])
    return f'{def_word_level.upper()} {grammar} {use}{dis_g}{variants}{labels} {definition}'

def random_pick(example_list: list) -> object:
    if not example_list : return ''
    return random.choice(example_list)

#%%
def format_example(word: str, example: str) -> str:
    word = word.lower()
    capitalized_word = word.capitalize()
    example_words = example.split()
    formatted_example = []

    for w in example_words:
        if word in w:
            formatted_example.append(w.replace(word, "{{c1::" + word + "}}"))
        elif capitalized_word in w:
            formatted_example.append(w.replace(capitalized_word, "{{c1::" + capitalized_word + "}}"))
        else:
            formatted_example.append(w)

    return ' '.join(formatted_example)


# c = format_example('account','She works in Accounts (= the accounts department).')
# print(c)
#%%

def pick_an_example(word: str, examples: list) -> str:
    example = random_pick(examples)
    formatted = format_example(word, example)
    return formatted




for i, word_def in enumerate(words_dict[:10]):
    print('\n',i)

    for key, definition in word_def['definitions'].items():
        print('def', key, word_def['word'])
        for word in words_list:
            if word_def["word"] == word["word"]:

                example = pick_an_example(word["word"],definition["examples"]+definition["extra_examples"])

                formatted_def = str(key + 1) + '. ' + format_definition(definition)

                my_note = genanki.Note(
                    model=my_model,
                    fields=[
                        word_def["word_level"].upper(),
                        word["word"],
                        example,
                        formatted_def,
                        word_def["ipa_nam"],
                        word_def["ipa_br"],
                        # word_def["word_level"].upper(),
                        word_def["word_type"],
                        " ".join(word["group"]),
                        convert_list_to_html_ul(definition["examples"]),
                        convert_list_to_html_ul(definition["extra_examples"]),
                        f'http://www.google.com/search?q={word["word"]}&tbm=isch',
                        f'https://www.oxfordlearnersdictionaries.com/us/definition/english/{word["word"]}',
                        f'https://www.ldoceonline.com/dictionary/{word["word"]}',
                        '<img src="Image_2.jpg">',
                        " ".join(
                            word["group"] +
                            list(word_def["word_level"].upper().split())
                            + word_def["word_type"].split()
                        ),
                    ],
                    tags=
                    word["group"] +
                    list(word_def["word_level"].upper().split())
                    + word_def["word_type"].split(),
                )

                my_deck.add_note(my_note)

                my_package = genanki.Package(my_deck)

                my_package.media_files = ["images/a/a_2.jpg"]

                my_package.write_to_file("output.apkg")



# for word_def in words_dict[:5]:
#     for word in words_list:
#         if word_def["word"] == word["word"]:
#             print(word)
#             my_note = genanki.Note(
#                 model=my_model,
#                 fields=[
#                     word["word"],
#                     word_def["example"].replace(
#                         word["word"], "{{c1::" + word["word"] + "}}"
#                     ),
#                     word_def["definition"],
#                     word_def["ipa_nam"],
#                     word_def["ipa_br"],
#                     word_def["word_level"].upper(),
#                     word_def["word_type"],
#                     " ".join(word["group"]),
#                     f'http://www.google.com/search?q={word["word"]}&tbm=isch',
#                     f'https://www.oxfordlearnersdictionaries.com/us/definition/english/{word["word"]}',
#                     f'https://www.ldoceonline.com/dictionary/{word["word"]}',
#                     '<img src="Image_2.jpg">',
#                     " ".join(
#                         word["group"]
#                         + list(word_def["word_level"].upper().split())
#                         + word_def["word_type"].split()
#                     ),
#                 ],
#                 tags=word["group"]
#                 + list(word_def["word_level"].upper().split())
#                 + word_def["word_type"].split(),
#             )

#             my_deck.add_note(my_note)

#             my_package = genanki.Package(my_deck)

#             my_package.media_files = ["images/a/a_2.jpg"]

#             my_package.write_to_file("output.apkg")
