import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, width, hight, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((width, hight))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            width1, hight1 = pos
            if width1 < width < width1 + width and hight1 < hight < hight1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as file:
        pickle.dump(posList, file)

while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
