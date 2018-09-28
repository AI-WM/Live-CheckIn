# -*- coding: utf-8 -*-
from functools import wraps
from cv2 import VideoCapture
from cv2 import waitKey

def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class VCapture(object):
    def __init__(self):
        self.cap = None
        self.frm = None

    def __enter__(self):
        if not self.cap:
            self.cap = VideoCapture(0)

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        if self.cap:
            self.cap.release()
            self.cap = None

    def run(self, process, quit_key='q'):
        while True:
            _, self.frm = self.cap.read()
            process(self.cap, self.frm)
            if waitKey(1) & 0xFF == ord(quit_key):
                break

vcap = VCapture()
