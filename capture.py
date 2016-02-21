#! /usr/bin/env python2

import cv2
import argparse
import os
import errno

parser = argparse.ArgumentParser()
parser.add_argument("output_dir")
parser.add_argument("-c", "--camera", type=int, default=0)
parser.add_argument("-w", "--width", type=int)
parser.add_argument("-H", "--height", type=int)
parser.add_argument("-s", "--scale", type=float, default=1)

args = parser.parse_args()

cap = cv2.VideoCapture(args.camera)
cap.set(3, args.width)
cap.set(4, args.height)

try:
    os.makedirs(args.output_dir)
except OSError as e:
    if e.errno == errno.EEXIST and os.path.isdir(args.output_dir):
        pass
    else:
        raise

n = len([f for f in os.listdir(args.output_dir)
    if os.path.isfile(os.path.join(args.output_dir, f))])
while True:
    _, frame = cap.read()
    prev = cv2.resize(frame, None, fx=args.scale, fy=args.scale)
    cv2.putText(prev, str(n), (0, 100),
        cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)
    cv2.imshow("preview", prev)

    key = cv2.waitKey(10) & 0xff

    if key == 27:
        break
    elif key == 10:
        n += 1
        cv2.imwrite("%s/frame_%07d.png" % (args.output_dir, n), frame)
