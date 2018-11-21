import cv2
import numpy as np
import subprocess

cap = cv2.VideoCapture(0)

while(1):
    
    ret,frame=cap.read()
	
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
	
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
	
    res=cv2.bitwise_and(frame,frame,mask=mask)
	
    median = cv2.medianBlur(mask, 45)
	
    ret,thresh = cv2.threshold(median ,127,255,0) # cv2.threshold(img, min val, max val, cv.THRESH_BINARY(default))
	
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
	
    wx,wy=median.shape
	
    if contours:
        
	cnt = contours[0]
	M = cv2.moments(cnt) # The function computes moments, up to the 3rd order, of a vector shape or a rasterized shape
	
	if M['m00']!=0:
                    
	    cx = int(M['m10']/M['m00'])  # cx and cy are the default centroids, this is the defalt value
	    cy = int(M['m01']/M['m00'])
			
	    area = cv2.contourArea(cnt)
			
##	print M
##	print "cx:%r,cy:%r"%(cx,cy)
##	print area
##	print wx,wy
			
	    if 0<cx<int(wx/3) and 0<cy<int(wy/3):
                
		subprocess.call(['python', 'gu.py','jungu.wav'])
		#print 'one'
				
	    elif int(wx/3)<cx<int(wx/3*2) and 0<cy<int(wy/3):
		subprocess.call(['python', 'gu.py','bicha.wav'])
		#print 'two'
				
	    elif int(wx/3*2)<cx<int(wx) and 0<cy<int(wy/3):
		subprocess.call(['python', 'gu.py','caicha.wav'])
		#print 'three'
		#two ((0,100),(100,200)) ((100,200),(100,200))  ((200,300),(100,200))
		
	    elif 0<cx<int(wx/3) and int(wy/3)<cy<int(wy/3*2):
		subprocess.call(['python', 'gu.py','datonggu.wav'])
		#print 'four'
		
	    elif int(wx/3)<cx<int(wx/3*2) and int(wy/3)<cy<int(wy/3*2):
		subprocess.call(['python', 'gu.py','digu.wav'])
		#print 'five'
		
	    elif int(wx/3*2)<cx<int(wx) and int(wy/3)<cy<int(wy/3*2):
		subprocess.call(['python', 'gu.py','er1.wav'])
		#print 'six'
		#three ((0,100),(100,200)) ((100,200),(100,200))  ((200,300),(100,200))
				
	    elif 0<cx<int(wx/3) and int(wy/3*2)<cy<int(wy):
		subprocess.call(['python', 'gu.py','er2.wav'])
		#print 'seven'
		
	    elif int(wx/3)<cx<int(wx/3*2) and int(wy/3*2)<cy<int(wy):
		subprocess.call(['python', 'gu.py','lichaqing.wav'])
		#print 'eight'
		
	    elif int(wx/3*2)<cx<int(wx) and int(wy/3*2)<cy<int(wy):
		subprocess.call(['python', 'gu.py','lichachong.wav'])
		#print 'nine'
		
	    else:
		subprocess.call(['python', 'gu.py','jungu.wav'])
		#print 'unknown'
				
	#cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	#cv2.imshow('res',res)
    cv2.imshow('median',median)
    k=cv2.waitKey(5)&0xFF
    if k==27:
		break
cv2.destroyAllWindows()
