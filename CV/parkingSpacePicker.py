import cv2
import pickle

width, height = 18, 45
zones = {"A": [], "B": [], "C": [], "D": []}  # Define zones

try:
    with open('CarParZones', 'rb') as f:
        zones = pickle.load(f)
except:
    zones = {"A": [], "B": [], "C": [], "D": []}

current_zone = "A"  # Default zone for adding rectangles


def mouseClick(events, x, y, flags, params):
    global current_zone
    if events == cv2.EVENT_LBUTTONDOWN:
        zones[current_zone].append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for zone in zones.values():
            for i, pos in enumerate(zone):
                x1, y1 = pos
                if x1 < x < x1 + width and y1 < y < y1 + height:
                    zone.pop(i)
                    break
    with open('CarParZones', 'wb') as f:
        pickle.dump(zones, f)


while True:
    img = cv2.imread('C:\\Users\\JUI JOB\\Desktop\\CV\\data\\PARKSLOT_SS.jpg')

    # Draw all rectangles for each zone
    for zone_name, positions in zones.items():
        for pos in positions:
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
            cv2.putText(img, zone_name, (pos[0], pos[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Define Zones", img)
    cv2.setMouseCallback("Define Zones", mouseClick)

    key = cv2.waitKey(1)
    if key == ord('a'):
        current_zone = "A"
    elif key == ord('b'):
        current_zone = "B"
    elif key == ord('c'):
        current_zone = "C"
    elif key == ord('d'):
        current_zone = "D"
    elif key == 27:  # Press ESC to exit
        break
