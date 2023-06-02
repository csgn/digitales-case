import os
import argparse
import cv2
import uuid

fcc = cv2.VideoWriter_fourcc(*'XVID')

def run(spath, opath, interval):
    cap = cv2.VideoCapture(spath)
    c = 0;
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if c % interval == 0:
            out = os.path.join(opath, str(uuid.uuid4()) + '.png')
            print(f"{out} writed\tframe: {c}")
            cv2.imwrite(out, frame)

        c+=1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect objects inside video')
    parser.add_argument('-s', '--source_path', type=str, help='Source Path')
    parser.add_argument('-o', '--output_path', type=str, help='Output path')
    parser.add_argument('-i', '--interval', type=int, help='Interval')
    args = parser.parse_args()

    run(args.source_path, args.output_path, args.interval)

