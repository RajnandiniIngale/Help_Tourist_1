import numpy as np

file1 = open('keysreviews.txt', 'r')
Lines = file1.readlines()
my_dict={}
count = 0
# Strips the newline character
for line in Lines:
    review=line
    arr=review.split(":")
    my_dict[arr[0]]=arr[1]
    #print(review)

keys = list(my_dict.keys())
values = list(my_dict.values())
sorted_value_index = np.argsort(values)[::-1]
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)