#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import path
from os.path import abspath
from os.path import join
from os import pardir
from urllib.request import urlopen

from numpy import asarray
from numpy import uint8
from cv2 import imdecode
from cv2 import IMREAD_COLOR
from cv2 import cvtColor
from cv2 import COLOR_BGR2RGB
from cv2 import rectangle
from cv2 import imshow
from cv2 import waitKey

path.append(abspath(join(__file__, pardir, pardir, 'src')))
from facedetector import FaceDetector


def main():
    img_url = ('http://2.bp.blogspot.com/-Ooj8qMem5vo/VRKMGtvmWJI'
               '/AAAAAAAABjg/DH001_agnPY/s1600/face.jpg')
    img_np = asarray(bytearray(urlopen(img_url).read()), dtype=uint8)
    image = imdecode(img_np, IMREAD_COLOR)

    detr = FaceDetector()
    fpos = detr.get_faces_pos(image, minNeighbors=15)

    RGB_GREEN = (0, 255, 0)
    roi = image.copy()
    for (x, y, w, h) in fpos:
        roi = rectangle(roi, (x, y), (x+w, y+h), color=RGB_GREEN, thickness=2)

    imshow('Face Detection', roi)
    waitKey(0)


if __name__ == '__main__':
    main()
