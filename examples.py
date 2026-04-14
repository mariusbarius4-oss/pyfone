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