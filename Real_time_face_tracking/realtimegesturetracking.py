import cv2
from matplotlib.pyplot import hsv
import numpy as np 

# Set up webcam capture
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    #Convert HSV for colour filtering
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Define the lower and upper colour ranges in HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    # Create a mask to detect skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Apply the mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #Find contours in the masked image
    contours,_= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # if contours are found, draw them
    if contours:
        max_contour = max(contours, key=cv2.contourArea)#Getting the largest contour
        if cv2.contourArea(max_contour) > 500: # ignore small contours 
            #Draw bounding box around the hand
            x,y,w,h= cv2.BoundingRect(max_contour)
            cv2.rectangle(frame,(x,y),(x + w , y + h),(0,255,0),2)
            #Get the ceter of the hand for further tracking and interaction
            center_x = int(x + w/2)
            center_y = int(y + h / 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) #Red dot at the center of the hand
    # Display the original and result frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Filtered Frame', result)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows

