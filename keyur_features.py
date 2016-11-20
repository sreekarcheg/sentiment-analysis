import re
import nltk
from nltk.stem.snowball import SnowballStemmer

from utility import loadLexicon

def keyurFeatures(rawSentence):
	# TODO get a proper lexicon of intensifiers
	intensifiers = set([])
	with open('dataset/lexicon/intensifiers.txt','r') as intfile:
		for line in intfile:
			for word in line.split():
				intensifiers.add(word)
	rawSentence = nltk.word_tokenize(rawSentence)
	sentence = []
	for token in rawSentence:
		match = re.search(r'^[.,?!-()";:\']+$',token)
		if match==None:
			sentence.append(token)
	sentence = nltk.pos_tag(sentence)
	stemmer = SnowballStemmer("english")
	features = []
	lexicon = loadLexicon('dataset/lexicon/subjclueslen1-HLTEMNLP05.tff')
	for i in range(len(sentence)):
		feature = []
		# the word token and part of speech
		feature.append(stemmer.stem(sentence[i][0]))
		feature.append(sentence[i][1])
		# word context: before, this, after
		if i>0:
			feature.append(sentence[i-1][0])
		else:
			feature.append('')
		feature.append(sentence[i][0])
		if i<len(sentence)-1:
			feature.append(sentence[i+1][0])
		else:
			feature.append('')
		try:
			feature.append(lexicon[sentence[i][0]]['priorpolarity'])
		except KeyError:
			feature.append('none')
		try:
			feature.append(lexicon[sentence[i][0]]['type'])
		except KeyError:
			feature.append('none')
		if i>0:
			prevTag = sentence[i-1][1]
			# preceded by adjective
			if prevTag[0]=='J' and prevTag[1]=='J':
				feature.append(True)
			else:
				feature.append(False)
			# preceded by adverb other than not
			if prevTag[0]=='R' and prevTag[1]=='B' and sentence[i-1][0].lower()!='not':
				feature.append(True)
			else:
				feature.append(False)
			# preceded by intensifier
			if sentence[i-1][0].lower() in intensifiers:
				feature.append(True)
			else:
				feature.append(False)
		else:
			feature.append(False);feature.append(False);feature.append(False)
		# is intensifier
		if sentence[i][0].lower() in intensifiers:
			feature.append(True)
		else:
			feature.append(False)
		features.append(feature)
	return features
if __name__ == '__main__':

	passage = "I'm Rick Harrison, and this is my pawn shop. I work here with my old man and my son, Big Hoss. Everything in here has a story and a price. One thing I've learned after 21 years - you never know WHAT is gonna come through that door."
	features = keyurFeatures(passage)
	for f in features:
		print f
