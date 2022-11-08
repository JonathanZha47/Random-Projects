# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:57:18 2019

@author: Jonathan Zha

"""
#Final Project

#Partner's name: Jialin Yu
#Partner's email:jialinyu@bu.edu

def clean_test(txt):
    '''returns a list containing the words in txt after it has been “cleaned”
    '''
    txt = txt.lower()
    txt = txt.replace(',','')
    txt = txt.replace('.','')
    txt = txt.replace('?','')
    txt = txt.replace('!','')
    txt = txt.replace(':','')
    txt = txt.replace(';','')
    txt = txt.split()

    return txt
    
    
class TextModel:
    '''quantify how similar one piece of text is to another
    '''
    def __init__(self, model_name):
        '''constructs a new TextModel object
        '''
        self.name = model_name
        self.words = {} # a dictiionary that records the number of times each word appears in the text
        self.word_lengths = {} # a dictionary that records the number of times each word length appears
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word length: ' + str(len(self.word_lengths))
        return s
    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """
        word_list = clean_test(s)
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!

        # Template for updating the words dictionary.
        for w in word_list:
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        # Add code to update other feature dictionaries.
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
    def add_file(self, filename):
        '''adds all of the text in the file identified by filename to the model
        '''
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()      # read it all in at once!
        f.close()
        self.add_string(text)
    def save_model(self):
        """A function that demonstrates how to write a
           Python dictionary to an easily-readable file.
        """
        f = open(self.name + '_' + self.words, 'r')
        f.write(str(self.words))
        f.close()
        
        x = open()