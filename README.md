# YNA Training Department - Raspberry Pi Display
This project is designed to display training videos on a Raspberry Pi based on sensor input values. It uses OpenCV to handle video and image display and a custom library `lib16inpind` to read sensor values.

## Features
- Displays a welcome screen until a sensor value changes.
- Plays specific training videos based on sensor input.
- Displays a "close doors" image until all doors are closed.

## Requirements
- Raspberry Pi
- 3 Sequent Microsystems 16-opto isolated input HATs
- OpenCV
- `lib16inpind` library for reading sensor values
- Git on local PC

## Installation
1. Clone the repository to the desired network folder:
    ```bash
    git clone https://github.com/Yamada-North-America/RPi-Training-Display.git
    ```

## Update
1. Update repository (From inside RPi-Training-Display folder)
    ```bash
    git pull
    ```

## Raspberry Pi Setup
1. Enable I2C input (Interface Options)
    ```bash
    sudo raspi-config
    ```
2. Add mount folder
    ```bash
    sudo mkdir /mnt/Training
    ```
3. Create credential file
    ```bash
    sudo nano /etc/win-credentials
    ```
    Copy the following to the new file (Ask IT for details)
    ```bash
    username=REPLACE WITH USERNAME
    password=REPLACE WITH PASSWORD
    domain=REPLACE WITH DOMAIN
    ```
4. Set mount on boot
    ```bash
    sudo nano /etc/fstab
    ```
    Add the following line to the file
    ```bash
    # <file system>             <dir>          <type> <options>                                                   <dump>  <pass>
    //WIN_SHARE_IP/share_name  /mnt/Training  cifs  credentials=/etc/win-credentials,file_mode=0755,dir_mode=0755 0       0
    ```
    Apply the changes to fstab file
    ```bash
    sudo systemctl daemon-reload
    ```
    Test mount
    ```bash
    sudo mount /mnt/Training
    ```
5. Install the required libraries
    ```bash
    sudo pip3 install opencv-contrib-python SM16inpind --break-system-packages
    ```
6. Create autostart file
    ```bash
    sudo nano ~/.config/labwc/autostart
    ```
    Copy the following to the new file
    ```bash
    # Starts the Training Display python script
    python3 /mnt/Training/RPi-Training-Display/Training-Display.pi >/dev/null 2>&1 &
    # Starts the script to monitor the button on the Raspberry Pi HATs
    python3 /mnt/Training/RPi-Training-Display/Shutdown-Button.pi >/dev/null 2>&1 &
    ```
8. Restart Raspberry Pi
    ```bash
    reboot
    ```

## Usage


## Author
Christian Stewart - Yamada North America
