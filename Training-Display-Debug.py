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

import configparser
import os
import mpv
import time
import random
import tkinter as tk
import lib16inpind as inp16

#Global Variables - Adjust video paths here
sensorValue = 0 #Initial sensor value - Do not change
# Load paths from configuration file
config = configparser.ConfigParser()
config.read('/mnt/Training/RPi-Training-Display/config.ini')
fallbackVideo = config.get('Videos', 'fallbackVideo')
fallbackImage = config.get('Images', 'fallbackImage')

buttonPressed = config.get('Images', 'buttonPressed', fallback=fallbackImage)
welcomeScreen = config.get('Videos', 'welcomeScreen', fallback=fallbackVideo)
video1 = config.get('Videos', 'video1', fallback=fallbackVideo)
video2 = config.get('Videos', 'video2', fallback=fallbackVideo)
video3 = config.get('Videos', 'video3', fallback=fallbackVideo)
video4 = config.get('Videos', 'video4', fallback=fallbackVideo)
video5 = config.get('Videos', 'video5', fallback=fallbackVideo)
video6 = config.get('Videos', 'video6', fallback=fallbackVideo)
video7 = config.get('Videos', 'video7', fallback=fallbackVideo)
video8 = config.get('Videos', 'video8', fallback=fallbackVideo)
video9 = config.get('Videos', 'video9', fallback=fallbackVideo)
video10 = config.get('Videos', 'video10', fallback=fallbackVideo)
video11 = config.get('Videos', 'video11', fallback=fallbackVideo)
video12 = config.get('Videos', 'video12', fallback=fallbackVideo)
video13 = config.get('Videos', 'video13', fallback=fallbackVideo)
video14 = config.get('Videos', 'video14', fallback=fallbackVideo)
video15 = config.get('Videos', 'video15', fallback=fallbackVideo)
video16 = config.get('Videos', 'video16', fallback=fallbackVideo)
video17 = config.get('Videos', 'video17', fallback=fallbackVideo)
video18 = config.get('Videos', 'video18', fallback=fallbackVideo)
video19 = config.get('Videos', 'video19', fallback=fallbackVideo)
video20 = config.get('Videos', 'video20', fallback=fallbackVideo)
video21 = config.get('Videos', 'video21', fallback=fallbackVideo)
video22 = config.get('Videos', 'video22', fallback=fallbackVideo)
video23 = config.get('Videos', 'video23', fallback=fallbackVideo)
video24 = config.get('Videos', 'video24', fallback=fallbackVideo)
video25 = config.get('Videos', 'video25', fallback=fallbackVideo)
video26 = config.get('Videos', 'video26', fallback=fallbackVideo)
video27 = config.get('Videos', 'video27', fallback=fallbackVideo)
video28 = config.get('Videos', 'video28', fallback=fallbackVideo)
video29 = config.get('Videos', 'video29', fallback=fallbackVideo)
video30 = config.get('Videos', 'video30', fallback=fallbackVideo)
video31 = config.get('Videos', 'video31', fallback=fallbackVideo)
video32 = config.get('Videos', 'video32', fallback=fallbackVideo)
video33 = config.get('Videos', 'video33', fallback=fallbackVideo)
video34 = config.get('Videos', 'video34', fallback=fallbackVideo)
video35 = config.get('Videos', 'video35', fallback=fallbackVideo)
video36 = config.get('Videos', 'video36', fallback=fallbackVideo)
qcorner = config.get('Videos', 'qcorner', fallback=fallbackVideo)

#Plays the video located at the specified path in fullscreen mode
#
#Args:
#    video_path (str): The path to the video file. 
def play_video(video_path):
    global sensorValue
    player = mpv.MPV(fullscreen=True, ytdl=False)
    player.play(video_path)
    
    while player.core_idle == False:
        update()
        time.sleep(0.1)
    
    player.quit()
    os.system('clear')
    
    #Wait for all doors to close
    if sensorValue != 0:
        display_image(buttonPressed)

#Plays the video located at the specified path in fullscreen mode and waits for a sensor value change to exit
#
#Args:
#    video_path (str): The path to the video file.        
def play_screensaver(video_path):
    global sensorValue
    player = mpv.MPV(fullscreen=True, ytdl=False, loop=True)
    player.play(video_path)
    
    prev_value = sensorValue
    while sensorValue == 0:
        update()
        time.sleep(0.1)
    
    player.quit()
    os.system('clear')
    
#Displays the passed image in fullscreen mode until a sensor value changes 
#
#Args:
#    imagePath (str): The path to the welcome screen image file.     
def display_image(imagePath):
    global sensorValue
    player = mpv.MPV(fullscreen=True, ytdl=False)
    player.play(imagePath)
    
    prev_value = sensorValue
    while True:
        update()
        if sensorValue != prev_value:
            break
        time.sleep(0.1)
    
    player.quit()
    
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
    #sensorValue = combine_layers([inp16.readAll(0), inp16.readAll(1), inp16.readAll(2)])
    sensorValue = 0#random.randint(0, 10)
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
                play_screensaver(welcomeScreen)
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
            case 68719476736:
                play_video(qcorner)
            case 137438953472:
                os.system("sudo reboot")
            case _:
                display_image(buttonPressed)
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))