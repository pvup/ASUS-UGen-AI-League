
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

TARGET_ITEMS = ["cup"]
MISSING_THRESHOLD = 20

missing_counts = {item: 0 for item in TARGET_ITEMS}
ever_seen = {item: False for item in TARGET_ITEMS}

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    raise RuntimeError("Cannot open camera")

print("Smart Desk Inventory Started!")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = model.predict(
        frame,
        device="cpu",
        imgsz=640,
        conf=0.25,
        verbose=False
    )[0]

    display = result.plot()

    detected = set()

    if result.boxes is not None:
        for cls_id in result.boxes.cls.tolist():
            detected.add(result.names[int(cls_id)])

    for i, item in enumerate(TARGET_ITEMS):

        if item in detected:
            ever_seen[item] = True
            missing_counts[item] = 0
        else:
            missing_counts[item] += 1

        if not ever_seen[item]:
            status = "WAITING"
            color = (0, 255, 255)

        elif missing_counts[item] == 0:
            status = "PRESENT"
            color = (0, 255, 0)

        elif missing_counts[item] < MISSING_THRESHOLD:
            status = "CHECKING"
            color = (0, 255, 255)

        else:
            status = "MISSING"
            color = (0, 0, 255)

        cv2.putText(
            display,
            f"{item.upper()}: {status}",
            (20, 45 + i * 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )

    cv2.imshow("Smart Desk Inventory", display)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
