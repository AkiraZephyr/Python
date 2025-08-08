import cv2
import matplotlib.pyplot as plt

image_path = "C:\\Academics\\Python\\Digital Image Processing\\download.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Image not found. Please check the path")
    exit()

#Convert BGR to RGB for matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Covert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Display original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imshow()
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#plot histogram
plt.figure(figsize=(12,6))

#Grayscale Histogram
plt.subplot(1,2,1)
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.subplot(1,2,1)
plt.title('Grayscale histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True)

#RGB Channel Histogram
plt.subplot(1,2,2)
colors = ('r', 'g', 'b')
channel_names = ('Red', 'Green', 'Blue')

for i, col in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=channel_names[i])
    
plt.title('RGB Channel Histogram')
plt.xlabel('Pixel intensity')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()