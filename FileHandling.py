def Read():
    myfile = open("MyDetails.txt",'r')
    print(myfile.readline())
    print(myfile.readlines())
    myfile.close()

Read()

myfile = open("MyDetails.txt",'a')
details = input("Enter more details about you....")
myfile.write(details)
myfile.close()

Read()