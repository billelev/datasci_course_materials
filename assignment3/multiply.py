# multiply.py matrix.json

import MapReduce
import json
import sys

mr = MapReduce.MapReduce()
BCOLS = 10
AROWS = 10

# Map function
# mr - MapReduce object
# data - json object formatted as a string
#def mapper(mr, record):
def mapper(record):
	# Record: [matrix, i, j, value]
    # key: matrix
    # value: i, j, value
	#data = json.loads(record, encoding='latin-1') # for local use
	data = record # for submitted results
				
	#print nucFull + " " + nucCrop + "\n"
	if data[0] == 'a':
		for k in range(BCOLS):
			key = (data[1], k)
			mr.emit_intermediate(key, data)
	else:
		for l in range(AROWS):
			key = (l, data[2])
			mr.emit_intermediate(key, data)
	
# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
#def reducer(mr, key, list_of_values):
def reducer(key, list_of_values):
    # key: column if matrix a, row if matrix b
    # list_of_values: [matrix, i, j, value]
    # output (i, j, value)

	k = key[1]
	total = 0
	for v in list_of_values:
		if v[0] == 'a':
			for v2 in list_of_values:
				if v2[0] == 'b' and v2[1] == v[2]:
					total += v[3] * v2[3]
	#if k == 3 and key[0] == 1:
	#	print list_of_values
					
	mr.emit((key[0], key[1], total))


def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    # one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()