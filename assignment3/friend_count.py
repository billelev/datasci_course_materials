# friend_count.py symmetric_friendships.json

import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
	# Record: (PersonA, PersonB)
    # key: PersonA
    # value: Friend Count (1)
	#data = json.loads(record, encoding='latin-1')
	data = record
	#print data[0]
	#print str(record)
	personA = data[0]
	mr.emit_intermediate(personA, 1)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    # key: PersonA
    # value: List of occurance counts (1,1,1,1,...)
    # output key, value
	total = 0
	for v in list_of_values:
		total += v
	mr.emit((key, total))

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    # one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()