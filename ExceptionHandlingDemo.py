#Name = "BINOD"
try:
    print(Name)
except:
    print("You can not display name without assigning value")
finally:
    print("Thank You for implementing Exception handling in python")


try:

    1 / 0

except:

    print('exception')

else:

    print('else')

finally:

    print('finally')



def foo():

    try:

        return 1

    finally:

        return 2

k = foo()

print(k)