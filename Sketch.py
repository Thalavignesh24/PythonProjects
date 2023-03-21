import cv2
image=cv2.imread("Bat.jpg")
grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(grey_img)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertBlur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertBlur,scale=256.0)
cv2.imwrite("pencilSketch.png",sketch)


# import cv2
# image=cv2.imread("Bat.jpg")
# color=2

# if(color==2):
#     grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2LUV)
#     cv2.imwrite("sketch3.png",grey_img)

# elif (color==3):
#     grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     blur=cv2.GaussianBlur(grey_img,(21,21),0)
#     cv2.imwrite("second.png",blur)

