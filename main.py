import tkinter as tk
from tkinter import Canvas
from gui import CameraGUI
from backsound import play_backsound

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Utama")
        self.root.geometry("500x350")
        self.root.configure(bg="#1e1e1e")

        # NAMA TUBES
        title = tk.Label(
            root, 
            text="Party Clown Filter",
            font=("Poppins", 24, "bold"), 
            fg="white", 
            bg="#1e1e1e"
        )
        title.pack(pady=40)

        # Tombol Start 
        self.start_btn = tk.Button(
            root,
            text="START CAMERA",
            font=("Poppins", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief="flat",
            width=15,
            height=2,
            command=self.open_camera
        )
        self.start_btn.pack(pady=20)

        # Hover Effect
        self.start_btn.bind("<Enter>", lambda e: self.start_btn.config(bg="#58d164"))
        self.start_btn.bind("<Leave>", lambda e: self.start_btn.config(bg="#4CAF50"))

    def open_camera(self):
        # Play Backsound
        play_backsound("Backsound/game-8-bit.mp3")

        # Tutup menu utama
        self.root.destroy()

        # Masuk kamera
        cam_window = tk.Tk()
        CameraGUI(cam_window)
        cam_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
