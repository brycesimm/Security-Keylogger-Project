# Security-Keylogger-Project

<b>WatchDogAntivirus.exe and WatchDogAntivirusUnprotected.exe are NOT antiviruses.</b> </br>
<b>Both executables run keyloggers which will capture information from the machine they run on
and email them to a gmail account set up for this project.</b> </br> </br>
<b>DO NOT USE THIS SOFTWARE TO CAUSE HARM TO ANYONE OR THEIR PROPERTY. THESE KEYLOGGERS ARE MEANT TO BE HARMLESS, BUT THEY CAN LEAD TO INVASION OF PRIVACY IF USED WITHOUT CONSENT. THIS PROJECT WAS INTENDED TO SHOW PROOF OF CONCEPT AS WELL AS DEMONSTRATE CORE IDEAS OF SECURITY IN COMPUTING AND NOT INTENDED TO BE USED MALICIOUSLY.</b> </br> </br>
Neither of them actually harm the machine they run on, but it's not recommended that you run them.
Instead, the video demo is also located here, and a youtube link to the demo is also in the report. 

This repository holds the documentation and code for my Security in Computing final project. For this project, I created an advanced keylogger in Python. 
There are two versions of the keylogger; one that is armored and intended to sneak past antivirus software, and one that has no protection and will be spotted by most antiviruses. Both executables were packaged using the same Logger.py file using Pyinstaller, and the armored version was obfuscated and protected using Pyarmor. 

This keylogger is multifunctional. When running on a machine as either a python script or executable, it will snag information from your clipboard, microphone, screen, keystrokes, and system information. It will then store this information in .txt./.png/.wav files before encrypting them and giving them unsuspicious names to hide intentions. These files are then emailed to an account identified in code beforehand where I can grab them, decrypt them, and assess their contents. My intention for this keylogger was to be able to grab as much information about the device it runs on as possible without being detected by commercial antiviruses. 

To do so, I employed a few different methods. The files created on the victimized system would normally create a lot of noise, but the use of encryption and giving them normal names kept most shallow antiviruses from recognizing what the files were being used for. Next, the code itself was obfuscated using Pyarmor so that it was unreadable to most antiviruses. Following the packaging, I was able to edit the resulting executables to give them their "unprovocative" names as well as an icon to go along with the WatchDog design. Lastly, I created a fake certificate that I signed the armored executable with, which can bypass shallow antiviruses that simply look for a signature to be present rather than following the authentication chain. 

With all of these features added to the finished product, I was able to run the keylogger through VirusTotal, which checked 67 different antivirus' ability to detect any malicious behavior of the software. Out of these 67, only 1 antivirus found the file malicious, and this was simply because it was packaged with Pyinstaller; the antivirus did not alert to the actual behavior of the keylogger itself. The VirusTotal results can be found in the project report PDF in the repository along with a more thorough explanation of the project and a link to a video demonstration of the software in action. 
