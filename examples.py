# if
if 5 > 4:
    print("5 is greater than 4")


x = 45
x = x/2

# x = 22.5
if x > 30:
    print("NUH UH") # does not trigger
elif x > 25:
    print("second cond")
else:
    print("x is not that")

# result: 54
print("5" + " 4")
# result: 9
print(5 + 4)

name = input("enter name: ")
print(name)

name = int(input("enter name: "))

if name == "marius":
    print("logged in")


cool_number = 1

# != does not equal

while cool_number < 10:
    cool_number += 1
    print(cool_number)

numbers = [1,2,3]

sum = 0

for i in numbers:
    print(f"adding {i} to {sum}")
    sum += i


print("The sum is", sum)

# basic parity checker (parity checking means even or odd)

if number % 2 == 0:
    print("Even")
else:
    print("odd")


# lists

# define a list

list1 = [12, 3, 6]
empty_list = []

# adding a new value

list1.append(36)
# resulting list = [12, 3, 6, 36]

# position of an item
list1[1] # <-- this would be the SECOND number in a list
# WEIRD
# zero indexed list :thumbs_up:
print(list1[3]) #36
