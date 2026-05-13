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



import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense

# Load CIFAR-10
(x_train,y_train),(x_test,y_test)=cifar10.load_data()

class_names=['airplane','car','bird','cat','deer',
             'dog','frog','horse','ship','truck']

# Preprocess
x_train=x_train[:5000]/255.0
x_test=x_test[:10]/255.0

x_train=tf.image.resize(x_train,(96,96))
x_test=tf.image.resize(x_test,(96,96))

# Transfer Learning Model
base=MobileNetV2(weights='imagenet',
                 include_top=False,
                 input_shape=(96,96,3))

base.trainable=False

model=Sequential([
    base,
    GlobalAveragePooling2D(),
    Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train
model.fit(x_train,y_train[:5000],epochs=3,batch_size=32)

# Predict one image
img=x_test[0]
pred=model.predict(np.expand_dims(img,0),verbose=0)

cls=np.argmax(pred)
conf=np.max(pred)

# Draw fake detection box
img_np=np.array(img)

h,w,_=img_np.shape

cv2.rectangle(img_np,(20,20),(w-20,h-20),(0,255,0),2)

cv2.putText(img_np,
            f"{class_names[cls]} : {conf:.2f}",
            (20,15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,0),
            1)

# Show
plt.imshow(img_np)
plt.axis("off")
plt.show()
