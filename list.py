# goal
#
# create a new list with only the even numbers from a mixed list
# the base list is provided below
# the output must be printed without user input

# target output: [12, 62, 2]
#import time

baseList = [12, 53, 62, 1, 55, 2]
newList = []
for i in baseList:
    
    if i % 2 == 0:
        newList.append(i)

print(newList)