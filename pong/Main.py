
import cv2
import datetime
import numpy as np
import time
from pynput.mouse import Button, Controller
import pyautogui

## The below image resize function resizes the image without causing distortion.
## https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized

cap = cv2.VideoCapture(0)

m = pyautogui

last_click = datetime.datetime.now()

while True:
	_, frame = cap.read()
	frame = cv2.flip(frame, 1)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_orange = np.array([0, 120, 232])
	upper_orange = np.array([179, 255, 255])
	mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)

	contoursOrange, _ = cv2.findContours(mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for c in contoursOrange :
		if cv2.contourArea(c) <= 50 :
			continue
		x, y, _, _ = cv2.boundingRect(c)
		m.moveTo(x, y, _pause=False)
		cv2.drawContours(frame, contoursOrange, -1, (0, 255, 0), 3)
	
	frame = image_resize(frame, width = 800)  
	cv2.imshow("frame", frame)
	
	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()