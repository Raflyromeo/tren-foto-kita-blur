import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision as mp_vision
import pygame

pygame.mixer.init()

NAMA_FILE_LAGU = "foto_kita_blur.mp3"

try:
    sound = pygame.mixer.Sound(NAMA_FILE_LAGU)
    print(f"[INFO] Lagu '{NAMA_FILE_LAGU}' berhasil dimuat!")
except Exception:
    sound = None
    print(f"[PERINGATAN] Lagu '{NAMA_FILE_LAGU}' tidak ditemukan, progran tetap jalan tanpa audio!")

base_options = mp_python.BaseOptions(model_asset_path='hand_landmarker.task')
options = mp_vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=mp_vision.RunningMode.VIDEO,
    num_hands=1
)
detector = mp_vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
timestamp_ms = 0
is_playing = False

print("[INFO] Tekan 'Q' atau 'ESC' untuk keluar dari program!")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    )
    timestamp_ms += 33
    result = detector.detect_for_video(mp_image, timestamp_ms)

    is_peace = False

    if result.hand_landmarks:
        lm = result.hand_landmarks[0]

        for pt in lm:
            cv2.circle(frame, (int(pt.x * w), int(pt.y*h)), 4, (0, 255, 255), -1)

        telunjuk_up = lm[8].y < lm[6].y
        tengah_up = lm[12].y < lm[10].y
        manis_up = lm[16].y < lm[14].y
        kelingking_up = lm[20].y < lm[18].y

        if telunjuk_up and tengah_up and (not manis_up) and (not kelingking_up):
            is_peace = True

    if is_peace:
        frame = cv2.GaussianBlur(frame, (45, 45), 0)

        teks = "Foto Kita Blur"
        cv2.putText(frame, teks, (w//2 - 170, h//2),
                    cv2.FONT_HERSHEY_DUPLEX, 1.3, (0, 0, 0), 6, cv2.LINE_AA)
        cv2.putText(frame, teks, (w//2 - 170, h//2),
                    cv2.FONT_HERSHEY_DUPLEX, 1.3, (255, 255, 255), 2, cv2.LINE_AA)

        if sound and not is_playing:
            sound.play(-1)
            is_playing = True

    else:
        if sound and is_playing:
            sound.stop()
            is_playing = False

    cv2.imshow("Foto Kita Blur", frame)

    key = cv2.waitKey(1) & 0xFF
    if key in (ord('q'), ord('Q'), 27):
        break

if sound:
    sound.stop()
cap.release()
cv2.destroyAllWindows()
detector.close()