import cv2
import pickle
import cvzone
import numpy as np

# Load the video feed
cap = cv2.VideoCapture('C:\\Users\\JUI JOB\\Desktop\\CV\\data\\PARKING_VID.mp4')

# Width and height of the parking spaces (as before)
width, height = 18, 45

# Load the parking positions and zones from pickle files
with open('CarParPos', 'rb') as f:
    posList = pickle.load(f)

with open('CarParZones', 'rb') as f:
    zones = pickle.load(f)  # Zones loaded from file

# Function to check the parking space availability
def checkParkingSpace(imgPro):
    totalFreeSpaces = 0

    # Define separate color, thickness, and positions for each zone
    zone_text_properties = {
        'A': {'color': (0, 0, 139), 'thickness': 1, 'pos': (8, 30),'size':0.8},
        'B': {'color': (0, 153, 255), 'thickness': 1, 'pos': (475, 30),'size':0.8},
        'C': {'color': (128, 0, 128), 'thickness': 1, 'pos': (8, 170),'size':0.8},
        'D': {'color': (139, 69, 19), 'thickness': 1, 'pos': (475, 170),'size':0.8},
        # Add more zones as necessary with different positions
    }

    # Loop through each zone and its parking positions
    for zone_name, zone_positions in zones.items():
        zoneFreeSpaces = 0
        for pos in zone_positions:
            x, y = pos
            imgCrop = imgPro[y:y+height, x:x+width]
            count = cv2.countNonZero(imgCrop)

            # Display the count of non-zero pixels for each parking slot
            cvzone.putTextRect(img, str(count), (x, y + height - 5), scale=0.6, thickness=1, offset=0, colorR=(0, 0, 255))

            if count < 170:  # If the parking space is free (based on non-zero pixel count)
                color = (0, 255, 0)
                thickness = 2
                zoneFreeSpaces += 1  # Increment the free space counter for this zone
            else:
                color = (0, 0, 255)
                thickness = 1

            # Draw the rectangle for each parking space
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)

        # Customize the text properties for the current zone
        if zone_name in zone_text_properties:
            text_properties = zone_text_properties[zone_name]
            color = text_properties['color']
            thickness = text_properties['thickness']
            position = text_properties['pos']
        else:
            color = (0, 255, 0)
            thickness = 2
            position = (20, 40 + 20 * list(zones.keys()).index(zone_name))

        # Display the number of free spaces in the current zone with custom position and color
        cvzone.putTextRect(img, f'{zone_name}: {zoneFreeSpaces} Free', position, scale=text_properties['size'], thickness=thickness, offset=2, colorR=color)

        # Update the total number of free spaces across all zones
        totalFreeSpaces += zoneFreeSpaces

    # Display the total free spaces across all zones with custom positioning
    cvzone.putTextRect(img, f'Total Free: {totalFreeSpaces}/{sum(len(positions) for positions in zones.values())}', (200, 15), scale=1, thickness=1, offset=10, colorR=(0, 200, 0))

# Main loop to process video feed
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    if not success:
        break  # Exit if video frame is not fetched successfully

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 0.7)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    # Display the frames
    cv2.imshow("image", img)
    cv2.imshow("imageBlur", imgBlur)
    cv2.imshow("imageThresh", imgDilate)

    cv2.waitKey(20)

# Release the video feed and close windows
cap.release()
cv2.destroyAllWindows()
