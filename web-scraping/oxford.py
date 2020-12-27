# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:34:13 2020

@author: broch
"""

from bs4 import BeautifulSoup
import requests


class Oxford:
    def __init__(self):
        self.word = ""
        self.soup = None

        self.definitions = []
        self.examples = []
        self.extra_examples = []
        self.synonyms = []
        self.ipa_nam = ""
        self.ipa_br = ""
        self.word_type = ""
        self.word_level = ""
        self.variants = []
        self.use = []
        self.labels = []
        self.grammar = []
        self.dis_g= []
        self.formatted_data = {}

        self.definitions_li = []

    def get_html(self):
        """
         Oxford Word Endpoints
        _1 , _2, 1_1, 1_2, 1_3, 1_4, 2_1
        Examples: word_1, word1_1

        """
        URL = f"https://www.oxfordlearnersdictionaries.com/us/definition/english/{self.word}"
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}).text

        # Parse the html content
        self.soup = BeautifulSoup(html_content, "html.parser")

    def search(self, word):
        self.word = word

        self.clear_attributes()

        self.get_html()
        
        
        self.clear_collocations()
        self.get_definitions_li()
        self.get_definitions()
        self.get_extra_examples()
        self.get_examples()
        self.get_ipa()
        self.get_ipa("br")
        self.get_word_type()
        self.get_word_level()
        self.get_synonyms()
        self.get_variants()
        self.get_use()
        self.get_labels()
        self.get_grammar()
        self.get_dis_g()
        self.format_data()


    def get_definitions_li(self):
        try:
            isThereDefinition = True
            definitions_html = self.soup.find("ol", class_="sense_single")
            #Checking if it is Idioms Definitions, which we don't want
            if definitions_html.parent.name == 'span': definitions_html = None 
            self.definitions_li = definitions_html.find_all("li", class_="sense")
        except AttributeError:
            print("Can't find single definition")
            try:
                isThereDefinition = True
                definitions_html = self.soup.find("ol", class_="senses_multiple")
                self.definitions_li = definitions_html.find_all("li", class_="sense")
            except:
                isThereDefinition = False
                print("Can't find multiple definitions")
            
        if not isThereDefinition : raise Exception(f"Can't find the '{self.word}' definition")


    def get_definitions(self):
        try:
            for definition in self.definitions_li:
                def_text = definition.find("span", class_="def").text
                self.definitions.append(def_text)
        except:
            print("Can't find definition")


    def get_variants(self):
        for definition in self.definitions_li:
            try:
                variants_text = definition.find("div", class_="variants").text
                self.variants.append(variants_text)
            except:
                # print("Can't find definition variants")
                self.variants.append([])
    
    
    def get_use(self):
        for definition in self.definitions_li:
            try:
                use_text = definition.find("span", class_="use").text
                self.use.append(use_text)
            except:
                # print("Can't find definition use")
                self.use.append([])
                

    def get_labels(self):
        for definition in self.definitions_li:
            try:
                labels = definition.find("span", class_="labels").text
                self.labels.append(labels)
            except:
                # print("Can't find definition labels")
                self.labels.append([])
    
    
    def get_grammar(self):
            for definition in self.definitions_li:
                try:
                    grammar = definition.find("span", class_="grammar").text
                    self.grammar.append(grammar)
                except:
                    # print("Can't find definition grammar")
                    self.grammar.append([])
    
    def get_dis_g(self):
            for definition in self.definitions_li:
                try:
                    dis_g = definition.find("span", class_="dis-g").text
                    self.dis_g.append(dis_g)
                except:
                    # print("Can't find definition dis_g")
                    self.dis_g.append([])


    def clear_extra_examples(self):
        try:
            extra_examples = self.soup.find_all("span", unbox="extra_examples")

            for extra_eg in extra_examples:
                extra_eg.clear()
        except AttributeError:
            print("Doesn't exist 'extra examples' or Can't clear 'extra examples'")
        try:
            self.soup.find("span", unbox="more_about").clear()  # more_about removed
        except AttributeError:
            print("Doesn't exist 'more_about' or Can't clear 'more_about'")
        try:
            self.soup.find("span", unbox="cult").clear()  # more_about removed
        except AttributeError:
            print("Doesn't exist 'culture' or Can't clear 'culture'")
            
    def clear_collocations(self):
        '''
        Limpa "Collocations" para extrair as "labels" de forma correta
        Pois existem "labels" dentro dessas "Collocations"
        '''
        try:
            collocations = self.soup.find_all("span", unbox="colloc")

            for colloc in collocations:
                colloc.clear()
        except AttributeError:
            print("Doesn't exist 'Collocations'")
        pass
        


    def get_examples(self):
        for definition in self.definitions_li:
            try:
                examples_ul = definition.find(
                    "ul", class_="examples", hclass="examples"
                )
                example_list = [ex.text for ex in examples_ul.find_all("li")]
                self.examples.append(example_list)
            except:
                # print("There is no examples for this definition")
                self.examples.append([])


    def get_extra_examples(self):
        for definition in self.definitions_li:
            try:
                extra_examples = definition.find("span", unbox="extra_examples")
                example_list = [ex.text for ex in extra_examples.find_all("li")]
                self.extra_examples.append(example_list)
            except:
                # print('There is no "Extra Examples" for this definition')
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
            except:
                self.synonyms.append([])


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
    
    def clear_attributes(self):
        self.definitions = []
        self.examples = []
        self.extra_examples = []
        self.synonyms = []
        self.ipa_nam = ""
        self.ipa_br = ""
        self.word_type = ""
        self.word_level = ""
        self.variants = []
        self.use = []
        self.labels = []
        self.grammar = []
        self.dis_g = []
        self.formatted_data = {}  
        self.definitions_li = []

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
                "use": self.use[index],
                "dis_g": self.dis_g[index]
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
    teste = Oxford()

    # teste.search("umbrella")
    teste.search("action")
    # synonym - palavra deliberately

    definitions = teste.definitions
    examples = teste.examples
    # nam = teste.ipa_nam
    # br = teste.ipa_br
    # word_type = teste.word_type
    # word_level = teste.word_level
    extra_examples = teste.extra_examples
    synonyms = teste.synonyms
    labels = teste.labels
    grammar = teste.grammar
    variants = teste.variants
    use = teste.use
    dis_g = teste.dis_g
    formatted_data = teste.formatted_data
    
# import itertools
# defs = ['def 1', 'def 2', 'def 3']
# var = ['var 1', 'var 2']

# for d , v in itertools.zip_longest(defs, var):
#     if v is None:
#         print (d)
#     else:

#         print (d + ' ' + v)
