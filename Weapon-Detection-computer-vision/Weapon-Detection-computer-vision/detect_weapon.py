from ultralytics import YOLO
import cv2
import numpy as np


model = YOLO("yolov8n.pt")


weapon_keywords = ["knife", "gun", "rifle", "pistol","person"]


img = cv2.imread("test.jpg")
original = img.copy()


results = model(img)

masked = np.zeros_like(img)

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        
        if any(w in label.lower() for w in weapon_keywords):
            masked[y1:y2, x1:x2] = original[y1:y2, x1:x2]

            cv2.rectangle(masked, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                masked,
                f"{label} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )


cv2.namedWindow("Weapon Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Weapon Detection", 800, 600)


cv2.imshow("Weapon Detection", masked)
cv2.imwrite("output.jpg", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
