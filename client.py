import cv2
import requests
import json
# Open the default camera
cap = cv2.VideoCapture(0)
# Loop to continuously read frames and display them in a window
while True:
    # Read a frame
    ret, frame = cap.read()

    # Display the frame in a window
    cv2.imshow('Webcam Preview', frame)

    # Wait for a key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

_, img_encoded = cv2.imencode('.jpeg', frame)

# Send a POST request to the server
url = 'http://localhost:8080/api/'
headers = {'Content-Type': 'image/jpeg'}
cv2.imwrite('image.jpeg', frame)
response = requests.post(url, data=img_encoded.tobytes(), headers=headers)
# response = requests.get("https://www.google.com")
# Print the server response
y = json.loads(response.content)
if(float(y["conf"])<0.30):
    print("Engine cannot start")
else:
    print("Engine can start")
print(response.content)

# Save the last captured frame to a file
