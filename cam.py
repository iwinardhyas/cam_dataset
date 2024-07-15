import cv2 as cv
import time

cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()
    key = cv.waitKey(1)

    cv.imshow('original', img)

    if key == ord('q'):
        break
    elif key == ord(' '):
        cv.imwrite('data/data_{}.jpg'.format(time.time()), img)
        print('saving an image')
        continue
    else:
        continue

cap.release()
cv.destroyAllWindows()