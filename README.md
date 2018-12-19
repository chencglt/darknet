## Retrain YOLOv3 with Custom Dataset

Following files are need to retrain Yolov3 with your data.
1. Pre-trained weights of darknet53: [darknet53.conv.74](https://pjreddie.com/media/files/darknet53.conv.74)
2. Config file of your dataset
3. Create your own yolov3.cfg. Your can simply using the config file in *cfg/*, and make sure the lines below are modified according to your dataset
* Change the lines about class numbers:
      Line 610: classes = <num>
      Line 696: classes = <num>
      Line 783: classes = <num>
* Set the lines about filter numbers as ** (class_number+5)*3 **:
      Line 603: filters = (class_number+5)*3
      Line 689: filters = (class_number+5)*3
      Line 776: filters = (class_number+5)*3
