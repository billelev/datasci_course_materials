import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
#print json.load(response)

#pyresponse = json.load(response)
#print pyresponse.keys()
#print pyresponse["results_per_page"]
#print pyresponse["results"]
#print type(pyresponse["results"])

#results = pyresponse["results"]
#print results.keys()
#print type(results[0])
#print results[0].keys()

#sText = results[2]["text"]
#print sText

#tPerPage = pyresponse["results_per_page"]

# Print out one page of results
#for iT in range(tPerPage):
#    print "Tweet " + str(iT+1) + ": " + results[iT]["text"]

#fname = 'stdout'
f = open('stdout', 'w')

# Print out two pages of results
for iP in range(10):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(iP+1))
    pyresponse = json.load(response)
    tPerPage = pyresponse["results_per_page"]
    results = pyresponse["results"]
    for iT in range(tPerPage):
        sOut = "Page " + str(iP + 1) + ", Tweet " + str(iT+1) + ": " + results[iT-1]["text"]
        #sOut2 = sOut.encode('ascii', 'xmlcharrefreplace') + "\n"
        sOut2 = sOut.encode('utf-8') + "\n"
        f.write(sOut2)
