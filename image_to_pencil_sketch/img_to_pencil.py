

# Import open-cv library
import cv2

# Reading image File
image = cv2.imread('./cat.jpg')

# Displaying Original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Reading the black and white image
baw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# To display black and white image
cv2.imshow("Black and White Image", baw_image)
cv2.waitKey(0)

# inverting the image
inverted_image = 255-baw_image

# displaying inverted image
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey()

# Blurring the image
blurred = cv2.GaussianBlue(inverted_image, (21, 21), 0)

# Inverting the blurred image
inverted_image = 255-blurred

# Creating the pencil sketch image
pencil_sketch = cv2.divide(baw_image, inverted_image, scale=256.0)

# Displaying sketch image
cv2.imshow("Sketch image", pencil_sketch)
cv2.waitKey(0)

# Displaying original image
cv2.imshow("Original image", image)

# Displaying Sketch image

cv2.imshow("Pencil Sketch Image", pencil_sketch)

cv2.waitKey(0)
