from tkinter import *
from PIL import Image, ImageTk

def test():
    import cv2
    import mediapipe as mp
    import numpy as np

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    # 웹캠, 영상 파일의 경우 이것을 사용하세요.:
    cap = cv2.VideoCapture(0)

    # 이미지를 로드하고 크기를 조정합니다.
    image = cv2.imread('image.jpg')  # 이미지 파일의 경로를 지정하세요.
    if image is not None:
        # 이미지 크기 조정
        target_width, target_height = 500, 500  # 원하는 이미지 크기로 조정하세요
        image = cv2.resize(image, (target_width, target_height))

    with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("카메라를 찾을 수 없습니다.")
                # 동영상을 불러올 경우는 'continue' 대신 'break'를 사용합니다.
                continue

            # 필요에 따라 성능 향상을 위해 이미지 작성을 불가능함으로 기본 설정합니다.
            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame)

            # 포즈 주석을 이미지 위에 그립니다.
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

            # 이미지를 프레임에 합성합니다.
            if image is not None:
                frame[30:30 + target_height, 30:30 + target_width] = image

            # 보기 편하게 이미지를 좌우 반전합니다.
            cv2.imshow('MediaPipe Pose', cv2.flip(frame, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()


def display_image():
    image_path = "start.png"  # 이미지 파일의 경로
    w = Tk()
    w.title("start")

    # Open the image using Pillow (PIL)
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    btn = Button(w, image=photo, command=test)  # Specify the test function for the button click
    btn.pack(expand=0, anchor=CENTER)

    w.mainloop()

# 함수 호출
display_image()
