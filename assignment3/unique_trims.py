# asymmetric_friendships.py asymmetric_friendships.json
# asymmetric_friendships.py symmetric_friendships.json

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
    # value: PersonB
	#data = json.loads(record, encoding='latin-1')
	data = record
	#print data[0]
	#print str(record)
	sort = sorted(data)
	key = sort[0] + "," + sort[1]
	#print str(type(key))
	#print key
	mr.emit_intermediate(key, 1)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    # key: as a string: sorted(PersonA, PersonB)
    # value: Count of sorted(PersonA, PersonB)
    # output key, value
	#print "Yay \n"
	if len(list_of_values) == 1:
		person = key.split(",")
		personA = person[0]
		personB = person[1]
		mr.emit((personA, personB))
		mr.emit((personB, personA))


def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    # one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()