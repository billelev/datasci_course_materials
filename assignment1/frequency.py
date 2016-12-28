# $ python frequency.py <tweet_file>
# frequency.py output_first20.txt

import sys
import json

terms = {}

stopWords = {'a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your'}

def getLines(fp):
    length = len(fp.readlines())
    #print str(length)
    return (length)

def bValidTweet(line):
	if line[1:10] != "\"delete\":" :
		return (True)
	else:
		return (False)
	
def getJSON(line):
	return json.loads(line)
	
def getTweet(line):
	punc = ("\",./;'?&-#@\:")
	txt1 = getJSON(line)
	txt2 = txt1['text']
	txt3 = txt2.encode('utf-8')
	txt4 = txt3.lower()
	txt5 = txt4.translate(None, punc)
	return (txt5)

def tokenize(txt):
	tokens = txt.split()
	return(tokens)
	
def main():
    #tweet_file = open(sys.argv[1])
	# tweet_file = open('output_first20.txt')
    #nLines = getLines(tweet_file)
    #print str(nLines)
    #for i in range(nLines):
    count = 0
    with open(sys.argv[1]) as f:
	#with open('output_first20.txt') as f:
		#print str(i)
		#line = tweet_file.readline()
		for line in f:
			#line = f.readline()
			if bValidTweet(line):
				txt = getTweet(line)
				tokens = tokenize(txt)
				for t in range(len(tokens)):
					if (tokens[t] in terms):
						terms[tokens[t]] += 1
					else:
						terms[tokens[t]] = 1
					count += 1
	
    freq = {}
    cumsum = float(0)
    for i in range(len(terms)):
		freq[terms.keys()[i]] = float(terms[terms.keys()[i]]) / float(count)
		cumsum += freq[terms.keys()[i]]
		
    if round(cumsum, 6) == 1.0:
		for i in range(len(freq)):
			print freq.keys()[i] + " " + str(freq[freq.keys()[i]])
				
			
if __name__ == '__main__':
    main()
