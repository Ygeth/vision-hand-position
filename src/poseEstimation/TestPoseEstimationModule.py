import cv2
import mediapipe as mp
import time
import poseModule as pm


video = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils 

prevTime = 0

def main():
  # print(currTime, prevTime)
  poseEstimationVideo()
  

# Capture video
# Press q to quit
def poseEstimationVideo():
  detector = pm.poseDetector()
  while True: 
    success, img = video.read() 
    showFPS(img)
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    
    if len(lmList) != 0:
      print(lmList[14])
      cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0,0,255), cv2.FILLED)
    
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