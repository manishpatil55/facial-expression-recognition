import cv2  # pip install opencv-python
from deepface import DeepFace  # pip install deepface

# Load the pre-trained face detector from OpenCV
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(1)

# Check if the webcam is opened correctly
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()  # Read one image from a video

    if not ret:
        break

    try:
        # Analyze the frame for emotion using DeepFace with enforce_detection set to False
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list):
            result = result[0]
        dominant_emotion = result.get('dominant_emotion', "Error")
    except Exception as e:
        print(f"Error analyzing frame: {e}")
        dominant_emotion = "Error"

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Set the font for the text
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Insert text (dominant emotion) on the video
    cv2.putText(frame,
                dominant_emotion,
                (50, 50),
                font, 1, (0, 0, 255),
                2,
                cv2.LINE_AA)

    # Display the video
    cv2.imshow('Original video', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
