import cv2

class Camera:
    def __init__(self, index=0):
        # Membuka kamera
        self.cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

        if not self.cap.isOpened():
            raise ValueError("Tidak bisa membuka kamera. Coba Devie lain.")

    def get_frame(self):
        """Mengambil satu frame dari kamera"""
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        """Menutup kamera"""
        if self.cap.isOpened():
            self.cap.release() #  # Tutup kamera