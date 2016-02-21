#! /usr/bin/env python2

import cv2
import argparse
import os
import errno
import math
import numpy as np

def dist(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


parser = argparse.ArgumentParser()
parser.add_argument("calibration_file")
parser.add_argument("image_dir")
parser.add_argument("output_dir")

args = parser.parse_args()

try:
    os.makedirs(args.output_dir)
except OSError as e:
    if e.errno == errno.EEXIST and os.path.isdir(args.output_dir):
        pass
    else:
        raise

with open(args.calibration_file, "r") as f:
    n = 0

    while True:
        line = f.readline()
        if not line:
            break
        line = list(map(int, line.strip("\r\n").split(" ")))

        ms = []
        dsizes = []
        for p in range(line[2]):
            c = [list(map(int, l.strip("\r\n").split(" ")))
                for l in [f.readline() for i in range(4)]]
            w = int(dist(c[0], c[1]))
            h = int(dist(c[0], c[2]))
            nc = [[0, 0], [w, 0], [0, h], [w, h]]
            ms.append(cv2.getPerspectiveTransform(
                    np.array(c, dtype=np.float32),
                    np.array(nc, dtype=np.float32)))
            dsizes.append((w, h))

        for i in range(line[0], line[1]+1):
            img = cv2.imread(os.path.join(args.image_dir, "frame_%07d.png" % i))
            for (m, dsize) in zip(ms, dsizes):
                new_img = cv2.warpPerspective(img, m, dsize)
                n += 1
                new_name = os.path.join(args.output_dir, "frame_%07d.png" % n)
                cv2.imwrite(new_name, new_img)

