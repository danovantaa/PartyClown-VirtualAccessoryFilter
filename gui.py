import cv2
from tkinter import Label, Button
from PIL import Image, ImageTk
import os
from camera import Camera
import time
from landmark import FaceLandmark, HandLandmark
from backsound import stop_backsound
from accessories.overlay import overlay_png
from accessories.transform import get_face_angle
from accessories.hat import render_hat
from accessories.glasses import render_glasses
from accessories.mustache import render_mustache
from utils.resizeimg import resize_with_aspect_ratio
from utils.handutils import hand_touching_rect

BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, "Images")

class CameraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Camera")

        # landmark detektor
        self.face = FaceLandmark()
        self.hand = HandLandmark()

        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))
        
        # kamera
        try:
            self.cam = Camera(0)
        except:
            self.cam = Camera(1)
            
        self.last_touch_time = 0
        self.touch_delay = 0.5
        accessories_info = [
            ("winter", os.path.join(IMG_DIR, "winter-hat.png"), "hat"),
            ("gradu",  os.path.join(IMG_DIR, "gradu-hat.png"),  "hat"),
            ("beach",  os.path.join(IMG_DIR, "beach-hat.png"),  "hat"),
            ("witch",  os.path.join(IMG_DIR, "witch-hat.png"),  "hat"),

            ("rich",   os.path.join(IMG_DIR, "rich-sunglasses.png"), "glasses"),
            ("love",   os.path.join(IMG_DIR, "love-sunglasses.png"), "glasses"),
            ("3D",     os.path.join(IMG_DIR, "3d-sunglasses.png"),   "glasses"),
            ("8bit",   os.path.join(IMG_DIR, "8bit-sunglasses.png"), "glasses"),

            ("kumis",  os.path.join(IMG_DIR, "kumis.png"), "kumis")
        ]

        self.accessories = {}
        start_x = 10
        start_y = 10
        spacing = 70  # jarak antar icon

        for i, (key, path, kind) in enumerate(accessories_info):
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # BGRA
            if img is None:
                raise FileNotFoundError(f"Gambar aksesori tidak ditemukan: {path}")

            preview = cv2.resize(img, (65, 65), interpolation=cv2.INTER_AREA)
            pos = (start_x + i * spacing, start_y)  # posisi icon di pojok 

            self.accessories[key] = {
                "img": img,         # gambar full
                "preview": preview, # icon kecil
                "pos": pos,         # posisi icon
                "kind": kind,       # nama accessories
            }

        # Tidak ada topi yang aktif di awal
        self.active_accessories   = set()

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
        if frame is None:
            self.root.after(10, self.update_frame)
            return

        frame = cv2.flip(frame, 1) # mirror effect
             
        # Deteksi landmark
        frame, face_points = self.face.process(frame)
        frame, hand_points = self.hand.process(frame)

        face_angle = 0
        if 33 in face_points and 263 in face_points:
            (x1, y1) = face_points[33]
            (x2, y2) = face_points[263]
            face_angle = get_face_angle((x1, y1), (x2, y2))

        for key, info in self.accessories.items():
            px, py = info["pos"]
            frame = overlay_png(frame, info["preview"], px, py)

        for key, info in self.accessories.items():
            px, py = info["pos"]
            ph, pw = info["preview"].shape[:2]
            current_time = time.time()

            if hand_touching_rect(hand_points, px, py, pw, ph):
                if current_time - self.last_touch_time > self.touch_delay:
                    kind = info["kind"]

                    if key in self.active_accessories:
                        self.active_accessories.remove(key)
                    else:
                        to_remove = [
                            k for k in self.active_accessories
                            if self.accessories[k]["kind"] == kind
                        ]
                        for k in to_remove:
                            self.active_accessories.remove(k)

                        self.active_accessories.add(key)

                    self.last_touch_time = current_time
                break

        h, w, _ = frame.shape
        
        # Render aksesori
        for acc_key in self.active_accessories:
            info = self.accessories[acc_key]
            acc_img = info["img"]
            kind = info["kind"]
            
            if kind == "hat" and 10 in face_points and 33 in face_points and 263 in face_points:
                frame = render_hat(frame, acc_img, face_points, face_angle)

            elif kind == "glasses" and 33 in face_points and 263 in face_points:
                frame = render_glasses(frame, acc_img, face_points, face_angle)

            elif kind == "kumis" and 13 in face_points and 14 in face_points and 61 in face_points and 291 in face_points:
                frame = render_mustache(frame, acc_img, face_points, face_angle)

        win_w = self.root.winfo_width()
        win_h = self.root.winfo_height() - 70 # space untuk tombol STOP
        if win_w > 0 and win_h > 0:
            frame = resize_with_aspect_ratio(frame, win_w, win_h)

        # Konversi frame BGR → RGB → ImageTk
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def stop_camera(self):
        """Hentikan backsound, matikan kamera, dan tutup window."""
        stop_backsound()
        self.cam.release()
        self.root.destroy()
