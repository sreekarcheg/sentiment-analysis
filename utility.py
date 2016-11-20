import nltk
import sys
import bllipparser

parser = bllipparser.RerankingParser.fetch_and_load('WSJ-PTB3', verbose=True)

def parseDoc(document):
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
'''
def nounChunking(sentence, debug = False):
	grammar = "NP: {<DT>?<JJ>*<NN>}"
	cp = nltk.RegexParser(grammar)
	result = cp.parse(sentence)
	if debug:
		print result
		result.draw()
	return result
'''

def getAdjAdvPhrases(tree):
    '''Gets all adjective and adverb phrases.'''
    adjp = []
    advp = []
    for child in tree:
        print child, child.label
        if child.label == 'ADJP':
            adjp.append(child.tokens())
        elif child.label == 'ADVP':
            advp.append(child.tokens())
        else:
            aj, av = getAdjAdvPhrases(child)
            adjp += aj
            advp += av

    return adjp, advp

def getPolarityClues(parser, sentence):
    rankedTrees = parser.parse(sentence)
    best_tree = rankedTrees[0].ptb_parse
    advP, adjP = getAdjAdvPhrases(best_tree[0])
    return advP + adjP

def loadLexicon(filePath):
    """
        Loads the annotated corpus and extracts the structure
        with easy access.
    """
    dictionary_file = open(filePath, "r")
    lines = dictionary_file.readlines()
    words = {}
    for line in lines:
        attributes = line.split(" ")
        for index,attr in enumerate(attributes):
            if attr.find('word1') > -1:
                word_value = attr.split("=")[1]
                attributes[index] = []
                break
        if word_value in words:
            for attr in attributes:
                if attr != []:
                    arr = attr.split("=")
                    key = arr[0]
                    if key == "pos1":
                        pos = words[word_value][key]
                        words[word_value][key].append(arr[1])
                        break
        else:
            words[word_value] = {}
            for attr in attributes:
                if attr != []:
                    arr = attr.split("=")
                    key = arr[0]
                    if len(arr) > 1:
                        value = arr[1]
                    if key == "pos1":
                        words[word_value][key] = [value.replace("\n", "")]
                    else:
                        words[word_value][key] = value.replace("\n", "")
    return words
