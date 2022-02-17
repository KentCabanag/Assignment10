#Assignment 10

#Contact Tracing App
	#- Create a python program that will read QRCode using your webcam
	#- You may use any online QRCode generator to create QRCode
	#- All personal data are in QRCode 
	#- You may decide which personal data to include
	#- All data read from QRCode should be stored in a text file including the date and time it was read

#Note: 
	#- Search how to generate QRCode
	#- Search how to read QRCode using webcam
	#- Search how to create and write to text file
	#- Your source code should be in github before Feb 19
	#- Create a demo of your program (1-2 min) and send it directly to my messenger.

import cv2
import webbrowser

from cv2 import QRCodeDetector

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
	_, img = cap.read()
	data, bbox, _ = detector.detectAndDecode(img)
	if data:
		a=data
		break
	cv2.imshow("QRCODEscanner", img)
	if cv2.waitKey(1) == ord("q"):
		break

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()
