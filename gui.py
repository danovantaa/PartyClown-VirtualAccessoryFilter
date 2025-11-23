import cv2
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

from camera import Camera
from landmark import FaceLandmark
from landmark import HandLandmark
from backsound import stop_backsound

class CameraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Camera")

        # Landmark detektor
        self.face = FaceLandmark()
        self.hand = HandLandmark()

        # Kamera
        try:
            self.cam = Camera(0)
        except:
            self.cam = Camera(1)

        # Area Video
        self.video_label = Label(self.root)
        self.video_label.pack()

        # Tombol STOP
        self.stop_btn = Button(
            self.root,
            text="STOP",
            font=("Arial", 12, "bold"),
            bg="red",
            fg="white",
            relief="flat",
            command=self.stop_camera
        )
        self.stop_btn.pack(pady=10)

        self.update_frame()
        self.root.protocol("WM_DELETE_WINDOW", self.stop_camera)

    def update_frame(self):
        frame = self.cam.get_frame()
        if frame is not None:

            # Deteksi wajah
            frame = self.face.process(frame)

            # Deteksi jari
            frame = self.hand.process(frame)

            # Convert ke Tkinter image
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def stop_camera(self):
        stop_backsound()
        self.cam.release()
        self.root.destroy()
