import cv2
import mediapipe as mp
import time

# Video de la camara
video = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils 

prevTime = 0


class poseDetector():
  def __init__(self, mode=False, upBody=False, smooth=True, 
              detectionCon=0.5, trackCon=0.5):
    self.mode = mode
    self.upBody = upBody
    self.smooth = smooth
    self.detectionCon = detectionCon
    self.trackCon = trackCon
    
    self.results=None
    self.mpDraw = mp.solutions.drawing_utils
    self.mpPose = mp.solutions.pose
    self.pose = self.mpPose.Pose()
  
  def findPose(self, img, draw=True):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    self.results = self.pose.process(imgRGB)
    
    if draw:
      if self.results.pose_landmarks:
        self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
    
    return img
  
  def findPosition(self, img, draw=True):
    lmList = []
    if self.results:
      if self.results.pose_landmarks:
        for id, lm in enumerate(self.results.pose_landmarks.landmark):
          h, w, c = img.shape
          cx, cy = int(lm.x*w), int(lm.y*h)
          lmList.append([id, cx, cy])
          if draw:
            cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)
    return lmList
    
    
def main():
  # print(currTime, prevTime)
  poseEstimationVideo()
  

# Capture video
# Press q to quit
def poseEstimationVideo():
  detector = poseDetector()
  while True: 
    success, img = video.read() 
    showFPS(img)
    img = detector.findPose(img)
    lmList = detector.findPosition(img)
    
    if len(lmList) == 14:
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