import numpy as np
import ast
import csv
#Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
#   # Define the header row of the CSV file
   fieldnames = ['Reviews', 'ratings']

#   # Create a CSV writer object
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#   # Write the header row
   writer.writeheader()

#ffile = open("abc.csv", "w")
file1 = open('keysreviews.txt', 'r')

Lines = file1.readlines()
my_dict={}
count = 0
# Strips the newline character
for line in Lines:
    review=line
    arr=review.split(":")
    key=arr[0].replace(' ] [','')
    my_dict[key]=(arr[1].rstrip())
    #print(review)

keys = list(my_dict.keys())
values = list(my_dict.values())


sorted_value_index = np.argsort(values)[::-1]
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)
with open('test.csv', 'w') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))




