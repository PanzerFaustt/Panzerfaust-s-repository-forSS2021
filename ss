import apriltag
import cv2
image = cv2.imread("/home/duck1/opencvTest/TEG")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)
results = detector.detect(gray)
print(str(results))
print(str(results).find("tag_id="))
print(str(results)[42:45].split(","))
