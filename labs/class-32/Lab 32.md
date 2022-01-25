## Lab 32

### Part 1: Staging

------

##### Disable Windows Defender Antivirus in FLARE VM

![Screenshot 2022-01-25 at 18.55.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-32/Screenshot 2022-01-25 at 18.55.42.png)

Go to **Manage settings** and disblae **Real-time protection**:

![Screenshot 2022-01-25 at 18.57.14](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-32/Screenshot 2022-01-25 at 18.57.14.png)

##### Open the evidence package named “class-32-traffic.7z” on your FLARE VM desktop using password “malwareinside” to open.

![Screenshot 2022-01-25 at 19.03.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-32/Screenshot 2022-01-25 at 19.03.32.png)

### Part 2: Malware Traffic Analysis

------



### Part 3: Reporting

------

#### Executive Summary

#### Include when, who, and what happened.

 On Thursday, 2020-11-13 at 00:26 UTC, a Windows computer used by Craig Alda was infected with IcedID malware. Several hours later at 09:39 UTC, the infected Windows computer retrieved a Windows executable file for Cobalt Strike malware, and we began seeing Cobalt Strike infection traffic.

#### Details

#### Include details of the victim such as hostname, IP address, MAC address, Windows user account name.

+ IP address: 192.168.200.8
+ MAC address: 00:08:02:1c:47:ae (HewlettP_1c:47:ae)
+ Host name: DESKTOP-JH1UZAE
+ User account name: craig.alda

#### Indicators of Compromise (IOCs)

#### Include SHA256 hashes and details of the malware and/or artifacts, IP addresses, domains and URLs associated with the infection.

- C-drive/syuHKYt/vFPKnDV/VSMecyU.dll
- C-drive/Users/craig.alda/AppData/Local/Temp/~2559312.dll
- C-drive/Users/craig.alda/AppData/Local/Temp/tezehu.exe
- C-drive/Users/craig.alda/AppData/Local/Temp/sqlite64.dll
- C-drive/Users/craig.alda/AppData/Local/Temp/~2457218.tmp
- C-drive/Users/craig.alda/AppData/Roaming/Exijopac/uwsida3/baipuyac.png
- C-drive/Users/craig.alda/AppData/Roaming/craig.alda/Maaywuku2.dll
- C-drive/Users/craig.alda/Documents/CV.xlsb
- C-drive/Windows/System32/Tasks/{5FD47D96-5062-7DE3-08DA-938D00A84B6B}