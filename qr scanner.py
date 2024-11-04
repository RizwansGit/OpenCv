import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)  # Initialize the webcam
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read frame from webcam.")
            break
        
        # Decode QR code in the frame
        codes = decode(img)
        for qrCode in codes:
            myText = qrCode.data.decode('utf-8')
            pts = np.array([qrCode.polygon], np.int32)  # Points for polygon around QR code
            rp = qrCode.rect
            # Draw a bounding box around QR code
            cv2.polylines(img, [pts], True, (255, 0, 0), 3)
            # Display the decoded text
            cv2.putText(img, myText, (rp[0], rp[1]), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 1)
            print(myText)

        # Show the frame with QR code annotations
        cv2.imshow('Result', img)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
