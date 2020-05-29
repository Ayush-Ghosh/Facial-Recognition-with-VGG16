import numpy as np
import os, time
import cv2
name = str(input("Enter the name of Person: "))

path1 = r".\data\videos" +"/"+ name
path2 = r".\data\face_images" + "/"+ name
os.makedirs(path1)
os.makedirs(path2)

name1 = name + ".avi"
#path = "./data/videos/" + name1 +"/"+name
savepath = r".\data\videos" + "/"+ name +"/"+name1
print("Registering Face.")
time.sleep(2)

# The duration in seconds of the video capture
capture_duration = 20

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter(savepath,fourcc, 20.0, (640,480))

start_time = time.time()
while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
        cv2.imshow('frame',frame)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()