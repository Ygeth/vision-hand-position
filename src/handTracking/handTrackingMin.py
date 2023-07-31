import cv2
import mediapipe as mp
import time

# Video de la camara
video = cv2.VideoCapture(0)

# Inicializar deteccion de manos
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()
prevTime = 0

def main():
  # print(currTime, prevTime)
  captureVideo()


# Capture video
# Press q to quit
def captureVideo():
  while True: 
    success, img = video.read()
    showFPS(img)
    
    # hands only uses RGB objects
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
        
    # Check if something was detected
    if results.multi_hand_landmarks:
      # For each hand detected
      for handLms in results.multi_hand_landmarks:
        # Draw hand landmarks
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
        # Enumerar cada una de las los puntos de la mano
        for id, landmark in enumerate(handLms.landmark):
          # Coordenadas de cada punto
          height, width, channels = img.shape
          cx, cy = int(landmark.x*width), int(landmark.y*height)
          # print(id, cx, cy)
          
          # Printar un punto gordo en el pulgar(4)
          # if id == 4:
          #   cv2.circle(img, (cx,cy), 25, (255,255,0), cv2.FILLED)
        
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