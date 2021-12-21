## Lab 14

### Part 1: Staging Traffic Mirroring, Snort

------

#### Deploy snort to a Ubuntu Linux Desktop VM. Make sure there are two network interfaces on the Ubuntu VM, one plugged into LAN port of pfSense and the second interface plugged into the SPAN port of pfSense.

 

![Screenshot 2021-12-21 at 13.37.08](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2013.37.08.png)

![Screenshot 2021-12-21 at 14.49.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2014.49.26.png)

![Screenshot 2021-12-21 at 14.50.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2014.50.43.png)

#### You can initialize Snort with `sudo snort -c snort.conf -A console -i [network interface name]`, note that you need to specify your network interface name accordingly.

 Type the following command to open the snort configuration file in **gedit** text editor: `sudo gedit /etc/snort/snort.conf` and find the **ipvar HOME_NET** setting. You’ll want to change the IP address to be your actual class C subnet.

![Screenshot 2021-12-21 at 15.07.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2015.07.23.png)

Run snort with `sudo snort -T -i [network interface name] -c /etc/snort/snort.conf` to test the configuration file.

![Screenshot 2021-12-21 at 15.11.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2015.11.11.png)

Now let's run snort with `sudo snort -c snort.conf -A console -i [network interface name]`

![Screenshot 2021-12-21 at 15.17.16](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2015.17.16.png)

### Part 2: Detecting Network Activity with Custom Snort Rules

------

#### Write and test a Snort rule that detects when ICMP packets transmitted to its IP from internet and raises an alert to the console.

Follow **[THIS](https://frankfu.click/security/ids/how-to-detect-nmap-scan-using-snort/)** guide to add a ICMP detection rule.

![Screenshot 2021-12-21 at 16.52.16](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2016.52.16.png)

#### Issue the Zenmap test command: `nmap -sn [Snort host IP] -disable-arp-ping`.

![Screenshot 2021-12-21 at 16.08.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2016.08.19.png)

#### Issue the Zenmap test command: `nmap -sn [network IP with CIDR block] -disable-arp-ping`

![Screenshot 2021-12-21 at 16.51.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2016.51.44.png)

#### Observe Snort alerts. What are you seeing, and what is happening?

Snort is issuing an alert according to the rule, everytime it detects a ping sweep on the specificed network.

#### Write and test a Snort rule that detects when Kali Linux VM attempts an FTP connection to another local PC and raises an alert to the console.

Additional FTP related rules **[HERE](https://github.com/eldondev/Snort/blob/master/rules/ftp.rules)**

![Screenshot 2021-12-21 at 17.23.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2017.23.55.png)

##### Issue the Kali Linux console test command: `ftp [target host IP]`.

![Screenshot 2021-12-21 at 17.26.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2017.26.43.png)

#### Write and test a Snort rule that detects when Kali Linux VM attempts an SSH connection to another local PC and raises an alert to the console.

![Screenshot 2021-12-21 at 17.47.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2017.47.11.png)

##### Test the command using Kali Linux console command. Include a screenshot of this and the alet in your submission:

![Screenshot 2021-12-21 at 17.49.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2017.49.56.png)

##### Test the command using Zenmap/Nmap command. Include a screenshot of this and the alert in your submission:

![Screenshot 2021-12-21 at 17.54.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2017.54.17.png)

#### Write and test a Snort rule that detects when Kali Linux VM attempts a HTTP connection to another local PC and raises an alert to the console.

![Screenshot 2021-12-21 at 18.32.46](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2018.32.46.png)

![Screenshot 2021-12-21 at 18.31.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2018.31.57.png)

### Part 3: Detecting Network Activity with Premade Snort Rules

------

Register at snort.org, then download the “Registered” rules package at [Snort downloads](https://snort.org/downloads/#rule-downloads).

![Screenshot 2021-12-21 at 18.39.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-14/Screenshot%202021-12-21%20at%2018.39.07.png)

### Part 4: Reporting

------

#### How does Snort differ from a LAN firewall appliance?

Snort is a IDS, intrusion detection system. Firewalls block unauthorized traffic and permits auhtorized one. IDS performs packet inspection and logging, much like a security camera, it acts as monitor system for a network or host.

#### Why would a security teams deploy a NIDS solution?

A IDS is mandatory for every security system. It can detect mallicious activities in the network and help prevent attacks. Also they make it easier to meet security regulations due to the visibility they provid across the network.

#### What are some limitations/shortcomings of a NIDS solution? In other words, what malicious activity would a NIDS not detect?

More elaborate attacks that don't follow a known pattern. They are susceptible to protocol based attacks. They do not process encrypted packets. 
