#! /usr/bin/env python2

from __future__ import print_function
import cv2
import argparse
import os

last_click = None

def mouse_callback(event, x, y, flags, params):
    global last_click
    if event == cv2.EVENT_LBUTTONDOWN:
        last_click = (x, y)

def request_point(img, text):
    global last_click
    last_click = None

    cv2.namedWindow(text)
    cv2.setMouseCallback(text, mouse_callback)

    while True:
        prev = img.copy()
        cv2.putText(prev, text, (0, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
        if last_click is not None:
            cv2.circle(prev, last_click, 2, (255, 0, 0), -1)

        cv2.imshow(text, prev)
        key = cv2.waitKey(10) & 0xff
        if key == 10:
            cv2.destroyWindow(text)
            return last_click

def get_corners(img_path, page_num):
    img = cv2.imread(img_path)
    text = (
        "Top left",
        "Top right",
        "Bottom left",
        "Bottom right",
        )
    return [request_point(img, "%s page %d" % (t, page_num)) for t in text]

parser = argparse.ArgumentParser()
parser.add_argument("ranges_file")
parser.add_argument("image_dir")
parser.add_argument("output_file")

args = parser.parse_args()

with open(args.ranges_file, "r") as f, open(args.output_file, "w") as o:
    for line in f:
        if line[0] == '#':
            continue
        line = list(map(int, line.strip("\r\n").split(" ")))
        m = (line[0]+line[1]+1)//2

        print(line[0], line[1], line[2], file=o)
        for i in range(line[2]):
            corners = get_corners(os.path.join(args.image_dir,
                    "frame_%07d.png" % m), i+1)
            for c in corners:
                print(c[0], c[1], file=o)
