import cv2
import numpy as np
import os
from create_image import gen_img, output_img
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import joblib

# load classifier
filename = "./data/rbf_model.joblib.pkl"
clf = joblib.load(filename)

canvas = np.ones((200,200), dtype="uint8") + 255
canvas[0:200,0:200] = 0

start_point = None
end_point = None
is_drawing = False
def draw_line(img, start_at, end_at):
   cv2.line(img,start_at,end_at,255,17)

def on_mouse_events(event,x,y,flags,params):
   global start_point
   global end_point
   global canvas
   global is_drawing
   if event == cv2.EVENT_LBUTTONDOWN:
      if is_drawing:
         start_point = (x,y)
   elif event == cv2.EVENT_MOUSEMOVE:
      if is_drawing:
         end_point = (x,y)
         draw_line(canvas, start_point, end_point)
         start_point = end_point
   elif event == cv2.EVENT_LBUTTONUP:
      is_drawing = False

cv2.namedWindow("Test Canvas")
cv2.setMouseCallback("Test Canvas", on_mouse_events)

while(cv2.getWindowProperty('Test Canvas', 0) >= 0):
   cv2.imshow("Test Canvas", canvas)
   key = cv2.waitKey(1) & 0xFF
   if key == ord('q'): break
   elif key == ord('s'): is_drawing = True
   elif key == ord('c'): canvas[0:200,0:200] = 0
   elif key == ord('p'):
      image = canvas[0:200,0:200]
      image = cv2.bitwise_not(image)
      # get img file and convert to vector
      cv2.imwrite('img.png', image)
      arr = gen_img('./img.png')
      os.remove('./img.png')
      x = []
      x.append(arr)
      # output_img(x)   uncomment to see the MNIST version of your number
      # predict number
      num = clf.predict(x)
      print("Predicted number:", int(num[0]))

cv2.destroyAllWindows()
