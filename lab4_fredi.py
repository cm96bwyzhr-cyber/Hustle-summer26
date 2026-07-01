# fredi miranda | lab 4 | intro to python

# Ticket 1


ages = [13, 15, 25, 10,8]
for age in ages:
    if age >= 13:
        print(f"{age} - Acces granted")
    else:
        print(f"{age} - Too young")

    # the ages that would be granted would be 13, 15, 25 and 10, 8 will be not granted it will be too young
    # the age that you could be have acces to enter is 13 and up, but if you are lower like 10 it will not let you access the app.


    # Ticket 2

 
Keep_checking = "yes"

while Keep_checking == "yes":
    age = int(input("enter an age: "))

    if age >= 13: 
        print("Acces granted")
    else:
        print("too young")
        Keep_checking = input("check another age? (yes/no): ")
# If the user types "no" on the first check, the loop still runs once because keep_checking starts as "yes" and not with A no 
# A while loop is best because we do not know ahead of time are else something bad would happen.


# Ticket 3

while True:
    age = input("Enter an age or type 'stop': ")

    if age == "stop":
        break

    age = int(age)

    if age >= 13:
        print("Access granted ")
    else:
        print("Too young ")
# without a break, the loop would never finish.

# Ticket 2 uses a condition (keep_checking == "yes") to continue and not to finish.
# Ticket 3 runs forever until break is used to stop it.


# Ticket 4

def can_access(age):
    if age >= 13:
        return True
    else:
        return False

ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ")
    else:
        print(f"{age} — Too young ")
# The output is the same as Ticket 1, but the age-checking logic is now inside the can_access() function. Instead of writing the if age >= 13 check every time, the program calls the function to do the check.
# you can only write the code once.


# Ticekt 5


def can_access(age):
    return age >= 13

def signup_report(ages):
    print("--- StreamPass Signup Report ---")

    approved = 0

    for number, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ")

    print(f"Approved: {approved} out of {len(ages)}")

signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)
# The expected output is shown above. There are 4 approved out of 6 signups because the ages 22, 15, 19, and 13 are all 13 or older.
#I used the functions, parameters, a list, a for loop with enumerate(), if/else statements, a counter variable (approved), len() to count the total signups, and f-strings to format the output.
