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
