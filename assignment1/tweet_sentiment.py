# $ python tweet_sentiment.py <sentiment_file> <tweet_file>
# $ python tweet_sentiment.py AFINN-111.txt output_first20.txt
# set PYTHONPATH=%PYTHONPATH%;C:\Users\BCUNLIFFE\Documents\GitHub\datasci_course_materials\assignment1
# tweet_file = open("output_first20.txt")

import sys
import json

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
    print str(length)
    return (length)
	
def getTweet_original(line):
	punc = ("\",./;'?&-#@")
	txt1 = line.split(",")[3]
	txt2 = txt1.split(":")[1]
	#txt1 = json.loads(line)
	#txt2 = str(txt1['text'])
	txt3 = " " + txt2.replace("#", "")
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
	# tweet_file = open("output_first20.txt")
    lines = tweet_file.readlines()
    #nSentiment = printLines(sent_file)
	#nTweets = printLines(tweet_file)
    buildDictionary(sys.argv[1])
    term = scores.keys()
    #print (scores)
    #f = open('stdout', 'w')
	# For each tweet, loop through dictionary, sum up score of each
    # term in dictionary that appears in tweet
    for line in lines:
		# only process tweets that have not been deleted
		if line[1:10] != "\"delete\":" :
			totScore = 0
			out = ""
			txt = getTweet(line)
			#print txt
			# ==== Method 1
			#for i in range(0,len(term)-1):
			#	if txt.lower().find(term[i].lower()) != -1:
			#		totScore = totScore + scores[term[i]]
			#		out = out + " " + term[i]
			# ==== Method 2
			tokens = tokenize(txt)
			for i in range(len(tokens)):
				if tokens[i] in term:
					totScore = totScore + scores[tokens[i]]
					if len(out) == 0:
						out = tokens[i]
					else:
						out = out + " " + tokens[i]
			#if totScore != 0:
			#	print out + ": (" + str(totScore) + ") === " + txt 
			#f.write(str(totScore) + "\n")
			print totScore
			
			
if __name__ == '__main__':
    main()

	
