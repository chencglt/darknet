# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
import cv2

sys.path.append(os.path.join(os.getcwd(),'python/'))
import darknet as dn

# net_cfg="cfg/yolo9000.cfg"
# weights="yolo9000.weights"
# meta_cfg = "cfg/combine9k.data"

net_cfg="cfg/yolov2.cfg"
weights="yolov2.weights"
meta_cfg = "cfg/coco.data"

net = dn.network(net_cfg, weights)
meta = dn.metadata(meta_cfg)

def draw_box(img, results):
    for box in results:
        x = box[2][0]; y = box[2][1]
        box_width = box[2][2]; box_height = box[2][3]
        x1 = int(x-1/2*box_width); y1 = int(y-1/2*box_height)
        x2 = int(x+1/2*box_width); y2 = int(y+1/2*box_height)
        
        img = cv2.putText(img, box[0], (x1,y1), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return img

def detect_video(video_path):
    net = dn.network(net_cfg, weights)
    meta = dn.metadata(meta_cfg)

    capture = cv2.VideoCapture(video_path)
    read_flag, frame = capture.read()
    while(read_flag):
        res = dn.detect(net, meta, frame)
        img = draw_box(frame, res)
        cv2.imshow("frame", img)
        cv2.waitKey(0)
        read_flag, frame = capture.read()

    capture.release()

def detect_image(image_path):
    net = dn.network(net_cfg, weights)
    meta = dn.metadata(meta_cfg)

    img = cv2.imread(image_path)
    res = dn.detect(net, meta, img)
    img = draw_box(img, res)
    cv2.imshow("frame", img)
    cv2.waitKey(0)

    return res
        

detect_video("data/videos/city.mp4")


