from ultralytics import YOLO
import cv2

model = YOLO('../yolo-weights/yolov8x.pt')
results = model("images/asia.jpg", show=True)
cv2.waitKey(0)