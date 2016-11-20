import os
import sys
import pickle
import nltk.corpus, nltk.tag, itertools

def pos_tagger(sentence):
	filename = open("stored/ubt_tagger.classifier")
	words = nltk.word_tokenize(sentence)
	ubt_tagger = pickle.load(filename)
	return ubt_tagger.tag(words)


if __name__=="__main__":
	pos = pos_tagger("I am good boy")
	print pos