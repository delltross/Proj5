import csv
import json

# read the .csv file into a "reader" object
# each reader row is a list of string fields
fileObj = open('data.csv')
reader = csv.reader(fileObj)
print("reader: ", reader)

# put each reader row (a list) into a list
entrylist = []
for row in reader:
    entrylist.append(row)


fields = entrylist[0]
keys = []
# get the field names from the first list row
for n in range(len(fields)):
    keys.append(fields[n])


# create the object to send to the .json output file
# the object is a Python list of dictionaries
# the 1st dictionary contains the field names
outlist = []
for n in range(len(entrylist)):
    outlist.append({})
    for i in range(len(entrylist[n])):
        key = keys[i]
        outlist[n][str(key)] = entrylist[n][i]

# write the final list to a .json file
fileObj = open('data_out.json', 'w')
json.dump(outlist, fileObj, indent=2)
fileObj.close()
