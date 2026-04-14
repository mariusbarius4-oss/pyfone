CORRECT_PASSWORD = "marius"
attempted_password = input("enter password: ")

while attempted_password != CORRECT_PASSWORD:
    print("incorrect")
    attempted_password = input("enter password: ")

print("correct password")