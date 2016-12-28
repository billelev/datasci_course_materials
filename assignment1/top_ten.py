# $ python top_ten.py <tweet_file>
# $ python top_ten.py output_first20.txt output.txt #output_first20.txt

import sys
import json
import re


# create global variable
scores = {} # initialize an empty dictionary


def buildDictionary(fp):
    afinnfile = open(fp)
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items()

# Number of lines in the files 
def printLines(fp):
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
	punc = ("\",./;'?&-@\:")
	txt1 = getJSON(line)
	txt2 = txt1['text']
	txt3 = txt2.encode('utf-8')
	txt4 = txt3.lower()
	txt5 = txt4.translate(None, punc)
	return (txt5)
	
def tokenize(txt):
	tokens = txt.split()
	return(tokens)
	
#  
def main():

    tags = {}
    with open(sys.argv[1]) as f:
	#with open('output_first20.txt') as f:
		for line in f:
			# only process tweets that have not been deleted
			if bValidTweet(line):
				tObj = getJSON(line)
				ent = tObj['entities']
				ht = ent['hashtags']
				#  re.findall(pattern, string, flags=0)
				#ht =  re.findall(r"#(\w+)", txt)
				if len(ht) > 0:
					#print ht
					#print type(ht)
					for i in range(len(ht)):
						tag = ht[i]['text']
						#print tag
						if tag in tags:
							tags[tag] += 1
						else:
							tags[tag] = 1
    #for i in range(len(tags)):
	#	print tags.keys()[i] + " " + str(tags[tags.keys()[i]])
    tags_sorted = sorted(tags.keys(), key=tags.__getitem__, reverse=True)
    #print tags_sorted
    rng = min(len(tags_sorted), 10)
    for i in range(rng):
		print tags_sorted[i] + " " + str(float(tags[tags_sorted[i]]))
	
			
			
if __name__ == '__main__':
    main()
