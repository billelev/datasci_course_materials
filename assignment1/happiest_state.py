# $ python happiest_state.py <sentiment_file> <tweet_file>
# $ python happiest_state.py AFINN-111.txt output.txt #output_first20.txt

import sys
import json
import operator


# create global variable
scores = {} # initialize an empty dictionary
states = {}
term = {}

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
	
#  
def main():

    sent_file = open(sys.argv[1])
	# tweet_file = open("output_first20.txt")
    buildDictionary(sys.argv[1])
    term = scores.keys()

    with open(sys.argv[2]) as f:
	#with open('output_first20.txt') as f:
		for line in f:
			# only process tweets that have not been deleted
			if bValidTweet(line) :
				tObj = getJSON(line)
				#print tObj
				if ('place' in tObj.keys()):
					pObj = tObj['place']
					if not (pObj == None) and ('country_code' in pObj.keys()):
						#print "==== PLACE ==== " 
						#print tObj['place']
						if pObj['country_code'] == "US":
							if 'user' in tObj.keys():
								uObj = tObj['user'] 
								#print "==== USER ==== " 
								#print uObj['location'].encode('utf-8')
								#print str('location' in uObj.keys()) and not (uObj['location'] == None)
								if ('location' in uObj.keys()) and (not (uObj['location'] == None)) and (len(uObj['location'])>0):
									loc = uObj['location']
									#print "==== LOCATION ==== " 
									#print loc.encode('utf-8')
									vState = loc.split(",")
									if len(vState) == 1:
										st = vState[0].replace(" ", "")
									else:
										st = vState[1].replace(" ", "")
									st = st.upper()
									st = st.encode('utf-8')
									st = st[0:2]
									#print " == " + st.encode('utf-8')
									#print "==== STATE ==== "
									#print st.encode('utf-8')
									txt = getTweet(line)
									#print "==== TWEET ==== "
									#print txt
									tokens = tokenize(txt)
									totScore = 0
									for i in range(len(tokens)):
										if tokens[i] in term:
										    #print tokens[i]
										    totScore += scores[tokens[i]]

									#print "==== SCORE ==== "
									#print totScore
									if st in states:
										states[st] += totScore
									else:
										states[st] = totScore
										
    high_score_state = max(states.iteritems(), key=operator.itemgetter(1))[0]
    #for i in range(len(states)):
	#	print states.keys()[i] + " " + str(states[states.keys()[i]])
	#print states
    print high_score_state
			
			
if __name__ == '__main__':
    main()
