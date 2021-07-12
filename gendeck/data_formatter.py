class WordFormatter:
    def __init__(self, item: tuple):
        self.item = item

    def create_dict(self) -> dict:
        return {
            "id": self.item[0],
            "word": self.item[1],
            "cefr": self.item[2].upper(),
            "speaking": self.item[3],
            "writing": self.item[4],
            "word_type": self.item[5],
            "ipa_nam": self.item[6],
            "ipa_br": self.item[7],
        }


class DefinitionFormatter:
    def __init__(self, item: tuple):
        self.item = item

    def create_dict(self) -> dict:
        return {
            "id": self.item[0],
            "definition": self.item[1],
            "cefr": self.item[2].upper(),
            "grammar": self.item[3],
            "def_type": self.item[4],
            "context": self.item[5],
            "labels": self.item[6],
            "variants": self.item[7],
            "use": self.item[8],
            "synonyms": self.item[9],
            "word_id": self.item[10],
        }


class ExampleFormatter:
    def __init__(self, word: str, item: tuple):
        self.word = word
        self.item = item
        self.example: str = item[1]
        self.context: str = item[2]
        self.labels: str = item[3]

        self.formatted_example = self.format_example()

    def format_example(self) -> str:
        word = self.word.lower()
        capitalized_word = self.word.capitalize()
        example_words = self.example.split()
        formatted_sentence = []

        for w in example_words:
            if word == w:
                formatted_sentence.append(self.add_cloze_command(w, word))
            elif capitalized_word == w:
                formatted_sentence.append(self.add_cloze_command(w, capitalized_word))
            else:
                formatted_sentence.append(w)

        return " ".join(formatted_sentence)

    def add_cloze_command(self, example_word: str, word: str) -> str:
        return example_word.replace(word, "{{c1::" + word + "}}")

    def create_tuple(self) -> tuple:
        return (
            str(self.item[0]),
            self.formatted_example,
            self.item[2],
            self.item[3],
            self.item[4],
            self.item[5],
        )

    def create_dict(self) -> dict:
        return {
            "id": str(self.item[0]),
            "example": self.formatted_example,
            "context": self.item[2],
            "labels": self.item[3],
            "definition_id": self.item[4],
            "word_id": self.item[5],
        }
