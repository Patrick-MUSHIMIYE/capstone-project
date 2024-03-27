import tensorflow as tf
from io import BytesIO
import nudenet

def is_nude(image_path):
    # Initialize NudeDetector
    nude_detector = nudenet.NudeDetector()
    # Perform nudity detection
    detections = nude_detector.detect(image_path)
    # Check if any of the detections correspond to nudity-related labels
    for detection in detections:
        if detection['class'] in ["FEMALE_GENITALIA_COVERED","BUTTOCKS_EXPOSED","FEMALE_BREAST_EXPOSED",
                                  "FEMALE_GENITALIA_EXPOSED","MALE_BREAST_EXPOSED","ANUS_EXPOSED","FEET_EXPOSED",
                                  "BELLY_COVERED","FEET_COVERED","ARMPITS_COVERED","ARMPITS_EXPOSED","BELLY_EXPOSED",
                                  "MALE_GENITALIA_EXPOSED","ANUS_COVERED","FEMALE_BREAST_COVERED","BUTTOCKS_COVERED",]:
            return True  # Image contains nudity
    return False  # Image is safe