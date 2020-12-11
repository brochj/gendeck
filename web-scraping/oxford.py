# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:34:13 2020

@author: broch
"""

from bs4 import BeautifulSoup
import requests


class Oxford:
    def __init__(self, word):
        self.word = word
        self.soup = None
        self.get_html()

        self.definitions = []
        self.examples = []
        self.ipa_nam = ""
        self.ipa_br = ""
        self.word_type = ""
        self.word_level = ""

        self.get_definitions()
        self.get_examples()
        self.get_ipa()
        self.get_ipa("br")
        self.get_word_type()
        self.get_word_level()

    def get_html(self):
        URL = f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{self.word}"
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text

        # Parse the html content
        self.soup = BeautifulSoup(html_content, "html.parser")

    def get_definitions(self):
        try:
            definitions_html = self.soup.find("ol", class_="senses_multiple")
            definitions_li = definitions_html.find_all("span", class_="def")

            for definition in definitions_li:
                self.definitions.append(definition.text)
        except:
            print("Can't find definitions")

    def clear_extra_examples(self):
        try:
            self.soup.find(
                "span", unbox="extra_examples"
            ).clear()  # extra_examples_removed
        except:
            print("Doesn't exist 'extra examples or Can't clear 'extra examples'")

    def get_examples(self):
        try:
            self.clear_extra_examples()
            definitions_html = self.soup.find("ol", class_="senses_multiple")
            examples_html = definitions_html.find_all(
                "ul", class_="examples", hclass="examples"
            )

            for example_ul in examples_html:
                example_list = [ex.text for ex in example_ul.find_all("li")]
                self.examples.append(example_list)
        except:
            print("Can't find examples")

    def get_extra_examples():
        return

    def get_ipa(self, phon="nam"):
        try:
            self.ipa_nam = self.soup.find("div", class_="phons_n_am").text.strip()
            self.ipa_br = self.soup.find("div", class_="phons_br").text.strip()
        except:
            print("Can't find ipa")

    def get_word_type(self):
        try:
            self.word_type = self.soup.find("span", class_="pos").text
        except:
            print("Can't find word type")

    def get_word_level(self):
        try:
            level_html = self.soup.find("div", class_="symbols")
            link = level_html.contents[0].get("href")
            self.word_level = link[-2:]
        except:
            print("Can't find word level")

    def get_idioms(self):
        # TODO
        idioms_html = self.soup.find("div", class_="idioms")
        print(idioms_html)
        print(len(idioms_html))
        # examples_html = idioms_html.find_all("ol", class_="examples", hclass="examples")

        return idioms_html


if __name__ == "__main__":
    teste = Oxford("name")

    definitions = teste.definitions
    examples = teste.examples
    nam = teste.ipa_nam
    br = teste.ipa_br
    word_type = teste.word_type
    word_level = teste.word_level
