#!/usr/bin/python3

from picamera2 import Picamera2, Preview
import numpy as np
import time

picam2 = Picamera2()
picam2.configure(picam2.preview_configuration())
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(1)

overlay = np.zeros((300, 400, 4), dtype=np.uint8)
overlay[:150, 200:] = (255, 0, 0, 64)
overlay[150:, :200] = (0, 255, 0, 64)
overlay[150:, 200:] = (0, 0, 255, 64)

picam2.set_overlay(overlay)
time.sleep(2)
