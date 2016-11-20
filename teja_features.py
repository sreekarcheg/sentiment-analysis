import nltk
from utility import loadLexicon, getPolarityClues
from nltk.parse.stanford import StanfordDependencyParser


filepath = 'dataset/lexicon/subjclueslen1-HLTEMNLP05.tff'
#lexicon = loadLexicon(filepath)

jarpath = 'stored/stanford-parser-full-2015-12-09/stanford-parser.jar'
modpath = 'stored/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
dep_parser = StanfordDependencyParser(path_to_jar=jarpath, path_to_models_jar=modpath)

def subjClues(sentence):
	'''Gets all subjectivity clues in a sentence.'''
	clues = getPolarityClues(sentence)
	strong = 0
	weak = 0
	for clue in clues:
		for w in clue:
			d = lexicon.get(w)
			if d is not None:
				if d['type'] == 'strongsubj':
					#print "Strong: %s"%w
					strong += 1
				elif d['type'] == 'weaksubj':
					#print "Weak: %s"%w
					weak += 1
	return strong, weak

def get_paths_bfs(dep):
	'''Returns the edge labels on the path from root to every node.'''
	start_node_addr = dep.get_by_address(0)['deps']['root'][0]
	q = [start_node_addr]
	paths = dict()
	paths[start_node_addr] = []
	while q:
		addr = q.pop(0)
		curr_path = paths[addr]
		node = dep.get_by_address(addr)
		edges = node['deps']
		
		for label in edges:
			edgelist = edges[label]
			for n in edgelist:
				if n in paths:
					raise Exception('Cycle in Dependency Tree!')
				paths[n] = curr_path + [label]
				q.append(n)
	return paths


def structFeatures(sentence):
	#Get the parse tree. 
	dep = dep_parser.raw_parse(sentence).next()
	paths = get_paths_bfs(dep)
	

