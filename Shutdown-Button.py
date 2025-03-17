import RPi.GPIO as GPIO
import time
import os

# Pin configuration
BUTTON_PIN = 26  # GPIO 26 (Pin 37)
HOLD_TIME = 3  # Time in seconds to hold the button to shut down

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle_button(channel):
    start_time = time.time()
    while GPIO.input(BUTTON_PIN) == GPIO.LOW:
        if time.time() - start_time >= HOLD_TIME:
            print("Shutdown button held, shutting down Raspberry Pi...")
            os.system("sudo shutdown -h now")
            return
        time.sleep(0.1)  # Polling interval
    
    print("Button pressed briefly, rebooting Raspberry Pi...")
    os.system("sudo reboot")

# Detect button press
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=handle_button, bouncetime=200)

try:
    print("Monitoring shutdown button. Press briefly to reboot, hold for", HOLD_TIME, "seconds to shut down.")
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
