import os
import sys
import argparse
import cv2
import torch
import numpy as np

def run(model, source_path: str):
    cap = cv2.VideoCapture(source_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (800, 600))
        result = model(frame)
        frame = np.squeeze(result.render())

        cv2.imshow("yolov5@custom:v1_130531", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect objects inside video')
    parser.add_argument('-m', '--model', type=str, required=True, help='Model Path')
    parser.add_argument('-s', '--source_path', type=str, required=True, help='Source Path')
    args = parser.parse_args()

    if not os.path.exists(args.model):
        print(f"{args.model} is not exist")
        sys.exit(1)

    if not os.path.exists(args.source_path):
        print(f"{args.source_path} is not exist")
        sys.exit(1)

    model = torch.hub.load('ultralytics/yolov5', 'custom', args.model, force_reload=True)

    run(model, args.source_path)

