import cv2
import numpy as np
import tensorflow as tf
from scipy import ndimage
from functions import *
from tflite_runtime.interpreter import load_delegate


cap = cv2.VideoCapture(0)

interpreter = tf.lite.Interpreter(model_path="../CNN_V2_git.tflite",experimental_delegates=[load_delegate('libedgetpu.so.1.0')])
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

while True:
    _, frame = cap.read()
    
    cropped = find_ROI(frame)
    ROI = cropped.copy()
    cropped = cropped.astype(np.float32)
    input_data = np.expand_dims(cropped, axis=0)
    
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])
    pred_id=np.argmax(prediction,axis=-1)
    pred_label=CLASS_NAMES[int(pred_id)]
    
    print(pred_label)
    
    cv2.imshow('frame',frame)
    #cv2.imshow('cropped',cropped)
    cv2.imshow('ROI',ROI)
    key = cv2.waitKey(1)
  
#closing all open windows 
cv2.destroyAllWindows() 




