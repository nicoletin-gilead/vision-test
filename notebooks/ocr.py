import cv2 as cv 
import matplotlib.pyplot as plt

import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# OPTICAL CHARACTER RECOGNITION

def box_image_text(image, name = 'bounded_text'):
    img = image.copy()
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img) 
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv.rectangle(img, (int(b[1]), h - int(b[2])), 
              (int(b[3]), h - int(b[4])), (0, 0, 255), 2)

    cv.imshow(name, img)
    cv.waitKey(0)

# cropped = base_image[900:, 950:]
# box_image_text(cropped, 'cropped')
# pytesseract.image_to_string(cropped)