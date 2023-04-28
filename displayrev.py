import numpy as np
import ast
import csv

file1 = open('keysreviews.txt', 'r' ,encoding='UTF-8')

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
with open('static/js/test.csv', 'w',encoding='UTF-8') as f:
    for key in sorted_dict.keys():
        f.write("%s,%s\n"%(key,sorted_dict[key]))




