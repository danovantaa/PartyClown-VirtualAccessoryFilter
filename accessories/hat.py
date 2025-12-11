import math 
import cv2
from accessories.transform import rotate_png, rotate_point 
from accessories.overlay import overlay_png

def render_hat(frame, acc_img, face_points, face_angle):
    "Fungsi untuk menampilkan dan mengatur posisi kacamata"

    HAT_SCALE = 2.3       # mengatur ukuran topi
    HAT_OFFSET_Y = 13    #  mengatur tinggi topi (semakin negatif semakin naik)
    ho, wo = acc_img.shape[:2]
    
    # pivot rotasi = midpoint antara mata kanan & mata kiri (landmark 33 & 263)            
    (x1, y1) = face_points[33]
    (x2, y2) = face_points[263]
    pivot_x = (x1 + x2) // 2
    pivot_y = (y1 + y2) // 2

    # titik dahi (landmark 10)
    fx, fy = face_points[10]

    # ukuran topi mengikuti lebar dahi
    face_width = math.hypot(x2 - x1, y2 - y1)

    hat_w = int(face_width * HAT_SCALE)
    hat_h = int(hat_w * ho / wo)
    
    # Resize gambar topi sesuai dahi
    hat_img = cv2.resize(acc_img, (hat_w, hat_h))
    
    # Rotasi topi dari kemiringan kepala
    hat_img = rotate_png(hat_img, -face_angle)

    # dahi ikut diputar agar topi benar-benar mengikuti arah kepala
    rotated_fx, rotated_fy = rotate_point(pivot_x, pivot_y, fx, fy, face_angle)

    # posisi final topi
    hat_x = rotated_fx - hat_w // 2
    hat_y = rotated_fy - hat_h + HAT_OFFSET_Y

    frame = overlay_png(frame, hat_img, hat_x, hat_y)
    return frame