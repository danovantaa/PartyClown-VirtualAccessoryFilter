import math 
import cv2
from accessories.transform import rotate_png, rotate_point 
from accessories.overlay import overlay_png

def render_mustache(frame, acc_img, face_points, face_angle):
    "Fungsi untuk menampilkan dan mengatur posisi kumis"

    MUSTACHE_Y_OFFSET = -10
    ho, wo = acc_img.shape[:2]
    
    # center bibir
    (ux, uy) = face_points[13]
    (lx, ly) = face_points[14]
    mx = (ux + lx) // 2
    my = (uy + ly) // 2

    # mulut kiri & kanan 
    (ml_x, ml_y) = face_points[61]
    (mr_x, mr_y) = face_points[291]

    mouth_width = math.hypot(mr_x - ml_x, mr_y - ml_y)

    # scaling
    mw = int(mouth_width * 1.3)    # diperbesar 
    mh = int(mw * ho / wo)

    mustache = cv2.resize(acc_img, (mw, mh))
    mustache = rotate_png(mustache, -face_angle)

    # rotasi pusat mulut 
    cx = (ml_x + mr_x) // 2
    cy = (ml_y + mr_y) // 2

    mx2, my2 = rotate_point(cx, cy, mx, my, face_angle)

    frame = overlay_png(frame, mustache, mx2 - mw // 2, my2 - mh // 2 + MUSTACHE_Y_OFFSET)  
    return frame