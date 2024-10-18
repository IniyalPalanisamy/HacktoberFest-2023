#!/usr/bin/env python
# coding: utf-8

import mediapipe as mp
import cv2 
import time
from tqdm import tqdm  # Corrected import for tqdm

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Initialize the pose model
pose = mp_pose.Pose(static_image_mode=False,
                    model_complexity=2,
                    smooth_landmarks=True,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)

# Function to process each video frame
def process_frame(img):
    start_time = time.time()
    
    h, w = img.shape[:2]
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_RGB)
    
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        for i in range(33):  # Traverse 33 keypoints
            cx = int(results.pose_landmarks.landmark[i].x * w)
            cy = int(results.pose_landmarks.landmark[i].y * h)
            radius = 5
            
            # Color coding for different body parts
            if i == 0:  # Nose
                color = (0, 0, 255)
            elif i in [11, 12]:  # Shoulders
                color = (223, 155, 6)
            elif i in [23, 24]:  # Hips
                color = (1, 240, 255)
            elif i in [13, 14]:  # Elbows
                color = (140, 47, 240)
            elif i in [25, 26]:  # Knees
                color = (0, 0, 255)
            elif i in [15, 16, 27, 28]:  # Wrists and Ankles
                color = (223, 155, 60)
            elif i in [17, 19, 21]:  # Left Hand
                color = (94, 218, 121)
            elif i in [18, 20, 22]:  # Right Hand
                color = (16, 144, 247)
            elif i in [27, 29, 31]:  # Left Foot
                color = (29, 123, 243)
            elif i in [28, 30, 32]:  # Right Foot
                color = (193, 182, 255)
            elif i in [9, 10]:  # Mouth
                color = (205, 235, 255)
            elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # Eyes and Cheeks
                color = (94, 218, 121)
            else:  # Other keypoints
                color = (0, 255, 0)

            img = cv2.circle(img, (cx, cy), radius, color, -1)
    else:
        scaler = 1
        failure_str = 'NO Person'
        img = cv2.putText(img, failure_str, (25 * scaler, 100 * scaler), cv2.FONT_HERSHEY_SIMPLEX, 1.25 * scaler, (255, 0, 0), 2)

    end_time = time.time()
    FPS = 1 / (end_time - start_time)
    scaler = 1
    img = cv2.putText(img, 'FPS  ' + str(int(FPS)), (25 * scaler, 50 * scaler), cv2.FONT_HERSHEY_SIMPLEX, 1.25 * scaler, (223, 155, 6), 2)

    return img

# Function to generate video with pose detection
def generate_video(input_path):
    filehead = input_path.split('/')[-1]
    output_path = "out-" + filehead
    
    print('Video starts processing', input_path)
    
    # Get the total number of frames in the video
    cap = cv2.VideoCapture(input_path)
    frame_count = 0
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame_count += 1
    cap.release()
    print('The total number of video frames is', frame_count)
    
    cap = cv2.VideoCapture(input_path)
    frame_size = (int(cap.get(cv2.C
