# sample_code_testing


#finding number of pages in the pdf
number_of_pages = len(pdf_file)

#iterating through each page in the pdf
for current_page_index in range(number_of_pages):
  #iterating through each image in every page of PDF
  for img_index,img in enumerate(pdf_file.getPageImageList(current_page_index)):
        xref = img[0]
        image = fitz.Pixmap(pdf_file, xref)
        #if it is a is GRAY or RGB image
        if image.n < 5:        
            image.writePNG("{}/image{}-{}.png".format(location,current_page_index, img_index))
        #if it is CMYK: convert to RGB first
        else:                
            new_image = fitz.Pixmap(fitz.csRGB, image)
            new_image.writePNG("{}/image{}-{}.png".foramt(location,current_page_index, img_index))
            
            
            +++++
            
            import cv2
import numpy as np

img = cv2.imread("image.jpg")
logo = cv2.imread("logo.png", cv2.IMREAD_UNCHANGED)
rows, cols, channels = logo.shape
roi = img[0:rows, 0:cols]

# Create a mask of the logo and its inverse mask
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 220, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Black-out the area behind the logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, logo_fg)
img[0:rows, 0:cols] = dst

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
+++++++++++++++
Here's a list of steps that can be performed for cleaning an image in OpenCV:

Noise reduction: Remove any random noise from the image using filters like Gaussian blur or median blur.
Color correction: Correct the color balance and brightness of the image using techniques like histogram equalization.
Image sharpening: Enhance the edge information in the image using image sharpening techniques like unsharp masking.
Thresholding: Convert the image to a binary format using thresholding techniques like Otsu's threshold.
morphological operations: Perform morphological operations like erosion and dilation to clean up the binary image.
Contour detection: Detect contours in the binary image and extract the region of interest.
Image resizing: Resize the image to a desired size, either maintaining aspect ratio or not.
Image cropping: Crop the image to remove any unwanted parts.
Image rotation: Rotate the image to align it correctly.
Image denoising: Remove any small-scale noise from the image using techniques like non-local means denoising.
Note that not all of these steps will be required for every image cleaning task, and the specific steps required will depend on the specific task and the properties of the image being processed.





