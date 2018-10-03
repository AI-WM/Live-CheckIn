# -*- coding: utf-8 -*-
from os.path import exists
from os.path import abspath
from os.path import join
from os import pardir
from urllib.request import urlopen

from cv2 import CascadeClassifier


class FaceDetector(object):
    """Face Detector

    Face detection by Haar Feature-based Cascade Classifier in OpenCV.

    Attributes:
        ccc: Cascade Classifier
    """

    @staticmethod
    def get_abs_path(file_name='haarcascade.xml'):
        """Return absolute path for given file name under data directory."""
        return abspath(join(__file__, pardir, pardir, 'data', file_name))

    @staticmethod
    def download_haarcascade_xml(save_path=None):
        """Download haar cascade file and save into given path."""
        if not save_path:
            save_path = FaceDetector.get_abs_path()

        xml_url = ('https://raw.githubusercontent.com/opencv/opencv/master'
                   '/data/haarcascades/haarcascade_frontalface_default.xml')
        xml_doc = urlopen(xml_url).read().decode('utf-8')

        with open(save_path, 'w') as xml:
            xml.write(xml_doc)

    def __init__(self, file_path=None):
        """Init Haar Cascade Classifier

        Create classifier instance with given XML file.
        Download XML from the web if the file does not exist.

        Args:
            file_path: the path for cascade classifier XML file
        """
        if not file_path:
            file_path = FaceDetector.get_abs_path()
        if not exists(file_path):
            FaceDetector.download_haarcascade_xml(file_path)
        self.ccc = CascadeClassifier(file_path)

    def get_faces_pos(self, img, minNeighbors=3):
        """Get the position for each detected face.

        Call detectMultiScale function in CascadeClassifier and get detection
        result.

        Args:
            img:    Matrix of the type CV_8U containing an image where
                    face is detected
            minNeighbors:   Parameter specifying how many neighbors each
                            candidate rectangle should have to retain it

        Returns:
            numpy.ndarray contains position information for each detected face.
            For each position information, it has (x, y, w, h), where:
                x - the minimum horizontal coordinate of the image position.
                y - the minimum ordinate of the image position.
                w - Image width.
                h - Image height.
        """
        return self.ccc.detectMultiScale(img, minNeighbors=minNeighbors)

    def get_faces_img(self, img, fpos=None, minNeighbors=3):
        """Get Images for each detected face.

        Crop face images from the original image.
        If face position is not given, use get_faces_pos to detect it first.

        Args:
            img:    Matrix of the type CV_8U containing an image where
                    the face is detected
            fpos:   numpy.ndarray contains position information for each
                    detected face
            minNeighbors:   Parameter specifying how many neighbors each
                            candidate rectangle should have to retain it
                            (Use only when fpos is not given)

        Returns:
            A tuple contains cropped face images.
        """
        if not fpos:
            fpos = self.get_faces_pos(img, minNeighbors=minNeighbors)
        faces = [img[y:y+h, x:x+w] for (x, y, w, h) in fpos]
        return tuple(faces)
