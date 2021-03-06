# unique_trims.py dna.json

import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
#def mapper(mr, record):
def mapper(record):
	# Record: (sequence id, nucleotides)
    # key: PersonA
    # value: PersonB
	#data = json.loads(record, encoding='latin-1') # for local use
	data = record # for submitted results
	
	#print data[1]
	#print str(record)
	
	nucFull = data[1]
	#print nucFull
	nucCrop = nucFull[0:(len(nucFull)-10)]
	#print nucFull + " " + nucCrop + "\n"
	mr.emit_intermediate(nucCrop, data[0])

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
#def reducer(mr, key, list_of_values):
def reducer(key, list_of_values):
    # key: cropped nucleotide
    # value: list of sequence id's
    # output key, value
	#print "Yay \n"
	mr.emit(key)


def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    # one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()