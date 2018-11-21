import pygame, sys  
from pygame.locals import *
import time

pygame.init()
gu1 = sys.argv[1]
soundObj = pygame.mixer.Sound(gu1)  
soundObj.play()  
 
time.sleep(0.4)  
soundObj.stop()  
