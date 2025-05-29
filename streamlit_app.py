import streamlit as st
import cv2
from gesture_module import HandDetector

st.title("✋ Hand Gesture Recognition App")
st.write("Show your hand to the camera!")

detector = HandDetector()
FRAME_WINDOW = st.image([])

run = st.checkbox('Start Camera')

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.error("Failed to capture image")
        break

    frame, gesture = detector.detect_gesture(frame)
    st.write(f"Detected Gesture: **{gesture}**")
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
