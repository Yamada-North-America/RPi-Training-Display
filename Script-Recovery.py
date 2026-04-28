import subprocess
import time
import signal
import sys

SCRIPT_PATH = "/mnt/Training/RPi-Training-Display/Training-Display.py"
CHECK_INTERVAL = 30
PROCESS_NAME = "Training-Display.py"

def is_process_running():
    """Check if the Training Display process is running."""
    try:
        result = subprocess.run(
            ["pgrep", "-f", PROCESS_NAME],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error checking process: {e}")
        return False

def start_process():
    """Start the Training Display process."""
    try:
        subprocess.Popen(
            f"python3 {SCRIPT_PATH} >/dev/null 2>&1 &",
            shell=True
        )
        print(f"Started {PROCESS_NAME}")
    except Exception as e:
        print(f"Error starting process: {e}")

def signal_handler(sig, frame):
    """Handle graceful shutdown."""
    print("Shutting down...")
    sys.exit(0)

def main():
    """Monitor and restart the process."""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    print(f"Monitoring {PROCESS_NAME}...")
    
    while True:
        if not is_process_running():
            print(f"{PROCESS_NAME} not running. Restarting...")
            start_process()
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()