import numpy as np

file1 = open('sayajireviews.txt', 'r')
Lines = file1.readlines()
my_dict={}
count = 0
sumc=0;
# Strips the newline character
for line in Lines:
    review=line
    arr=review.split(":")
    my_dict[arr[0]]=arr[1]
    vv=float(arr[1].rstrip())
    sumc=sumc+vv


print(sumc)


sumc = sumc / 100



if sumc < 0.3:
    stars = 1
else:

    if sumc <= 0.5:
        stars = 2
    else:
        if sumc <= 1.5:
            stars = 3
        else:
            if sumc <= 2.5:
                stars = 4
            else:
                if sumc > 2.5:
                    stars = 5;


print("stars",stars)
keys = list(my_dict.keys())
values = list(my_dict.values())
sorted_value_index = np.argsort(values)[::-1]
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)