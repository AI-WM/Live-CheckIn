#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cv2 import imshow
from cv2 import flip
from cv2 import cvtColor, COLOR_BGR2GRAY
from vcapture import vcap


def process(cap, frm):
    frame = flip(frm, 1)
    gray = cvtColor(frame, COLOR_BGR2GRAY)
    imshow('Live Capture', gray)

if __name__ == '__main__':
    with vcap:
        vcap.run(process)

