from tkinter import *
from PIL import Image, ImageTk

def test():
    # window.destroy()
    print("Button clicked! Running the test function.")

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
