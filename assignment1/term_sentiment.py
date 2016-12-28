# $ python term_sentiment.py <sentiment_file> <tweet_file>
# <term:string> <sentiment:float> = foo 103.256
# term_sentiment.py AFINN-111.txt output_first20.txt

import sys
import json

# create global variable
scores = {} # initialize an empty dictionary
newTerms = {}
#newTerms['friend'] = 0
#newTerms['trying'] = 0

def buildDictionary(fp):
    afinnfile = open(fp)
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items()
	
def getTweet_original(line):
	punc = ("\",./;'?&-#@")
	txt1 = line.split(",")[3]
	txt2 = txt1.split(":")[1]
	txt3 = txt2.replace("#", "")
	txt4 = txt3.lower()
	txt5 = txt4.translate(None, punc)
	return (txt5)
	
def getTweet(line):
	punc = ("\",./;'?&-#@\:")
	txt1 = json.loads(line)
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

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
	# tweet_file = open('output_first20.txt')
    lines = tweet_file.readlines()
    buildDictionary(sys.argv[1])
    term = scores.keys()
    k = 0
	
    for line in lines:
		
		k = k + 1
		
		# only process tweets that have not been deleted
		if line[1:10] != "\"delete\":" :
			
			totScore = 0
			out = ""
			txt = getTweet(line)
			#print str(k) + ": " + txt
			tokens = tokenize(txt)
			
			for i in range(len(tokens)):
				#print tokens[i]
				if tokens[i] in term:
					totScore = totScore + scores[tokens[i]]
					if len(out) == 0:
						out = tokens[i]
					else:
						out = out + " " + tokens[i]
				else:
					# Store the other words in the new dicitonary
					if not (tokens[i] in newTerms):
						#print tokens[i]
						newTerms[tokens[i]] = 0
			
			#print str(k) + ": Total Score ==== " + str(totScore)
            
			#if totScore != 0:
			#	print out + ": (" + str(totScore) + ") === " + txt 
			
			# Loop through tokens that DO NOT appear in sentiment dictionary
			# and assign a score to the terms
			for i in range(len(tokens)):
				if tokens[i] in newTerms:
					newTerms[tokens[i]] = newTerms[tokens[i]] + totScore
			
    for i in range(len(newTerms)):
		print newTerms.keys()[i] + " " + str(float(newTerms[newTerms.keys()[i]]))
		
			
if __name__ == '__main__':
    main()
