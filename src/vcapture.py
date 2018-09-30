# -*- coding: utf-8 -*-
from functools import wraps
from cv2 import VideoCapture
from cv2 import waitKey


def singleton(cls):
    """Singleton Pattern"""
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class VCapture(object):
    """Video Capturing

    Class with the single instance that capturing video and processing frames.

    Attributes:
        cap: (capture) video capture with the default camera
        frm: (frame) The frame keep update
    """

    def __init__(self):
        """Init video capture with None."""
        self.cap = None
        self.frm = None

    def __enter__(self):
        """Construct VideoCapture instance if it has not been constructed."""
        if not self.cap:
            self.cap = VideoCapture(0)

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        """Release VideoCapture and set to None when exit."""
        if self.cap:
            self.cap.release()
        self.cap = None

    def run(self, process=lambda frm: None, quit_key='q'):
        """Run process function and check for quit key.

        Args:
            process: the function that will be executed for every frame.
                     ex. def process(frm): ...
            quit_key: end the infinite loop when given quit key is detected.
        """
        while True:
            _, self.frm = self.cap.read()
            process(self.frm)
            if waitKey(1) & 0xFF == ord(quit_key):
                break


"""VCapture Singleton"""
vcap = VCapture()
