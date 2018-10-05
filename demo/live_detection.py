#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import path
from os.path import abspath
from os.path import join
from os import pardir

from cv2 import flip
from cv2 import rectangle
from cv2 import imshow

path.append(abspath(join(__file__, pardir, pardir, 'src')))
from vcapture import vcap
from facedetector import FaceDetector

DETR = FaceDetector()
RGB_GREEN = (0, 255, 0)


def process(frm):
    frame = flip(frm, 1)
    fpos = DETR.get_faces_pos(frame, minNeighbors=15)

    for (x, y, w, h) in fpos:
        frame = rectangle(frame, (x, y), (x+w, y+h), color=RGB_GREEN, thickness=2)
    imshow('Live Detection', frame)


if __name__ == '__main__':
    with vcap:
        vcap.run(process)
