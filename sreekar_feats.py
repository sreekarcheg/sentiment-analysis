import parseTree
import os
import sys
import pickle
import nltk.corpus, nltk.tag, itertools
from utility import loadLexicon, getPolarityClues

filepath = 'dataset/lexicon/subjclueslen1-HLTEMNLP05.tff'
lexicon = loadLexicon(filepath)
jarpath = 'stored/stanford-parser-full-2015-12-09/stanford-parser.jar' 
modpath = 'stored/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar' 
dep_parser = StanfordDependencyParser(path_to_jar=jarpath, path_to_models_jar=modpath)

def pos_tagger(sentence):
    filename = open("stored/ubt_tagger.classifier")
    words = nltk.word_tokenize(sentence)
    ubt_tagger = pickle.load(filename)
    return ubt_tagger.tag(words)

def numAdj(rawSentence):
    pos = pos_tagger(rawSentence)
    count = 0
    for tag in pos:
        if tag[1]=='JJ':
            count += 1
    return count

def numAdv_without_NOT(rawSentence):
    pos = pos_tagger(rawSentence)
    count = 0
    for tag in pos:
        if tag[1]=='RB':
            count += 1
    return count

def existsCardinal(rawSentence):
    pos = pos_tagger(rawSentence)
    for tag in pos:
        if tag[1] =='CD':
            return True
    return False

def existsPronoun(rawSentence):
    pos = pos_tagger(rawSentence)
    for tag in pos:
        if tag[1] =='PRP':
            return True
    return False    

def modalInSentence(rawSentence):
    '''Indicates if a modal other than will is present'''
    modals = ['may', 'might', 'must', 'can', 'could', 'shall', 'should', 'would']
    if any(modal in rawSentence for modal in modals):
        return True
    return False

def modifies_strongsubj(word, idx, rawSentence, dep):
    #If you find a way of not constructing the node tree over and over that would be great. Maybe pass dep as a parameter.
    dep = dep_parser.raw_parse(rawSentence).next()
    flag1, flag2 = False, False

    node = dep.get_by_address(idx)
    parent_address = node['head']
    parent_node = dep.get_by_address(parent_address)
    parent_word = parent_node['word']
    d = lexicon.get(parent_word)
    if d is not None:
        if d['type'] == 'strongsubj':
            flag1 = True

    parent_relationship = node['rel'] 
    if parent_relationship in ['JJ', 'adjmod', 'advmod', 'vmod']:
        flag2 = True
    return falg1 and flag2

def modifies_weaksubj(word, idx, rawSentence):
    #If you find a way of not constructing the node tree over and over that would be great. Maybe pass dep as a parameter.
    dep = dep_parser.raw_parse(rawSentence).next()
    flag1, flag2 = False, False

    node = dep.get_by_address(idx)
    parent_address = node['head']
    parent_node = dep.get_by_address(parent_address)
    parent_word = parent_node['word']
    d = lexicon.get(parent_word)
    if d is not None:
        if d['type'] == 'weaksubj':
            flag1 = True

    parent_relationship = node['rel'] 
    if parent_relationship in ['JJ', 'adjmod', 'advmod', 'vmod']:
        flag2 = True
    return falg1 and flag2

def modifiedBy_strongsubj(word, idx, rawSentence):
    #If you find a way of not constructing the node tree over and over that would be great. Maybe pass dep as a parameter.
    dep = dep_parser.raw_parse(rawSentence).next()
    flag1, flag2 = False, False

    node = dep.get_by_address(idx)
    parent_address = node['head']
    parent_node = dep.get_by_address(parent_address)
    parent_word = parent_node['word']
    d = lexicon.get(word)
    if d is not None:
        if d['type'] == 'strongsubj':
            flag1 = True

    children = node['deps'] 
    if children in ['JJ', 'adjmod', 'advmod', 'vmod']:
        flag2 = True
    return falg1 and flag2

def modifiedBy_weaksubj(word, idx, rawSentence):
    #If you find a way of not constructing the node tree over and over that would be great. Maybe pass dep as a parameter.
    dep = dep_parser.raw_parse(rawSentence).next()
    flag1, flag2 = False, False

    node = dep.get_by_address(idx)
    parent_address = node['head']
    parent_node = dep.get_by_address(parent_address)
    parent_word = parent_node['word']
    d = lexicon.get(word)
    if d is not None:
        if d['type'] == 'weaksubj':
            flag1 = True

    children = node['deps'] 
    if children in ['JJ', 'adjmod', 'advmod', 'vmod']:
        flag2 = True
    return falg1 and flag2


if __name__=="__main__":
    lexicon = parseTree.loadLexicon("/Users/apple/DBMSProject/dataset/lexicon/subjclueslen1-HLTEMNLP05.tff")
    print lexicon