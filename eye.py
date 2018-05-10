#!/usr/local/bin/python3

import numpy as np
import cv2

class eyes:
    'camera related routines'
    dbg = 0
    deviceID = -1
    info = {}
    currentFrame = []
    lastFrame = []
    def __init__(self, deviceID=0, dbg=0):
        self.cap = cv2.VideoCapture(self.deviceID)
        if ( self.cap ):
            self.deviceID = deviceID
            self.dbg = dbg
    def getFrame(self):
        ret, frame  = self.cap.read()
        if ret:
            self.lastFrame = self.currentFrame
            self.currentFrame = frame
            return 1
        else:
            return 0
