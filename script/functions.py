import cv2
import numpy as np
from scipy import ndimage

CLASS_NAMES = ['2-purple-empty-squiggles',
'2-red-striped-ovals',
'2-green-empty-squiggles',
'1-green-striped-squiggle',
'3-red-empty-diamonds',
'3-red-empty-squiggles',
'2-green-solid-squiggles',
'3-green-empty-squiggles',
'1-purple-striped-oval',
'2-green-striped-squiggles',
'2-purple-solid-squiggles',
'1-purple-empty-oval',
'2-purple-empty-ovals',
'2-purple-striped-ovals',
'3-red-striped-diamonds',
'3-purple-striped-diamonds',
'3-green-solid-diamonds',
'2-red-striped-squiggles',
'3-green-solid-squiggles',
'2-red-solid-diamonds',
'1-purple-empty-diamond',
'1-purple-empty-squiggle',
'2-red-solid-ovals',
'3-purple-solid-diamonds',
'2-red-empty-diamonds',
'2-purple-solid-ovals',
'1-red-striped-diamond',
'1-red-striped-oval',
'3-green-solid-ovals',
'3-purple-empty-squiggles',
'2-green-empty-diamonds',
'3-red-solid-squiggles',
'1-red-solid-oval',
'2-red-empty-ovals',
'1-purple-solid-oval',
'2-purple-striped-diamonds',
'1-green-empty-oval',
'1-green-solid-oval',
'2-purple-empty-diamonds',
'3-purple-striped-ovals',
'3-purple-empty-diamonds',
'2-green-solid-diamonds',
'3-green-striped-ovals',
'1-red-empty-oval',
'2-purple-solid-diamonds',
'2-green-striped-ovals',
'1-green-solid-diamond',
'2-purple-striped-squiggles',
'3-purple-solid-ovals',
'2-green-empty-ovals',
'2-green-solid-ovals',
'3-red-solid-diamonds',
'1-green-striped-diamond',
'1-green-empty-squiggle',
'1-red-solid-diamond',
'3-red-empty-ovals',
'3-green-striped-squiggles',
'1-purple-striped-diamond',
'2-red-empty-squiggles',
'1-green-empty-diamond',
'3-green-empty-ovals',
'1-red-empty-squiggle',
'1-purple-striped-squiggle',
'1-green-striped-oval',
'3-purple-solid-squiggles',
'1-red-empty-diamond',
'3-green-empty-diamonds',
'1-red-solid-squiggle',
'3-red-striped-squiggles',
'2-red-striped-diamonds',
'3-green-striped-diamonds',
'3-purple-striped-squiggles',
'2-red-solid-squiggles',
'3-red-striped-ovals',
'1-purple-solid-diamond',
'1-green-solid-squiggle',
'2-green-striped-diamonds',
'1-red-striped-squiggle',
'3-purple-empty-ovals',
'1-purple-solid-squiggle',
'3-red-solid-ovals']



def trim(frame):
    #crop top
    if not np.sum(frame[0]):
        return trim(frame[1:])
    #crop bottom
    elif not np.sum(frame[-1]):
        return trim(frame[:-2])
    #crop left
    elif not np.sum(frame[:,0]):
        return trim(frame[:,1:]) 
    #crop right
    elif not np.sum(frame[:,-1]):
        return trim(frame[:,:-2])    
    return frame



def find_ROI(image):
    """Without plotting the steps, finds the contours and crops the image"""

    #image = cv2.imread(image_path)
    image = cv2.resize(image,(250,250)) # resizing 
    #cv2_imshow(image)
    image = cv2.GaussianBlur(image,(5,5),1) # gaussian blur to smoothen the image
    edge = cv2.Canny(image,100,200) # detect edges from colored image

    contours, hierarchy = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours

    img_cpy = image.copy() #create an image copy
    
    index=0
    thickness=3
    color=(255,0,0)
    
    cv2.drawContours(img_cpy,contours,index,color,thickness)  #select first contour
    #cv2_imshow(edge) #show edged image
    #cv2_imshow(img_cpy) #show image + contours

    ############################### min surf rect
    img_cpy3 = image.copy()
    rect = cv2.minAreaRect(contours[0]) #create a rectangle from contour

    box = cv2.boxPoints(rect) #convert into a four points array[[x y]]
    box = np.int0(box) #cast into integers

    angle = rect[2]
    #print("theta= ",angle)
    im = cv2.drawContours(img_cpy3,[box],0,(0,0,255),2) #draw rectangular contour
    #cv2_imshow(im)

    rotated = ndimage.rotate(img_cpy3, angle)
    #cv2_imshow(rotated)

    pts = box

    mask = np.zeros(image.shape, np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    result = cv2.bitwise_and(image, mask)
    rotated = ndimage.rotate(result, angle)

    #cv2_imshow(rotated)

    
    thold = (rotated>120)*rotated
    trimmedImage = trim(rotated)
    trimmedImage = cv2.resize(trimmedImage,(160,160))
    
    #cv2_imshow(thold)
    #cv2_imshow(trimmedImage)
    return trimmedImage
    
    
