"""

While loop in python
"""

for no in range(10):
    print(no)

print("printing in Reverse order")

for no in range(10,0,-1):
    print(no)

age = 12
while age<18:
    age += 1
    print("You can not vote")
    if age == 18:
        break
