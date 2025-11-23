# 🤡 Party Clown - Virtual Accessory Filter 🤡

## 📝 Project Description

Party Clown is a facial recognition system that adds virtual accessories to users in real time. The system utilizes facial landmark detection technology to track the user's face and head position, then applies graphical objects such as hats, glasses, and other party decorations that can be selected interactively. This project is designed to provide an engaging and entertaining visual experience with a simple interface and fast response. This application has the potential to be implemented as an entertainment feature on multimedia platforms, creative camera filters, and interactive social media content.

## 👥Team Members

| Name                      | NIM       | Github Profile                                           |
| ------------------------- | --------- | -------------------------------------------------------- |
| Zefanya Danovanta Tarigan | 122140101 | [@danovantaa](https://github.com/danovantaa)             |
| Gabriella Natalya Rumapea | 122140056 | [@gabriellarumapea](https://github.com/gabriellarumapea) |
| Joy Daniella V.S          | 122140039 | [@jdaniella039](https://github.com/jdaniella039)         |

## 🔧 Tools

- Mediapipe = untuk mendeteksi landmark wajah (FaceMesh) dan landmark tangan (HandLandmark).
- OpenCV = untuk membaca frame video, melakukan konversi warna (BGR → RGB)
- Pygame = untuk memainkan backsound
- Pillow = untuk konversi image hasil OpenCV menjadi format yang dapat ditampilkan di Tkinter

## 📂 Struktur Folder
```bash
├── requirements.txt
├── main.py
├── gui.py
├── camera.py
├── landmark.py
├── backsound.py
├── requirements.txt
└── README.md
└── Backsound/
    └── game-8-bit.mp3
└── Images/
    └── ...
```

## 🚀 Instalasi

### **Prasyarat**

- Python **3.8 atau lebih tinggi**
- Webcam (untuk face & hand tracking)
- Sistem Operasi:
  - Windows
  - macOS
  - Linux

---

### **1. Clone Repository**

```bash
git clone https://github.com/danovantaa/PartyClown-VirtualAccessoryFilter.git
cd PartyClown-VirtualAccessoryFilter
```

### **2. Buat Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

#macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Depedensi**

```bash
pip install -r requirements.txt
```

---

## Penggunaan

### **1. Jalankan Aplikasi**

```bash
python main.py
```

### **2. Pastikan device memiliki webcam**

### **3. Klik Tombol start maka backsound dan webcam akan jalan**

### **4. Arahkan tangan anda ke bagian asset yang berada di atas kanan dan sesuaikan tangan ke gambar aksesoris yang ingin dipakai**

### **5. Klik tombol stop jika ingin mengakhiri program**

## 📑Weekly Logbook

| Date             | Activity                 | Result                                                                 |
| ---------------- | ------------------------ | ---------------------------------------------------------------------- |
| 29 October 2025  | Create Repository Github | Repository PartyClown-VirtualAccessoryFilter                           |
| 1 November 2025  | Upload Asset             | Folder Backsound & Images                                              |
| 23 November 2025 | Create GUI & Landmarks   | Membuat landmarks pada bagian wajah dan tangan dan GUI agar interaktif |
