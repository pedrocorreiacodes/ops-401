## Lab 32

### Part 1: Staging

------

##### Disable Windows Defender Antivirus in FLARE VM

![Screenshot 2022-01-25 at 18.55.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-25%20at%2018.55.42.png)

Go to **Manage settings** and disblae **Real-time protection**:

![Screenshot 2022-01-25 at 18.57.14](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-25%20at%2018.57.14.png)

##### Open the evidence package named “class-32-traffic.7z” on your FLARE VM desktop using password “malwareinside” to open.

![Screenshot 2022-01-25 at 19.03.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-25%20at%2019.03.32.png)

### Part 2: Malware Traffic Analysis

------

We can check on the alerts that several downloads took place at 192.168.200.8:

![Screenshot 2022-01-26 at 13.15.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-26%20at%2013.15.57.png)

Let's open the `.pcap` to analyze traffic from that ip address:

![Screenshot 2022-01-26 at 13.26.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-26%20at%2013.26.55.png)

We can open the HTTP packet corresponding to one of those download to check the mac address and model of the computer that performed that download:

![Screenshot 2022-01-26 at 13.28.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-26%20at%2013.28.53.png)

We can also check that there is an unusual amount of `ACK`packets being sent from `205.185.113.20` that probably means that they are performing a `TCP ACK Scan`. It is used to map out firewall rulesets, determining whether they are stateful or not and which ports are filtered.

![Screenshot 2022-01-26 at 13.36.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-32/Screenshot%202022-01-26%20at%2013.36.23.png)



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
