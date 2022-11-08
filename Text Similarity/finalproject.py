#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:21:56 2019

@author: Yiwei Zha
"""
# finalproject.py


# partner's name: Jialin Yu
# Partner's email: jialinyu@bu.edu

import math
    
def clean_text(txt):
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
    

def stem(s):
    """ return the stem of s. The stem of a word is the root part of the word, which excludes any prefixes and suffixes. """
    
    if len(s) <= 4:
        return s
    
    elif s[-3:] == 'ing':
        if s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        if s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-1] == 'y':
        s = s[:-1]+'i'
    elif s[-2:] == 'es':
        if s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-1] == 's' and s != "Is" and s != 'is':
        s = s[:-1]
    elif s[-2:] == 'ed':
        if s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-1] == 'e' and s != 'the' and s!= 'The':
        s = s[:-1]
    elif s[-4:] == 'ment':
        s = s[:-4]
    elif s[-4:] == 'ship' and s != 'ship':
        s = s[:-4]
    elif s[-4:] == 'able'and s != 'able':
        s = s[:-4]
    elif s[-3:] == 'ful':
        s = s[:-3]
    elif s[-2:] == 'al':
        s = s[:-2]
    elif s[-2:] == 'ly':
        s = s[:-2]
    elif s[-3:] == 'ers':
        s = s[:-3]
        
    return s


def compare_dictionaries(d1, d2):
    '''take two feature dictionaries d1 and d2 as inputs, and it should 
        compute and return their log similarity score
    '''
    score = 0
    total = 0
    for i in d1:
        total += d1[i]
        
    for i in d2:
        if i in d1:
            score += d2[i] * math.log(d1[i]/total)
        elif i not in d1:
            score += d2[i] * math.log(0.5/total)
    return score


class TextModel:
    '''quantify how similar one piece of text is to another
    '''
    def __init__(self, model_name):
        '''constructs a new TextModel object
        '''
        self.name = model_name
        self.words = {} # a dictiionary that records the number of times each word appears in the text
        self.word_lengths = {} # a dictionary that records the number of times each word length appears
        self.stems = {}
        self.sentence_lengths= {}
        self.adj_words = {}
        
        
    def __repr__(self):
        """Return a string representation of the TextModel."""
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of sequence of adjacent words: ' + str(len(self.adj_words))
        return s
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model.
        """
        s1 = s.lower()
        s1 = s1.replace('?','.')
        s1 = s1.replace('!','.')
        s2 = s1.split('.')
        for i in s2:
            if i != '':
                x = i.split()
                if len(x) not in self.sentence_lengths:
                    self.sentence_lengths[len(x)] = 1
                else:
                    self.sentence_lengths[len(x)] += 1

        for i in s2:
            if i != '':
                x = i.split()
                for y in range(len(x)-1):

                    if stem(x[y]) + ' ' + stem(x[y+1]) not in self.adj_words:
                        self.adj_words[stem(x[y]) + ' ' + stem(x[y+1])] = 1
                    else:
                        self.adj_words[stem(x[y]) + ' ' + stem(x[y+1])] += 1

        word_list = clean_text(s)
        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of the functions you have already written!

        # Template for updating the words dictionary.
        for w in word_list:
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.
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
                
        for w in word_list:
            w = stem(w)
            w = stem(w)
            if w not in self.stems:
                self.stems[w] = 1
            else:
                self.stems[w] += 1
                
                
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
        
        f = open(str(self.name + '_words'), 'w')      # Open file for writing.
        f.write(str(self.words))              # Writes the dictionary to the file.
           
        f.close()                    # Close the file.
        
        x = open(str(self.name + '_word_lengths'), 'w')
        x.write(str(self.word_lengths))
        
        x.close()
        
        y = open(str(self.name + '_stems'), 'w')
        y.write(str(self.stems))
        
        y.close()
        
        z = open(str(self.name + '_sentence_lengths'), 'w')
        z.write(str(self.sentence_lengths))
        
        z.close()
        
        u = open(str(self.name + '_adj_words'), 'w')
        u.write(str(self.adj_words))
        
        u.close()
    
    def read_model(self):
        """A function that demonstrates how to read a
        Python dictionary from a file.
        """
        f = open(str(self.name + '_words'), 'r')     # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()
        self.words = dict(eval(d_str))      # Convert the string to a dictionary.
        
        x = open(str(self.name + '_word_lengths'), 'r')
        y_str = x.read()
        x.close()
        self.word_lengths = dict(eval(y_str))
        
        q = open(str(self.name + '_stems'), 'r')
        w_str = q.read()
        q.close()
        self.stems = dict(eval(w_str))
        
        e = open(str(self.name + '_sentence_lengths'), 'r')
        r_str = e.read()
        e.close()
        self.sentence_lengths = dict(eval(r_str))
        
        y = open(str(self.name + '_adj_words'), 'r')
        u_str = y.read()
        y.close()
        self.adj_words = dict(eval(u_str))
        
    def similarity_scores(self, other):
        '''returns a list of log similarity scores measuring the similarity 
            of self and other
        '''
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        adj_words_score = compare_dictionaries(other.adj_words, self.adj_words)
        return [word_score, word_lengths_score, stems_score, sentence_lengths_score, adj_words_score]

        
    def classify(self, source1, source2):
        '''compares the called TextModel object (self) to two other “source” 
        TextModel objects (source1 and source2) and determines which of these other
        TextModels is the more likely source of the called TextModel
        '''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ', source1.name,': ',scores1)
        print('scores for ', source2.name,': ',scores2)
        x= 0
        y= 0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                x += 1
            elif scores1[i] < scores2[i]:
                y += 1
        if x > y:
            print(self.name,' is more likely to have come from ',source1.name)
        else:
            print(self.name,' is more likely to have come from ',source2.name)
        
def test():
    """ one function that you can use to test your TextModel implementation """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)


def run_tests():
    """ function that compare different texts """
    source1 = TextModel('Financial Times')
    source1.add_file('Financial_Times_source_text.txt')

    source2 = TextModel('New York Times')
    source2.add_file('New_York_Times_source_text.txt')

    new1 = TextModel('wr100')
    new1.add_file('wr100_source_text.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('Boston Globe')
    new2.add_file('Boston_Globe_source_text.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('Part New York Times')
    new3.add_file('Part_New_York_Times_source_text.txt')
    new3.classify(source1,source2)
    
    new4 = TextModel('Part Financial Times')
    new4.add_file('Part_Financial_Times_source_text.txt')
    new4.classify(source1,source2)
    


