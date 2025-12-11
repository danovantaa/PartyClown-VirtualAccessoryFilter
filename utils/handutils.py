def hand_touching_rect(hand_points, x, y, w, h):
    """
    cek  titik-titik tangan (hasil landmark Mediapipe)
    menyentuh atau berada di dalam area persegi (rectangle) tertentu.

    hand_points : list berisi koordinat (px, py) dari landmark tangan
    x, y        : posisi kiri-atas rectangle
    w, h        : lebar dan tinggi rectangle
    """
    
    if not hand_points:  # None atau list kosong
        return False  # tidak ada yang menyentuh

    for px, py in hand_points:
        if x <= px <= x + w and y <= py <= y + h:
            return True # ada titik tangan masuk ke area rect

    return False
