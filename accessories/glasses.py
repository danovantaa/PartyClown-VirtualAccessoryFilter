import math 
import cv2
from accessories.transform import rotate_png 
from accessories.overlay import overlay_png

def render_glasses(frame, acc_img, face_points, face_angle):
    "Fungsi untuk menampilkan dan mengatur posisi kacamata"
    # tinggi (ho)  lebar (wo) dari kacamata (PNG)
    ho, wo = acc_img.shape[:2]
    
    # 33 = mata kanan, 263 = mata kiri
    (x1, y1) = face_points[33]
    (x2, y2) = face_points[263]

    # lebar wajah dari jarak kedua mata
    width = math.hypot(x2 - x1, y2 - y1)
    gw = int(width * 1.8)
    gh = int(gw * ho / wo)
    
    # Resize gambar kacamata sesuai wajah
    glass = cv2.resize(acc_img, (gw, gh))
    
    # Rotasi kacamata dari kemiringan kepala
    glass = rotate_png(glass, -face_angle)
    
    # pusat lokasi kacamata
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    
    frame = overlay_png(frame, glass, cx - gw // 2, cy - gh // 2)
    return frame