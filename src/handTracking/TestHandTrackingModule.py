import cv2
import time
import handTrackingModule as htm
# Video de la camara
video = cv2.VideoCapture(0)

# Inicializar deteccion de manos
# mpHands = mp.solutions.hands
# mpDraw = mp.solutions.drawing_utils
# hands = mpHands.Hands()
prevTime = 0
# Capture video
# Press q to quit
detector = htm.handDetector()
  
def showFPS(img):
  auxPrevTime = globals()['prevTime']
  currTime = time.time()
  fps=1/(currTime-auxPrevTime)
  globals()['prevTime'] = currTime
  
  # Escribir FPS
  cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
  

while True: 
  success, img = video.read()
  showFPS(img)
  img = detector.findHands(img)
  lmList = detector.findPositionFromHand(img)
  if len(lmList) > 0:
    print(lmList[4] )
      
  cv2.imshow("Image", img)
  cv2.waitKey(1)  
