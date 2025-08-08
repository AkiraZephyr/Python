import cv2

image = cv2.imread("C:\Academics\Python\Digital Image Processing\Lab1.jpg",0)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
