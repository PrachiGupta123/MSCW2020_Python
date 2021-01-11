import matplotlib.pyplot as pt

x = [2,5,9]
y = [4,15,36]

pt.plot(x,y)
pt.xlabel("No of Indian Webseries on OTA platform")
pt.ylabel("No of Netflix Subscribers in 2020(Thousands)")
pt.bar(x,y)
pt.show()

