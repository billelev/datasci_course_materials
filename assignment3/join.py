# join.py order_records.json
# join.py order_records2.json
# join.py order_records3.json

import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
    # key: orderid
    # value: tuple
	#print type(record)
	#data = json.loads(record, encoding='latin-1')
	data = record
	print str(type(data))
	key = data[1]

	mr.emit_intermediate(key, data)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(key, list_of_values):
    # key: orderid
    # value: list of tuples
    # output key, value
    for o in list_of_values :
        if o[0] == "order" :
			#print o[0]
			for l in list_of_values :
				if l[0] == "line_item" and o[1] == l[1]:
					#print o[0] + " " + l[0] + "\n"
					joinedList = o + l
					#print str(type(joinedList)) + " " + str(len(joinedList)) + "\n"
					for i in range(len(joinedList)):
						joinedList[i] = str(joinedList[i])
						#print str(type(joinedList[i]))
					#print str(len(joinedList))
					#list_of_values.remove(l)
					#print joinedList
					mr.emit(joinedList)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    # one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()

	
			
			
			
			
			
			
			
			
			
			
			