import matplotlib.pyplot as pt
import matplotlib.image as im

myImage = im.imread("India_gate.jpg",)

print(im)
print(myImage)

imgplt = pt.imshow(myImage)
pt.colorbar()
pt.show()

NewImage = myImage[:,:,0]
pt.imshow(NewImage,cmap="hot")
pt.imshow(NewImage)
pt.show()