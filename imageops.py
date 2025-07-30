import cv2
import numpy as np

def imgRotateClockwise(image):
    rotatedImage = image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    return rotatedImage

def imgRotateCounterClockwise(image):
    rotatedImage = image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return rotatedImage
