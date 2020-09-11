import sys
import csv
import operator

# Import CSV File, and initialize it
with open('weatherdataset.csv') as I:
    reader = csv.reader(I)
    fulllist = list(reader)

print ('CONVERTED WEATHER DATA SET\n')
print ("DATE " + ' '*6 + "TEMP (INPUT -> F)" + ' '*4 + "TEMP (C)" + ' '*7 +  "TEMP (F)" + ' '*6 + "\n" + '-'*58)

# Use this for loop to ignore the top line
for item in range(1, len(fulllist)): 
    # Print each row using "item" as the index value
    date = fulllist[item][0]
    tempInput = fulllist[item][2]
    temptoC = (((float(tempInput) - 32)*5)/9)
    temptoF = (1.8 * temptoC) + 32

    # Print formatted and converted data
    print ("{} {} {} {}".format(
        str(date).ljust(10),
        str(tempInput).ljust(20),
        str(round(temptoC, 2)).ljust(14),
        str(round(temptoF, 2)).ljust(14)
    ))
