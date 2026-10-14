# tren-foto-kita-blur

Program deteksi gestur tangan (peace sign) menggunakan OpenCV dan MediaPipe Hand Landmarker untuk menerapkan efek blur pada video kamera serta memutar audio pengiring.

## Fitur
- Deteksi gestur tangan (peace sign / dua jari) secara realtime menggunakan webcam.
- Penerapan efek Gaussian Blur saat gestur terdeteksi.
- Penambahan teks "Foto Kita Blur" pada layar video.
- Pemutaran file audio `foto_kita_blur.mp3` secara otomatis saat efek aktif.

## Prasyarat
Pastikan Python sudah terinstal di komputer. Install pustaka yang diperlukan:
```bash
pip install opencv-python mediapipe pygame
```

## Cara Menjalankan
1. Pastikan file model `hand_landmarker.task` dan file audio `foto_kita_blur.mp3` berada dalam satu direktori dengan skrip `foto_kita_blur.py`.
2. Jalankan skrip melalui terminal:
   ```bash
   python foto_kita_blur.py
   ```
3. Arahkan dua jari (jari telunjuk dan jari tengah membentuk peace sign) ke arah webcam untuk memicu efek blur dan audio.
4. Tekan tombol `Q` atau `ESC` untuk menutup program.
