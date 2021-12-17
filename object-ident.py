import cv2
import RPi.GPIO as gpio
import time

classNames = []
classFile = "./coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "./ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "./frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward(sec):
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    print('forward')
    time.sleep(sec)
    #gpio.cleanup()

def left(sec):
    gpio.output(17, True)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    print('left')
    time.sleep(sec)

def right(sec):
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, False)
    print('right')
    time.sleep(sec)

def reverse(sec):
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    print('reverse')
    time.sleep(sec)
    #gpio.cleanup()

def stop(sec):
    gpio.output(17, False)
    gpio.output(22, False)
gpio.output(23, False)
    gpio.output(24, False)
    print('stop')
    time.sleep(sec)
    
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    #print('classIds',bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className == 'cup':
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    x, y, w, h = box
                    #print(box)
                    center = (x+w)/2
                    #print(center)
                    print(center)
                    if center < 150:
                        left(0.1)
                    if center > 171 and center < 300:
                        forward(0.1)
                    if center > 300:
                        right(0.1)
#                     if center in range(171, 360):

            else:
                stop(0.1)

    return img,objectInfo


if __name__ == "__main__":
    init()
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    count = 0
    #cap.set(10,70)
    #try:
    while True:
        success, img = cap.read()
        if count == 10:
            print('analyzing')
            result, objectInfo = getObjects(img,0.45,0.2,objects=['cup'])
            count = 0
        #print(objectInfo)
#        cv2.imshow("Output",img)
        cv2.waitKey(1)
        count += 1
    #finally:
        #gpio.cleanup()