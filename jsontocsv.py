import json
import csv

# read the .json file into a list of dictionaries
# note that string dictionary keys will automatically be
#   converted to all lower case
with open('data_orig.json') as json_file:
    data = json.load(json_file)

# create a list of field names
keys = data[0].keys()

# write the field names to the .csv file
with open('data_out.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(keys)

# write each dictionary to the .csv file,
#   adding double quotes around all values
values = []
for n in range(len(data)):
    value = data[n].values()
    values.append(value)


csv.register_dialect('doublequotes', delimiter = ',', quotechar = '"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
with open('data_out.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, 'doublequotes')
    writer.writerows(values)