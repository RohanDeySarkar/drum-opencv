import cv2
import numpy as np
import subprocess
import pygame
import time

pygame.init()

# load sound files
##beats = pygame.mixer.music
##beat1 = beat.load('lichazhong.wav')
##beats = [beat1.play()]
##
##beat2 = pygame.mixer.music

cap = cv2.VideoCapture(0)

kernel_erode = np.ones((4, 4), np.uint8)
kernel_close = np.ones((15, 15), np.uint8)

while True:

    xr, yr, wr, hr = 0, 0, 0, 0
    
    x1, y1, x2, y2 = 0, 200, 160, 300  # for drawing rectangles on screen later on
    x3, y3, x4, y4 = 180, 300, 320, 400
    x5, y5, x6, y6 = 360, 300, 480, 400
    x7, y7, x8, y8 = 500, 200, 680, 300

    ret,frame = cap.read()
    
    frame = cv2.flip(frame, 1)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,0])
    upper_red = np.array([200,250,200])

    mask = cv2.inRange(hsv,lower_red,upper_red)

    erode = cv2.erode(mask, kernel_erode, iterations = 1)

    closing = cv2.morphologyEx(erode, cv2.MORPH_CLOSE, kernel_close)

    image, contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

    try:
        for i in range(0, 10):
            xr, yr, wr, hr = cv2.boundingRect(contours[i])
            if (wr*hr) > 2000:
                break

    except:
        pass
    
    cv2.rectangle(frame, (xr, yr), (xr+wr, yr+hr), (0,0,255), 2)

    cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 200, 0))
    cv2.rectangle(frame, (x3,y3), (x4,y4), (0, 200, 0))
    cv2.rectangle(frame, (x5,y5), (x6,y6), (0, 200, 0))
    cv2.rectangle(frame, (x7,y7), (x8,y8), (0, 200, 0))

    # detect if the object touches any box, if touch -> play sound

    if xr > x1 and yr > y1 and xr+wr < x2 and yr+hr < y2:
        pygame.mixer.Sound('lichazhong.wav').play()
        time.sleep(0.1)
        pygame.mixer.Sound('lichazhong.wav').stop()

    elif xr > x3 and yr > y3 and xr+wr < x4 and yr+hr < y4:
        pygame.mixer.Sound('digu.wav').play()
        time.sleep(0.1)
        pygame.mixer.Sound('digu.wav').stop()

    elif xr > x5 and yr > y5 and xr+wr < x6 and yr+hr < y6:
        pygame.mixer.Sound('jungu.wav').play()
        time.sleep(0.1)
        pygame.mixer.Sound('jungu.wav').stop()

    elif xr > x7 and yr > y7 and xr+wr < x8 and yr+hr < y8:
        pygame.mixer.Sound('dingcha.wav').play()
        time.sleep(0.1)
        pygame.mixer.Sound('dingcha.wav').stop()


    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k== 27:
        break

cv2.destroyAllwinows()
    
    
