import nltk
from utility import loadLexicon, getPolarityClues
from nltk.parse.stanford import StanfordDependencyParser
import os
import re
from nltk.internals import find_jars_within_path
from collections import defaultdict
from nltk.stem.snowball import SnowballStemmer

# Lexicon to get the priorpolarity for words.
filepath = 'dataset/lexicon/subjclueslen1-HLTEMNLP05.tff'
lexicon = loadLexicon(filepath)

jarpath = 'stored/stanford-parser-full-2015-12-09/stanford-parser.jar'
modpath = 'stored/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
dep_parser = StanfordDependencyParser(path_to_jar=jarpath, path_to_models_jar=modpath)

def getPriorPolarity(word):
	'''
	This function finds the priorpolarity of a given word.
	'''
	wordFeatures = lexicon.get(word)
	if wordFeatures is None:
		return "neutral"

	polarity = wordFeatures.get('priorpolarity')
	if polarity is None:
		return "neutral"
	
	return polarity

def getPolarityFeatures(rawSentence):
	dep = dep_parser.raw_parse(rawSentence).next()
	negation = set([])
	intensifiers = set([])
	generalShifters = set([])
	negativeShifters = set([])
	positiveShifters = set ([])
	with open('dataset/lexicon/negation.txt','r') as intfile:
		for line in intfile:
			for word in line.split():
				negation.add(word)
	intfile.close()
	with open('dataset/lexicon/intensifiers.txt','r') as intfile:
		for line in intfile:
			for word in line.split():
				intensifiers.add(word)
	intfile.close()
	with open('dataset/lexicon/generalShifters.txt','r') as intfile:
		for line in intfile:
			for word in line.split():
				generalShifters.add(word)
	intfile.close()
	with open('dataset/lexicon/negativeShifters.txt','r') as intfile:
		for line in intfile:
			for word in line.split():
				negativeShifters.add(word)
	intfile.close()
	with open('dataset/lexicon/positiveShifters.txt','r') as intfile:
		for line in intfile:
			for word in line.split():
				positiveShifters.add(word)
	intfile.close()
	rawSentence = nltk.word_tokenize(rawSentence)
	sentence = []
	for token in rawSentence:
		match = re.search(r'^[.,?!-()";:\']+$',token)
		if match==None:
			sentence.append(token)
	features = []
	for idx,word in enumerate(sentence):
		node = dep.get_by_address(idx+1)
		negated = False
		negatedSubject = False
		extra = False
		#1]. Negated: 1. Check for any negated word in the preceding 4 words of the word.
		for i in range(1,5):
			try:
				if sentence[idx-i] in negation and sentence[idx-i] not in intensifiers:
					negated = True
			except IndexError:
				extra = True
		#1]. Negated: 2. Check for negated word in any of the children of the word.
		children = node['deps']
		for child in children:
			child_node = dep.get_by_address(children[child][0])
			child_name = child_node['word']
			if child_name in negation and child_name not in intensifiers:
				negated = True
		#2]. Negated Subj:
		if node['rel'] == "nsubj":
			for child in children:
				child_node = dep.get_by_address(children[child][0])
				child_name = child_node['word']
				if child_name in negation and child_name not in intensifiers:
					negatedSubject = True
		# Features 3,4,5.	
		node = dep.get_by_address(idx+1)
		feature = []
		modifiesPolarity = "notmod"
		modifiedByPolarity = "notmod"
		conjugatePolarity = "notmod"
		# 3]. Check for and get Modifies polarity:
		# If parent of a word has the relation obj, mod, or vmod 
		# assign the modifiesPolarity of the word as the priorpolarity of the parent
		if (node['rel'] == "dobj") or (node['rel'] == "amod") or (node['rel'] == "nmod") or (node['rel'] == "vmod"):
			parent_address = node['head']
			parent_node = dep.get_by_address(parent_address)
			parent = parent_node['word']
			modifiesPolarity = getPriorPolarity(parent)

		# 4]. Check for and get Modified by polarity:
		# If a child of a word has the relation mod or vmod 
		# assign the modifiedByPolarity of the word as the priorpolarity of the child.
		children = node['deps']
		for child in children:
			if (child == "amod") or (child == "nmod") or (child == "vmod"):
				child_node = dep.get_by_address(children[child][0])
				child_name = child_node['word']
				modifiedByPolarity = getPriorPolarity(child_name)
				break

		# 5]. Check for and get conjugate polarity:
		# If the word has the relation conj with another word
		# assign the conjugatePolarity of the word as the priorpolarity of the other word
		if node['rel'] == "conj":
			parent_address = node['head']
			parent_node = dep.get_by_address(parent_address)
			parent = parent_node['word']
			conjugatePolarity = getPriorPolarity(parent)
		else:
			children = node['deps']
			for child in children:
				if child == "conj":
					child_node = dep.get_by_address(children[child][0])
					child_name = child_node['word']
					conjugatePolarity = getPriorPolarity(child_name)
					break
		# Features 6,7,8.
		generalBool = False
		positiveBool = False
		negativeBool = False
		extra = False
		for i in range(1,5):
			try:
				if sentence[idx-i] in positiveShifters:
					positiveBool = True
				if sentence[idx-i] in negativeShifters:
					negativeBool = True
				if sentence[idx-i] in generalShifters:
					generalBool = True
			except IndexError:
				extra = True
		feature = [negated, negatedSubject, modifiesPolarity, modifiedByPolarity, conjugatePolarity, generalBool, negativeBool, positiveBool]
		features.append(feature)
	return features

if __name__ == '__main__':

	passage = "I'm Rick Harrison, and this is my little pawn shop. I work here with my old man and my son, Big Hoss. Everything in here has a story and a price. There is never a lack of boredom. One thing I've learned after 21 years - you never know WHAT is gonna come through that door."
	features = getPolarityFeatures(passage)
	for f in features:
		print f