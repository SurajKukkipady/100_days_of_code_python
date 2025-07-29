import pyautogui
from PIL import ImageGrab
import time

# Coordinates to check for obstacle (You might need to adjust these based on screen resolution and Chrome window position)
DETECTION_REGION = (300, 420, 350, 460)  # (left, top, right, bottom)

def is_obstacle_in_path():
    screen = ImageGrab.grab(bbox=DETECTION_REGION)  # Capture a small region ahead of dino
    grayscale = screen.convert('L')  # Convert to grayscale
    pixels = grayscale.getdata()

    # If any pixel is dark (likely obstacle), trigger jump
    for pixel in pixels:
        if pixel < 100:  # 0 (black) to 255 (white)
            return True
    return False

def jump():
    pyautogui.press("space")

def main():
    print("Starting Dino Bot in 3 seconds... Switch to Chrome Dino game.")
    time.sleep(3)
    print("Dino Bot running... Press Ctrl+C to stop.")

    while True:
        if is_obstacle_in_path():
            jump()
            time.sleep(0.1)  # Small delay to avoid double jumping
        # Optional: Add sleep to reduce CPU usage
        time.sleep(0.01)

if __name__ == "__main__":
    main()
