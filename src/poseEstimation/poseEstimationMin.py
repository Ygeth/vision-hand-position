import cv2
import mediapipe as mp
import time

# Video de la camara
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
  while True: 
    success, img = video.read() 
    showFPS(img)
    
    ## class
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) ## MediaPipe usa RGB
    
    result = pose.process(imgRGB)

    if result.pose_landmarks:
      mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
      
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