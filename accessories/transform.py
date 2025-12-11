import cv2
import math

def get_face_angle(p1, p2):
    """
    Menghitung sudut rotasi wajah berdasarkan dua titik landmark.
    p1 = titik landmark pertama (x1, y1)
    p2 = titik landmark kedua (x2, y2)
    """
    
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle

def rotate_png(png, angle):
    """
    Merotasi gambar PNG (dengan transparansi) dengan sudut tertentu.
    png   = gambar (BGRA)
    angle = sudut rotasi dalam derajat (positif = searah jarum jam)
    """
    
    h, w = png.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    #  rotasi PNG dengan warpAffine
    rotated = cv2.warpAffine(
        png, M, (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0, 0, 0, 0)
    )
    return rotated

def rotate_point(cx, cy, px, py, angle_deg):
    """
    rotasi titik (px, py) pada pusat rotasi (cx, cy) sebesar angle_deg.
    """
    
    angle = math.radians(angle_deg)
    s = math.sin(angle)
    c = math.cos(angle)

    px -= cx
    py -= cy

    xnew = px * c - py * s
    ynew = px * s + py * c

    px = xnew + cx
    py = ynew + cy
    return int(px), int(py)