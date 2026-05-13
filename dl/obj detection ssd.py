import cv2
import matplotlib.pyplot as plt

# Load pretrained SSD MobileNet model
config = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
model  = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(model, config)

# Model settings
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

# COCO class labels
classes = []
with open("coco.names","r") as f:
    classes = f.read().strip().split("\n")

# Load image
img = cv2.imread("test.jpg")

# Detect objects
classIds, confs, boxes = net.detect(img, confThreshold=0.5)

# Draw detections
for classId, conf, box in zip(classIds.flatten(), confs.flatten(), boxes):

    label = classes[classId-1]

    cv2.rectangle(img, box, (0,255,0), 2)

    cv2.putText(img,
                f"{label}: {conf:.2f}",
                (box[0], box[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2)

# Show output
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
