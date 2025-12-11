import cv2

def overlay_png(bg, fg, x, y):
    """
    Overlay gambar PNG (bg: BGR, fg: BGRA) ke posisi (x, y) di bg.
    x, y = posisi kiri-atas fg di bg.
    """
    bh, bw = bg.shape[:2]
    fh, fw = fg.shape[:2]

    # Cek batas biar gak keluar frame
    if x >= bw or y >= bh:
        return bg
    if x + fw <= 0 or y + fh <= 0:
        return bg

    # Clipping ROI
    x1 = max(x, 0)
    y1 = max(y, 0)
    x2 = min(x + fw, bw)
    y2 = min(y + fh, bh)

    fg_x1 = x1 - x
    fg_y1 = y1 - y
    fg_x2 = fg_x1 + (x2 - x1)
    fg_y2 = fg_y1 + (y2 - y1)

    roi = bg[y1:y2, x1:x2]
    fg_roi = fg[fg_y1:fg_y2, fg_x1:fg_x2]

    if fg_roi.shape[2] == 4:
        b, g, r, a = cv2.split(fg_roi)
        alpha = a.astype(float) / 255.0
        alpha = alpha[..., None]

        fg_rgb = cv2.merge((b, g, r)).astype(float)
        bg_rgb = roi.astype(float)

        blended = alpha * fg_rgb + (1 - alpha) * bg_rgb
        bg[y1:y2, x1:x2] = blended.astype("uint8")
        
    else:
        bg[y1:y2, x1:x2] = fg_roi[:, :, :3]

    return bg