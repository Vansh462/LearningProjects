import pywt
import numpy as np
import cv2

def w2d(img, mode='haar', level=1):
    imArray = img
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_BGR2GRAY )
    #convert to float
    imArray =  np.float32(imArray)
    #normalizing
    imArray /= 255;
    # compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)  # decomposition

    #Process Coefficients
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0;

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);  # reconstruction
    imArray_H *= 255;  # we did /255 then *255 cz wavelet fx works better with 0-1 range
    imArray_H =  np.uint8(imArray_H)

    return imArray_H