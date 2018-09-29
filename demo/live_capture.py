#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cv2 import imshow
from cv2 import flip
from cv2 import cvtColor
from cv2 import COLOR_BGR2GRAY

from sys import path
from os.path import abspath
from os.path import join
from os import pardir
path.append(abspath(join(__file__, pardir, pardir, 'src')))

from vcapture import vcap


def process(cap, frm):
    frame = flip(frm, 1)
    gray = cvtColor(frame, COLOR_BGR2GRAY)
    imshow('Live Capture', gray)


def main():
    with vcap:
        vcap.run(process)


if __name__ == '__main__':
    main()
