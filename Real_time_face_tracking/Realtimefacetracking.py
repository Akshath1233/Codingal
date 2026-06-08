import cv2
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# Load pre-trained Haar Cascade Classifier for face detection
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default. xml')
#print(face_cascade)
# Initialize video capture (use webcam)
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    #capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    #convert frame to greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    #print(faces)
    #draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    #dislpay the face count
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'People Count: {len(faces)}', (10,30), font, 1, (255,0,0), 2)
    #display the resulting frame
    cv2.imshow('Face tracking and counting - Press q to Quit', frame)
    #break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#relese webcam and destroy windows
cap.release()
cv2.destroyAllwindows()

