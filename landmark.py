import cv2
import mediapipe as mp

class FaceLandmark: 
    """"
    Deteksi Landmark Wajah pada Frame
    """
    def __init__(self):
        self.mp_face = mp.solutions.face_mesh
        self.face_mesh = self.mp_face.FaceMesh(
            max_num_faces=1,        # deteksi 1 wajah
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.face_mesh.process(rgb)

        face_points = {}  # {index: (x, y)}

        if result.multi_face_landmarks:
            h, w, _ = frame.shape
            for face_landmarks in result.multi_face_landmarks:
                for idx, lm in enumerate(face_landmarks.landmark):
                    x = int(lm.x * w)
                    y = int(lm.y * h)
                    face_points[idx] = (x, y)

        return frame, face_points

class HandLandmark:
    """"
    Deteksi Landmark Tangan pada Frame
    """
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,            # deteksi 2 tangan
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        hand_points = []  # list of (x, y) semua titik tangan

        if result.multi_hand_landmarks:
            h, w, _ = frame.shape
            for hand in result.multi_hand_landmarks:
                for lm in hand.landmark:
                    x = int(lm.x * w)
                    y = int(lm.y * h)
                    hand_points.append((x, y))
        return frame, hand_points