import cv2
import numpy as np

img = cv2.imread("images/sample.jpeg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(9,9),2)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=200,
    param1=50,
    param2=30,
    minRadius=200,
    maxRadius=400
)

if circles is not None:

    circles = np.uint16(np.around(circles))

    max_diameter = 0

    for c in circles[0,:]:
        diameter_pixels = c[2] * 2
        if diameter_pixels > max_diameter:
            max_diameter = diameter_pixels

    pixels_per_mm = 20

    diameter_mm = max_diameter / pixels_per_mm

    print("Maximum diameter (pixels):", max_diameter)
    print("Maximum diameter (mm):", diameter_mm)