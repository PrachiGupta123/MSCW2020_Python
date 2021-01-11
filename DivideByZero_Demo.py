import sys


no1 = int(input("Enter first no"))
no2 = int(input("Enter second no"))
try:
    output = no1/no2
    print("Final output is" + str(output))
    print(Name)

except ZeroDivisionError:
    print("Do not try to divide a no by 0")
    error = sys.exc_info()[0]
    print(error)
    sys.exit()
except NameError:
    print("Defirn all variables before using it")
    error = sys.exc_info()[0]
    print(error)

finally:
    print("Thank You for using my application")



