MyMobiles = {"Nokia","Samsung","Apple","Oneplus"}

def display():
    for mobile in MyMobiles:
        print(mobile)
    print("----------------------------------")

display()
MyMobiles.add("Mi")
display()

MyMobiles.remove("Samsung")
display()

print(MyMobiles.pop())

MyMobiles.remove("Apple")
display()