## Class 43

### Reading: What is a Sniffing attack and How can you defend it?

------

Sniffing in general terms refers to investigate something coverly in oder to find confidential information. From an information security perspective sniffing refers to tapping the traffic or routing the traffic to a target where it can be captured, analyzed and monitored. Sniffing is usually performed to analyze the network usage, troubleshooting network issues, monitoring the session for development and testing purpose.

#### Define a Sniffing Attack

In the world of internet, sniffing can be performed using an application, hardware devices at both the network and host level.

Any network packet having information in plain text can be intercepted and read by the attackers. This information can be usernames, passwords, secret codes, banking details or any information which is of value to the attacker. This attack is just the technical equivalent of a physical spy.

Sniffing motives:

+ Getting username and passwords
+ Stealing bank related/transaction related information
+ Spying on email and chat messages
+ Identity theft

#### Types of Sniffing

There are two types of sniffing: active and passive.

As the name suggests, active involves some activiy or interaction by the attacker in order to gain information. In passive the attacker is just hiding dormant and getting the information.

###### Passive Sniffing:

This kind of sniffing occurs at the hub. A hub is a device that received the traffic on one port and then retransmits that traffic on all other ports. It does not take into account that the traffic is not mean for other destinations. In this case, if a sniffer device is placed at the hub then all the network traffic can be directly captured by the sniffer. Since hubs are not used these days much, this kind of attack will be an old-school trick to perform. Hubs are being replaced by switches and that is where active sniffing comes into the picture.

###### Active Sniffing:

In a nutshell, a switch learns a CAM table that has the mac addresses of the destinations. Based on this table the switch is able to decide what nwtqorks packets is to be sent where. In active sniffing, the sniffer will flood the switch with bogus requests so that the CAM table gets full. Once the CAM is full the switch will act as a switch and send the network traffic to all ports. Now, this is legitimate traffic that gets distributed to all the ports. This way the attacker can sniff the traffic from the switch.

+ MAC flooding - Flodding the switch with MAC address so that the CAM table is overflowed and sniffing can be done.
+ DNS cache poisoning - Altering the DNS cache records so that it redirects the request to a malicious website where the attacker can caputre the traffic. The malicious website may be a genuine looking website which has been set up by the attacker so that the victims trust the website. The user may enter the login details and they are sniffed right away.
+ Evil Twin attack - The attacker uses malicious software to change the DNS of the victim.  The attacker has a twin DNS set up already (evil twin), which will respond to the requests. This can be easily used to sniff the traffic and reroute it to the website that the attacker wishes.
+ Mac spoofing - The attacker can gather the MAC adress that are being connected to the switch. The sniffing device is set with the same MAC address so that the messages that are intended for the the orignal machine are delivered to the sniffer machine since it has the same MAC address set.

#### How do you identify a Sniffer?

Protocols vulnerable to sniffing attacks

Sniffing attacks work on various layers depending on the momtive of the attack. Sniffers can capture the PDU's from various layers but layer 3 (Network) and 7 (Application) are of key importance. Out of all the protocols, some are susceptible to sniffing attacks. Secured version of protocols are also available but if some systems are still using the unseured versions then the risk of information leakage becomes considerable. Let's discuss some of the protocols that are vulnerable to sniffing attacks.

1. HTTP - Hypertext transfer protocol is used at layer 7 of the OSI model. This is an application layer protocol that transmits the infromation in plain text. This was fine whn there were static websites or websites that did not required any input from the user. Anyone can set up a MITM proxy in between and listen to all the traffic or modify that traffic for personal gains. Now when we have entered into the web 2.0 world, we need to ensure that the user's interaction is secured. This is ensured by using the secured version of HTTP i.e. HTTPS. Using https, the traffic is encrypted as soon as it leaves layer 7.
2. TELNET - Is a client-server protocol that provides communication facility thprugh virtual terminal. Telnet does not encrypt the traffic by default. Anyone having access to a switch or hub that connects the client and the server can sniff the telnet traffic for username and password. SSH is used as an alternate to the unsecured telnet. SSH uses cryptography to encrypt the traffic and provides confidentiality and integrity to the traffic.
3. FTP - Is used to transfer files between client and server. For authentication FTP used plain text username and password mechanism. Like telnet, an attacker an sniff the traffic to gain credentials and access all files on the server. FTP can be secured by sung SSL/TLS or can be replaced by a more secured version called SFTP (SSH file transfer protocol).
4. POP - It stands for Post office protocol and is used by email clients to download the emails from the mail server. It also used palin text mechanism for communication hence it is also vulnerable to sniffing attack.POP is followed by POP2 and POP3 which are little bit more secure than the original version.
5. SNMP - Simple network management protocol is used for communication with managed network devices on the network. SNMP uses various messages for communication and community strings for performing client authentication. Community srings in effect are just like password that is transmittd in clear text. SNMP has been superseded by SNMPV2 and V3, v3 being the latest and most secure.

#### Top Sniffing Tools

##### Wireshark

An opensource packet capturer and analyzer. It supports Windows, Linux etc. and is a GUI based tool (alternate to Tcpdump). It used pcap to monitor and caputre the packets from the network interface. The packets can be filtered basis IP, protocol and many other parameters. The packets can be grouped or marketd basis relevance. Each packet can be selected and dissected as per need.

##### dSniff

It is used for network analysis and password sniffing from various network protocols. It can analyze a variety of protocols (FTP, Telnet, POP, rLogin, Microsoft SMB, SNMP, IMAP etc) for getting the information.

Microsoft network monitor: As the name suggests it is used for capturing an analyzing the network. It is used for troubleshooting the network. Some of the features of the software are Grouping, a Large pool of protocol support(300+), Wireless monitor mode, reassembly of fragmented messages etc.

##### Debookee

A paid tool that can be used to monitor and analyze the network. It is able to intercept and analyze the traffic from devices that are in that subnet, irrespective of the device type (Laptop, devices, Tv etc.). It offers various modules:

+ Network analysis module: Scan for connected devices, Intercept traffic in a subnet, TCP port scannerm Network analysis and monitor of HTTP, DNS, TCP, DHCP protocols, Analyse VoIP calls etc.
+ WiFi monitoring module: Details of access points in radio range, wireless client details, wifi statistics etc
+ SSL/TLS decryption module: Support for monitoring and analyszing secured protocols.

#### Precautionary measure against Sniffing attacks

1. Connects to trusted networks - Connecting to any public network will have a risk that the traffic might be sniffed. Attackers can either sniff that network or create a new network of their wn with similiar names so that the users get tricked into joining that network.
2. Encrypt! - Encrypt all the traffic that leaves your systems. This will ensure that even if the traffic is being sniffed, the attacker will not be able to make sense of it. Defense in depth principle. Encrypting the data does not mean that now everything is safe. The attacker might be able to capture a lot of data and ryn crypto attacks to get something out of it.
3. Network scannign and monitoring: Networks must be scanned for any kind of intrusion attempt or rogue devices that may be setup in span mode to capture traffic. Network admins must monitor the network as well so as to ensure the device hygiene. It team can use various techniques to determine the presence of sniffers in the network. Bandwidth monitoring is one, an audit of devices which are set to promiscuous mode etc.