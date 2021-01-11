"""
Write A Python Program(WAP) to check if user can vote

Step1: Import Functionality
Step2: Implement class/function
Step3: Output

"""
name = input("Enter Your Name \n")
age = int(input("Enter Your Age \n"))

if age >= 18:
    print("You are eligible for voting...")
else:
    print("Watch POGO....")

print("Thank You for using our application....")
"""
Data conversion
Indentation
Escape Sequence
Construct IF else
"""



try:

    if '2' != 2:

        raise ValueError

    else:

        print('same')

except ValueError:

    print('ValueError')

except NameError:

    print('NameError')

    valid = False

    while not valid:

        try:

            n = int(input("6"))

            while n % 2 == 0:
                print("Bye")

            valid = True

        except ValueError:

            print("Invalid")




