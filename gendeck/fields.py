def create_tags(word: dict) -> str:
    return " ".join(
        [
            word["cefr"],
            word["speaking"],
            word["writing"],
            word["word_type"],
        ]
    )


def create_google_img_url(word: str) -> str:
    return f"http://www.google.com/search?q={word}&tbm=isch"


def create_oxford_url(word: str) -> str:
    return f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{word}"


def create_longman_url(word: str) -> str:
    return f"https://www.ldoceonline.com/dictionary/{word}"


def create_fields(word: dict, definition: dict, example: dict) -> list:
    return [
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
        create_google_img_url(word["word"]),
        create_oxford_url(word["word"]),
        create_longman_url(word["word"]),
        "",  # '<img src="Image_2.jpg">',
        create_tags(word),
    ]
