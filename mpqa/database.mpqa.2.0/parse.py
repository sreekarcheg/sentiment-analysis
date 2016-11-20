import os
import cPickle as pickle

#Gets data and pickles it. Assumes it is sitting in the directory of the dataset.

def getSentences(filePath, txt):
    '''Returns a dict which sentence starting point and sentence.'''
    boundaries = os.path.join('man_anns', filePath, 'gatesentences.mpqa.2.0')

    starts = []
    ends = []
    sentences = dict()

    with open(boundaries, 'r') as f:
        b = f.readlines()
        for line in b:
            bs = map(int, line.split()[1].split(','))
            starts.append(bs[0])
            ends.append(bs[1])
            sentences[txt[bs[0]:bs[1]]] = set()
    return sorted(starts), sorted(ends), sentences

def getPolarities(filePath):
    '''Takes a file path of the kind '20010627/23.46.20-17835', and returns
    a list of sentences, annotated with polarity clues and their polarities.'''
    txt = None
    with open(os.path.join('docs', filePath), 'r') as f:
        txt = f.read(-1) #Read everything.
    #print txt

    starts, ends, sentences = getSentences(filePath, txt)
    print starts
    sents = sentences.keys()

    with open(os.path.join('man_anns', filePath, 'gateman.mpqa.lre.2.0'), 'r') as f:
        for line in f:
            if (not line.startswith('#')) and 'polarity' in line:
                anns = line.split()
                bs = map(int, anns[1].split(','))
                #Get the sentence in which the indicator exists.
                i = 0
                while (ends[i] < bs[0]):
                    i += 1
                sent = txt[starts[i]:ends[i]]
                #Get the polarity.
                pol = [a for a in anns if 'polarity' in a][0][len('polarity="'):-1]
                #print sent, ':', pol

                #Add it to the relevant sentence.
                phrase = txt[bs[0]:bs[1]]
                sentences[sent].add((phrase, pol))

    #print sentences
    print '\n\n---------------\n\n'
    return sentences

def getAllPolarities():
    sentences = {}
    for d in os.listdir('docs'):
        filePath = os.path.join('docs', d)
        filePath = os.listdir(filePath)[0]
        filePath = os.path.join(d, filePath)
        print 'FilePath:', filePath
        tmp = getPolarities(filePath)
        for t in tmp:
            if tmp[t]:
                sentences[t] = tmp[t]
    return sentences

if __name__ == '__main__':
    print '\n\n'
    s = getAllPolarities()
    with open('../polarities.pkl', 'wb') as f:
        pickle.dump(s, f)






