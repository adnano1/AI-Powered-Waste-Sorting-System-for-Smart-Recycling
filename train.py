import torch
import cv2

# Load the custom YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/custom_yolov5_weights.pt')

def detect_waste(frame):
    results = model(frame)
    return results

def run_inference():
    cap = cv2.VideoCapture(0)  # Use default camera (can be updated to your specific camera if needed)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect waste using YOLOv5
        results = detect_waste(frame)

        # Render results on the frame
        results.render()

        # Display the frame with the detection results
        cv2.imshow("Waste Detection", results.imgs[0])

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

run_inference()
