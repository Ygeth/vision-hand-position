import cv2
import mediapipe as mp
import time

# Video de la camara
video = cv2.VideoCapture(0)

# Inicializar deteccion de manos
# mpHands = mp.solutions.hands
# mpDraw = mp.solutions.drawing_utils
# hands = mpHands.Hands()
prevTime = 0

class handDetector(): 
  def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
    self.mode = mode
    self.maxHands = maxHands
    self.modelComplexity = modelComplexity
    self.detectionCon = detectionCon
    self.trackCon = trackCon
    
    self.mpHands = mp.solutions.hands
    self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
    self.mpDraw = mp.solutions.drawing_utils
  
  def findHands(self, img, draw=True):
    # hands only uses RGB objects
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    self.results = self.hands.process(imgRGB)
        
    # Check if something was detected
    if self.results.multi_hand_landmarks:
      if draw:
        # For each hand detected
        for handLms in self.results.multi_hand_landmarks:
          # Draw hand landmarks
          self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
          
            
    return img
  
  def findPositionFromHand(self, img, handNumber=0, draw=True):
    lmList = []
    if self.results.multi_hand_landmarks:      
      selectedHand = self.results.multi_hand_landmarks[handNumber]
      
      # Enumerar cada una de las los puntos de la mano
      for id, landmark in enumerate(selectedHand.landmark):
            #   # Coordenadas de cada punto
            height, width, channels = img.shape
            cx, cy = int(landmark.x*width), int(landmark.y*height)
            lmList.append([id, cx, cy])
            if draw:
              cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)
    return lmList
    
    
## End handDetector class

def main():
  # print(currTime, prevTime)
  captureVideo()


# Capture video
# Press q to quit
def captureVideo():
  detector = handDetector()
  
  while True: 
    success, img = video.read()
    showFPS(img)
    img = detector.findHands(img)
    lmList = detector.findPositionFromHand(img)
    if len(lmList) > 0:
      print(lmList[4] )
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)  

def showFPS(img):
  auxPrevTime = globals()['prevTime']
  currTime = time.time()
  fps=1/(currTime-auxPrevTime)
  globals()['prevTime'] = currTime
  
  # Escribir FPS
  cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
  


if __name__ == '__main__':
    main()