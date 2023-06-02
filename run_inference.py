import os
import sys
import argparse
import cv2
import torch
import numpy as np
import uuid


def run(model, source_path, source_type):
    fcc = cv2.VideoWriter_fourcc(*'XVID')

    cap_type = 0
    if source_type == "video" or source_type == "ip":
        cap_type = source_path

    name = str(uuid.uuid4()) if source_type == "video" else "ip"
    writer = cv2.VideoWriter(f'./demo-{name}.avi', fcc, 30.0, (1020, 720))
    cap = cv2.VideoCapture(cap_type)
    
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            writer.release()
            break

        frame = cv2.resize(frame, (1020, 720))
        #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = model(frame)
        print(result)
        frame = np.squeeze(result.render())
        writer.write(frame)

        cv2.imshow("---", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect objects inside video')
    parser.add_argument('-m', '--model', type=str, required=True, help='Model Path')
    parser.add_argument('-s', '--source_path', type=str, help='Source Path')
    parser.add_argument('-t', '--source_type', type=str, default="video", choices=['video', 'cam', 'ip'], required=False, help='Source Type')
    args = parser.parse_args()

    if not os.path.exists(args.model):
        print(f"{args.model} is not exist")
        sys.exit(1)

    model = torch.hub.load('ultralytics/yolov5', 'custom', args.model, force_reload=True)
    #model.conf = 0.45

    run(model, args.source_path, args.source_type)

