# -*- coding: utf-8 -*-
"""
################################################################
# Filename:     oxford.py
# Start Date:   Fri Dec 11 11:34:13 2020
# Last Update:  Jan 02, 2020
# Author:       Oscar Broch    Github: https://github.com/brochj
# Purpose:      Extract info from Oxford Learners Dictionaries
#
# ==============================================================
# DESCRIPTION
# - This script searches for a given word and returns all main
#   information about it.
# - Example:
#   - Word level: A1, A2, ...
#   - Word type: noun, verb, modal, ...
#   - Definitions:
#       - Def 1: ...
#       - Def 2: ...
#   ...
################################################################
"""

from bs4 import BeautifulSoup
import requests
import logging


class Oxford:
    def __init__(self) -> None:
        self.word = ""
        self.soup = None
        self.ipa_nam = ""
        self.ipa_br = ""
        self.word_type = ""
        self.word_level = ""
        logging.basicConfig(level=logging.NOTSET)

    def basic_search(self, word):
        self.word = word
        self.clear_attr()
        self.get_html()
        self.clear_collocations()
        self.get_ipa()
        self.get_word_type()
        self.get_word_level()

    def get_html(self):
        """
         Oxford Word Endpoints
        _1 , _2, 1_1, 1_2, 1_3, 1_4, 2_1, ...
        Examples: word_1, word1_1
        """
        logging.info('Searching...')
        url = f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{self.word}"
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text

        # Parse the html content
        self.soup = BeautifulSoup(html_content, "html.parser")

    def clear_extra_examples(self):
        try:
            extra_examples = self.soup.find_all("span", unbox="extra_examples")

            for extra_eg in extra_examples:
                extra_eg.clear()
        except AttributeError:
            logging.debug("Doesn't exist 'extra examples' or Can't clear 'extra examples'")
        try:
            self.soup.find("span", unbox="more_about").clear()  # more_about removed
        except AttributeError:
            logging.debug("Doesn't exist 'more_about' or Can't clear 'more_about'")
        try:
            self.soup.find("span", unbox="cult").clear()  # more_about removed
        except AttributeError:
            logging.debug("Doesn't exist 'culture' or Can't clear 'culture'")

    def clear_collocations(self):
        """
        Clears "Collocations" to extract the "labels" correctly.

        Because there are "labels" within these "Collocations"
        """
        try:
            collocations = self.soup.find_all("span", unbox="colloc")

            for colloc in collocations:
                colloc.clear()
        except AttributeError:
            logging.debug("Doesn't exist 'Collocations'")

    def get_ipa(self):
        try:
            self.ipa_nam = self.soup.find("div", class_="phons_n_am").text.strip()
            self.ipa_br = self.soup.find("div", class_="phons_br").text.strip()
        except AttributeError:
            logging.debug("Can't find ipa")

    def get_word_type(self):
        try:
            self.word_type = self.soup.find("span", class_="pos").text
        except AttributeError:
            logging.debug("Can't find word type")

    def get_word_level(self):
        try:
            level_html = self.soup.find("div", class_="symbols")
            link = level_html.contents[0].get("href")
            self.word_level = link[-2:]
        except AttributeError:
            logging.debug("Can't find word level")

    def clear_attr(self):
        self.ipa_nam = ""
        self.ipa_br = ""
        self.word_type = ""
        self.word_level = ""


class Definition(Oxford):
    def __init__(self, log_level=logging.WARNING):
        """

        Parameters
        ----------
        log_level : int, optional
            DESCRIPTION. The default is logging.WARNING.
            VALUES: logging.CRITICAL = 50
                    logging.ERROR    = 40
                    logging.WARNING  = 30
                    logging.INFO     = 20
                    logging.DEBUG    = 10

        Returns
        -------
        None.

        """
        super().__init__()
        self.definitions_li = []
        self.definitions = []
        self.variants = []
        self.use = []
        self.labels = []
        self.grammar = []
        self.dis_g = []
        self.def_word_level = []
        self.examples = []
        self.extra_examples = []
        self.synonyms = []
        self.formatted_data = {}
        logger = logging.getLogger()
        logger.setLevel(log_level)

    def clear_attributes(self):
        self.definitions_li = []
        self.definitions = []
        self.variants = []
        self.use = []
        self.labels = []
        self.grammar = []
        self.dis_g = []
        self.def_word_level = []
        self.examples = []
        self.extra_examples = []
        self.synonyms = []
        self.formatted_data = {}

    def search(self, word):
        self.word = word
        self.clear_attributes()
        self.basic_search(word)

        self.clear_collocations()
        self.get_definitions_li()
        self.get_definitions()
        self.get_extra_examples()
        self.get_examples()
        self.get_ipa()
        self.get_word_type()
        self.get_word_level()
        self.get_synonyms()
        self.get_variants()
        self.get_use()
        self.get_labels()
        self.get_grammar()
        self.get_dis_g()
        self.get_def_word_level()
        self.format_data()

    def get_definitions_li(self):
        try:
            definition_exists = True
            definitions_html = self.soup.find("ol", class_="sense_single")
            # Checking if it is Idioms Definitions, which we don't want
            if definitions_html.parent.name == "span":
                definitions_html = None
            self.definitions_li = definitions_html.find_all("li", class_="sense")
        except AttributeError:
            logging.warning("Can't find single definition")
            try:
                definition_exists = True
                definitions_html = self.soup.find("ol", class_="senses_multiple")
                self.definitions_li = definitions_html.find_all("li", class_="sense")
            except AttributeError:
                definition_exists = False
                logging.error("Can't find multiple definitions")

        if not definition_exists:
            raise Exception(f"Can't find the '{self.word}' definition")

    def get_definitions(self):
        try:
            for definition in self.definitions_li:
                def_text = definition.find("span", class_="def").text
                self.definitions.append(def_text)
        except AttributeError:
            logging.error("Can't find definition")

    def get_variants(self):
        for definition in self.definitions_li:
            try:
                variants_text = definition.find("div", class_="variants").text
                self.variants.append(variants_text)
            except AttributeError:
                self.variants.append([])

    def get_use(self):
        for definition in self.definitions_li:
            try:
                use_text = definition.find("span", class_="use").text
                self.use.append(use_text)
            except AttributeError:
                logging.debug("Can't find definition 'use'")
                self.use.append([])

    def get_labels(self):
        for definition in self.definitions_li:
            try:
                labels = definition.find("span", class_="labels").text
                self.labels.append(labels)
            except AttributeError:
                logging.debug("Can't find definition 'labels'")
                self.labels.append([])

    def get_grammar(self):
        for definition in self.definitions_li:
            try:
                grammar = definition.find("span", class_="grammar").text
                self.grammar.append(grammar)
            except AttributeError:
                logging.debug("Can't find definition grammar")
                self.grammar.append([])

    def get_dis_g(self):
        for definition in self.definitions_li:
            try:
                dis_g = definition.find("span", class_="dis-g").text
                self.dis_g.append(dis_g)
            except AttributeError:
                logging.debug("Can't find definition dis_g")
                self.dis_g.append([])

    def get_def_word_level(self):
        for definition in self.definitions_li:
            try:
                level_html = definition.find("div", class_="symbols")
                link = level_html.contents[0].get("href")
                self.def_word_level.append(link[-2:])
            except AttributeError:
                logging.debug("Can't find definition word level")
                self.def_word_level.append([])

    def get_examples(self):
        for definition in self.definitions_li:
            try:
                examples_ul = definition.find(
                    "ul", class_="examples", hclass="examples"
                )
                example_list = [ex.text for ex in examples_ul.find_all("li")]
                self.examples.append(example_list)
            except AttributeError:
                logging.debug("There is no examples for this definition")
                self.examples.append([])

    def get_extra_examples(self):
        for definition in self.definitions_li:
            try:
                extra_examples = definition.find("span", unbox="extra_examples")
                example_list = [ex.text for ex in extra_examples.find_all("li")]
                self.extra_examples.append(example_list)
            except AttributeError:
                logging.debug("There are no 'Extra Examples' for this definition")
                self.extra_examples.append([])
        self.clear_extra_examples()

    def get_synonyms(self):
        for definition in self.definitions_li:
            synonyms_type = "nsyn"  # syn or nsyn
            synonyms = definition.find("span", xt="nsyn")
            if synonyms is None:
                synonyms_type = "syn"
            try:
                synonyms = definition.find("span", xt=synonyms_type)
                synonym_list = [ex.text for ex in synonyms.find_all("a")]
                self.synonyms.append(synonym_list)
            except AttributeError:
                logging.debug("There are no 'synonyms' for this definition")
                self.synonyms.append([])

    def format_data(self):
        definitions_dict = {}
        for index, definition in enumerate(self.definitions):
            definitions_dict[index] = {
                "definition": definition,
                "examples": self.examples[index],
                "extra_examples": self.extra_examples[index],
                "synonyms": self.synonyms[index],
                "labels": self.labels[index],
                "grammar": self.grammar[index],
                "variants": self.variants[index],
                "use": self.use[index],
                "dis_g": self.dis_g[index],
                "def_word_level": self.def_word_level[index]
            }
        self.formatted_data = {
            "word": self.word,
            "ipa_nam": self.ipa_nam,
            "ipa_br": self.ipa_br,
            "word_type": self.word_type,
            "word_level": self.word_level,
            "definitions": definitions_dict,
        }


if __name__ == "__main__":

    test = Oxford()
    test.basic_search('car')
    # test_ipa_nam = test.ipa_nam
    # test_ipa_br = test.ipa_br
    # test_word_type = test.word_type
    # test_word_level = test.word_level

    word = Definition()

    word.search("umbrella")

    # # lists
    # word_definitions = word.definitions
    # word_dis_g = word.dis_g
    # word_examples = word.examples
    # word_extra_examples = word.extra_examples
    # word_grammar = word.grammar
    # word_labels = word.labels
    # word_synonyms = word.synonyms
    # word_use = word.use
    # word_variants = word.variants

    # # strings
    # word_ipa_nam = word.ipa_nam
    # word_ipa_br = word.ipa_br
    # word_word_type = word.word_type
    # word_word_level = word.word_level

    # # final dict
    word_formatted_data = word.formatted_data
