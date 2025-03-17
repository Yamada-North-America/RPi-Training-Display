#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Training-Display.py
#
# This script is designed to display training videos on a Raspberry Pi based on sensor input values. 
# It uses OpenCV to handle video and image display and a custom library `lib16inpind` to read sensor values.
# Global Variables:
#     sensorValue (int): The current value read from the sensors.
#     welcomeScreen (str): Path to the welcome screen image.
#     closeDoors (str): Path to the close doors image.
#     video1 to video36 (str): Paths to the training videos.
#  
#  Copyright 2025  <Christian Stewart - Yamada North America>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import os
import cv2
import time
import lib16inpind as inp16

#Global Variables - Adjust video paths here
sensorValue = 0 #Initial sensor value - Do not change
welcomeScreen = "/mnt/Training/RPi-Training-Display/Media/Welcome-Screen.png"
closeDoors = "/mnt/Training/RPi-Training-Display/Media/Close-Doors.png"
video1 = "/mnt/Training/test_video1.mov"
video2 = "/mnt/Training/test_video2.mov"
video3 = "/mnt/Training/test_video3.mov"
video4 = "/mnt/Training/test_video4.mov"
video5 = "/mnt/Training/test_video5.mov"
video6 = "/mnt/Training/test_video6.mov"
video7 = "/mnt/Training/test_video7.mov"
video8 = "/mnt/Training/test_video8.mov"
video9 = "/mnt/Training/test_video9.mov"
video10 = "/mnt/Training/test_video10.mov"
video11 = "/mnt/Training/test_video11.mov"
video12 = "/mnt/Training/test_video12.mov"
video13 = "/mnt/Training/test_video13.mov"
video14 = "/mnt/Training/test_video14.mov"
video15 = "/mnt/Training/test_video15.mov"
video16 = "/mnt/Training/test_video16.mov"
video17 = "/mnt/Training/test_video17.mov"
video18 = "/mnt/Training/test_video18.mov"
video19 = "/mnt/Training/test_video19.mov"
video20 = "/mnt/Training/test_video20.mov"
video21 = "/mnt/Training/test_video21.mov"
video22 = "/mnt/Training/test_video22.mov"
video23 = "/mnt/Training/test_video23.mov"
video24 = "/mnt/Training/test_video24.mov"
video25 = "/mnt/Training/test_video25.mov"
video26 = "/mnt/Training/test_video26.mov"
video27 = "/mnt/Training/test_video27.mov"
video28 = "/mnt/Training/test_video28.mov"
video29 = "/mnt/Training/test_video29.mov"
video30 = "/mnt/Training/test_video30.mov"
video31 = "/mnt/Training/test_video31.mov"
video32 = "/mnt/Training/test_video32.mov"
video33 = "/mnt/Training/test_video33.mov"
video34 = "/mnt/Training/test_video34.mov"
video35 = "/mnt/Training/test_video35.mov"
video36 = "/mnt/Training/test_video36.mov"

#Plays the video located at the specified path in fullscreen mode
#
#Args:
#    video_path (str): The path to the video file. 
def play_video(video_path):
    global sensorValue
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return
    cv2.namedWindow("Training_Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Training_Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Training_Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    os.system('clear')
    update()
    #Wait for all doors to close
    if sensorValue != 0:
        close_doors(closeDoors)     
  
#Displays the welcome screen image in fullscreen mode until a sensor value changes 
#
#Args:
#    imagePath (str): The path to the welcome screen image file.     
def welcome_screen(imagePath):
    global sensorValue
    img = cv2.imread(imagePath)
    if img is None:
        print("Error: Cannot open image file.")
        return
    cv2.namedWindow("Welcome_Screen", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Welcome_Screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    #Wait for sensorValue to change
    while sensorValue == 0:
        cv2.imshow("Welcome_Screen", img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        update()
    cv2.destroyAllWindows()

#Displays the close doors image in fullscreen mode until all doors are closed
#
#Args:  
#    imagePath (str): The path to the close doors image file.
def close_doors(imagePath):
    global sensorValue
    img = cv2.imread(imagePath)
    if img is None:
        print("Error: Cannot open image file.")
        return
    cv2.namedWindow("Welcome_Screen", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Welcome_Screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    #Wait for sensorValue to return to 0
    while sensorValue != 0:
        cv2.imshow("Welcome_Screen", img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        update()
    cv2.destroyAllWindows()
   
#Converts each layer into its binary form, concatenates them, and converts the string back into an integer 
#
#Args:
#    layers (list): A list of integers representing the sensor layers.
#Returns:
#    int: The combined decimal result of the binary layers.  
def combine_layers(layers):
    binary_strings = [format(layer, '016b') for layer in layers]
    concat_binary = ''.join(reversed(binary_strings))
    decimal_result = int(concat_binary, 2)
    return decimal_result
 
#Updates sensorValue global variables by reading all 3 layers
def update():
    global sensorValue
    sensorValue = combine_layers([inp16.readAll(0), inp16.readAll(1), inp16.readAll(2)])
    #print("Dec: ", f'{sensorValue:016d}', "Bin: ", f'{sensorValue:048b}', end='\r')

#The main function that continuously checks the sensor value and displays the corresponding video or image
#
#Args:
#    args (list): Command line arguments.
def main(args):
    global sensorValue
    while True:
        match sensorValue:
            case 0:
                welcome_screen(welcomeScreen)
            case 1:
                play_video(video1)
            case 2:
                play_video(video2)
            case 4:
                play_video(video3)
            case 8:
                play_video(video4)
            case 16:
                play_video(video5)
            case 32:
                play_video(video6)
            case 64:
                play_video(video7)
            case 128:
                play_video(video8)
            case 256:
                play_video(video9)
            case 512:
                play_video(video10)
            case 1024:
                play_video(video11)
            case 2048:
                play_video(video12)
            case 4096:
                play_video(video13)
            case 8192:
                play_video(video14)
            case 16384:
                play_video(video15)
            case 32768:
                play_video(video16)
            case 65536:
                play_video(video17)
            case 131072:
                play_video(video18)
            case 262144:
                play_video(video19)
            case 524288:
                play_video(video20)
            case 1048576:
                play_video(video21)
            case 2097152:
                play_video(video22)
            case 4194304:
                play_video(video23)
            case 8388608:
                play_video(video24)
            case 16777216:
                play_video(video25)
            case 33554432:
                play_video(video26)
            case 67108864:
                play_video(video27)
            case 134217728:
                play_video(video28)
            case 268435456:
                play_video(video29)
            case 536870912:
                play_video(video30)
            case 1073741824:
                play_video(video31)
            case 2147483648:
                play_video(video32)
            case 4294967296:
                play_video(video33)
            case 8589934592:
                play_video(video34)
            case 17179869184:
                play_video(video35)
            case 34359738368:
                play_video(video36)
            case _:
                close_doors(closeDoors)
        update()
        time.sleep(0.10)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))