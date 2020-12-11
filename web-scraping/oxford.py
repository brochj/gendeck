# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:34:13 2020

@author: broch
"""

from bs4 import BeautifulSoup
import requests
import time

WORDS = ['umbrella'] 


URL=f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{WORDS[0]}"

# URL=f"https://www.google.com/search?q={WORDS[0]}"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(URL,headers={"User-Agent":"Mozilla/5.0"}).text

# Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')


def get_definitions(_soup):
    
    definitions_htmls = _soup.find_all("span", class_="def")
    definitions = []
    
    for definition in definitions_htmls:
        definitions.append(definition.text)
    return definitions


def get_examples(_soup):
    examples_html = _soup.find_all("ul", class_="examples", hclass="examples")
    examples = []
    
    for example_ul in examples_html:
        example_list = [ex.text for ex in example_ul.find_all('li')]
        examples.append(example_list)
    return examples
      

def get_ipa(_soup, phon="nam"):
    ipa_nam = _soup.find("div", class_="phons_n_am").text
    ipa_br = _soup.find("div", class_="phons_br").text
    
    return ipa_nam if phon=="nam" else ipa_br

def get_word_type(_soup):
    return _soup.find("span", class_="pos").text


def get_word_level(_soup):
    level_html = _soup.find("div", class_="symbols")
    link = level_html.contents[0].get('href')
    level = link[-2:]
    return level


# definitions = get_definitions(soup)
# examples = get_examples(soup)
# nam = get_ipa(soup)
# br = get_ipa(soup, 'br')
# word_type = get_word_type(soup)

word_level = get_word_level(soup)





