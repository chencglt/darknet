import cv2

sys.path.append(os.path.join(os.getcwd(),'python/'))
import darknet as dn

net_cfg="cfg/yolov2.cfg"
weights="yolov2.weights"
meta_cfg = "cfg/coco.data"

net = dn.network(net_cfg, weights)
meta = dn.metadata(meta_cfg)

img = cv2.imread("data/dog.jpg")
res = dn.detect(net, meta, img)
print(res)