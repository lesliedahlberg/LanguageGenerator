import tkinter
import random
from tkinter import *


class SymbolCollections:
    __collection_list = {}

    def add(self, symbols, symbol_type):
        self.__collection_list[symbol_type] = symbols

    def get(self, symbol_type):
        symbols = self.__collection_list[symbol_type]
        n_symbols = len(symbols)
        symbol_index = random.randrange(0, n_symbols)
        return symbols[symbol_index]


class Syllables:
    def __init__(self, structures, symbols):
        self.__structures = structures
        self.__symbols = symbols

    def generate(self):
        n_structures = len(self.__structures)
        structure_index = random.randrange(0, n_structures)
        structure = self.__structures[structure_index]
        r_syllable = ""
        for symbolType in structure:
            r_syllable += self.__symbols.get(symbolType)
        return r_syllable


class Word:
    def __init__(self, syllables):
        self.__syllables = syllables

    def generate(self, n_syllables):
        word = ""
        for i in range(0, n_syllables):
            word += self.__syllables.generate()
        return word


class Sentence:
    def __init__(self, word):
        self.__word = word

    def generate(self, n_words):
        sentence = ""
        for i in range(0, n_words):
            n_syllables = random.randrange(1, 5)
            sentence += self.__word.generate(n_syllables)
            if i < n_words - 1:
                sentence += ' '
            else:
                sentence += '. '
        return sentence.capitalize()


class Paragraph:
    def __init__(self, sentence):
        self.__sentence = sentence

    def generate(self, n_sentences):
        paragraph = ""
        for i in range(0, n_sentences):
            n_words = random.randrange(5, 20)
            paragraph += self.__sentence.generate(n_words)
        return paragraph


class Document:
    def __init__(self, paragraph):
        self.__paragraph = paragraph

    def generate(self, n_paragraphs):
        document = ""
        for i in range(0, n_paragraphs):
            n_sentences = random.randrange(5, 20)
            document += self.__paragraph.generate(n_sentences)
            if i < n_paragraphs-1:
                document += "\n\n"
        return document


def generate_callback():
    try:
        n = int(n_paragraphs.get())
        text.insert(tkinter.INSERT, document.generate(n))
    except ValueError:
        print("Not a number!")


def clear_callback():
    text.delete("0.1", tkinter.END)


vowel_list = ['a', 'e', 'i', 'u', 'o', 'ä', 'å', 'ö']
consonant_list = ['r', 't', 'p', 's', 'd', 'h', 'j', 'k', 'l', 'v', 'n', 'm']

symbol = SymbolCollections()
symbol.add(vowel_list, 'V')
symbol.add(consonant_list, 'C')

structure = ['CVVV', 'CVV', 'CV']
syllable = Syllables(structure, symbol)

word = Word(syllable)

sentence = Sentence(word)
paragraph = Paragraph(sentence)

document = Document(paragraph)

top = tkinter.Tk()

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

m2 = PanedWindow(orient=HORIZONTAL)
m2.pack(fill=BOTH, expand=1)

generate = tkinter.Button(top, text="Generate Text", command=generate_callback)
clear = tkinter.Button(top, text="Clear Text", command=clear_callback)
n_paragraphs_label = tkinter.Label(top, text="Number of Paragraphs")
n_paragraphs = tkinter.Entry(top)
text = tkinter.Text(top)

m2.add(n_paragraphs_label)
m2.add(n_paragraphs)
m2.add(generate)
m2.add(clear)

m.add(m2)
m.add(text)

top.mainloop()




