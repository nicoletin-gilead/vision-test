import os
import numpy as np
import cv2 as cv

# IMAGE PREPROCESSING TOOLS

# section image with/out text
def crop_text(img, text=True):
    if text == False:
        return img[:750, :]
    else:
        return img[750:, :]

# Dilate without eroding image (semi-tuned)
def dilate(img):
    kernel = np.ones((5,5), np.uint8)
    return cv.dilate(img, kernel, iterations= 1)

# tuned
# def canny(img, thresh_a = 30, thresh_b = 150):

#     return cv.Canny(img, thresh_a, thresh_b)
canny = lambda img: cv.Canny(img, 30, 150)

# IMAGE LOADING AND PREVIEW
data_root = "/Users/nicolelrtin/vision-test/data/source"

def get_internaldata():
    internal = data_root + '/internal/'
    file_names = os.listdir(internal)
    image = []
    for name in file_names: image += [cv.imread(internal + name)]
    return image

# preview image, missing save image functionality
def preview(img, savename = 'preview_image'):
    cv.imshow(savename, img)
    k = cv.waitKey(0)
    
    if k == ord('s'):
        cv.imwrite(savename + '.png', img)

# DEMO

# sample = get_internaldata()[2].copy()
# preview(sample, 'reference image')
