## Lab 43

### Part 1: Staging

------

Deploy two VMs to a NAT Network:

- class-40-45-kali.ova
- class-42-target2-win7.ova

![Screenshot 2022-02-14 at 14.48.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2014.48.10.png)

![Screenshot 2022-02-14 at 15.02.24](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2015.02.24.png)

Access the Class 43 folder on your Kali desktop to confirm Ettercap is installed and operational.

![Screenshot 2022-02-14 at 15.14.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2015.14.44.png)

- Download [PCAP and log key](https://github.com/pan-unit42/wireshark-tutorial-decrypting-HTTPS-traffic) that will be used in Part 3 to your Kali box.

### Part 2: MITM and ARP Cache Poisoning with Ettercap GUI

------

First let’s practice some basics by having Ettercap capture network traffic transmitted between class-42-target2-win7.ova and the internet. To do this, we’ll need to perform a simple ARP poisoning attack and then analyze the sniffed packets with Wireshark.

- Set packets to automatically forward from Kali Linux’s eth0 interface using the terminal command `sysctl -w net.ipv4.ip_forward=1`.

![Screenshot 2022-02-14 at 16.02.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.02.38.png)

- In Kali, launch Ettercap and select a sniffing mode.

![Screenshot 2022-02-14 at 16.03.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.03.51.png)

- Designate your targets.

We can run a quick scan of different hosts acting as parties in network traffic. Click Hosts > Scan for Hosts to run a quick scan and get a list of host targets. You should see Ettercap populate a list of host IP and MAC addresses.

Here we can see our target's IPaddress 10.0.2.19:

![Screenshot 2022-02-14 at 16.13.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.13.29.png)

Click on the target, or, if you want to attack every computer on the network, don't select any list item. 

- On Windows PC, grab a screenshot of the arp cache.

![Screenshot 2022-02-14 at 16.18.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.18.18.png)

- Perform an ARP poisoning attack to grant Ettercap access to Windows PC.

Select the target from the host list go to **MITM Menu > ARP poisoning...**:

![Screenshot 2022-02-14 at 16.22.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.22.51.png)

- On Windows PC, grab a screenshot of the poisoned arp cache. How can you tell it’s poisoned?

All of the known IP address share the same MAC address:

![Screenshot 2022-02-14 at 16.25.06](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.25.06.png)

- Initialize live sniffing in Ettercap, then launch Wireshark. Have Wireshark perform live packet capture on the sniffer interface.

![Screenshot 2022-02-14 at 16.28.25](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.28.25.png)

- Perform a ping from the Windows PC to any valid destination IP or URL. If you have successfully performed a MITM attack, you’ll see these ping packets.

![Screenshot 2022-02-14 at 16.29.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.29.30.png)

- Have Wireshark filter down the view to only ICMP packets. Take a screenshot of this successful outcome.

![Screenshot 2022-02-14 at 16.32.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.32.59.png)

- On the Windows PC navigate a web browser to [http://www.wikidot.com](http://www.wikidot.com/), then navigate to the “Pricing” link at the top.

![Screenshot 2022-02-14 at 16.51.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.51.53.png)

- Have Wireshark filter down the view to only HTTP packets. Take a screenshot of the HTTP GET request for the Pricing page.

![Screenshot 2022-02-14 at 16.54.39](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.54.39.png)

- Save a PCAP of the captured data to your desktop > Class 43 folder and take a screenshot of the PCAP.

![Screenshot 2022-02-14 at 16.57.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.57.18.png)

![Screenshot 2022-02-14 at 16.57.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2016.57.59.png)

### Part 3: Decrypting HTTPS with Wireshark

------

- If you have not done so in staging, download the [PCAP and log key used in this exercise](https://github.com/pan-unit42/wireshark-tutorial-decrypting-HTTPS-traffic) to your Kali system.

![Screenshot 2022-02-14 at 17.11.22](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2017.11.22.png)

- Complete the tutorial. Document in your submission today your thoughts and screenshots of key milestones achieved during the tutorial.

![Screenshot 2022-02-14 at 17.26.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2017.26.07.png)

Got the Preferences menu and inside the menu go to **Protocols** and slide down to select **TLS**. Click on **Browse** and select our key log file:

![Screenshot 2022-02-14 at 17.47.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2017.47.15.png)

Once you have clicked “OK,” when using the basic filter, your Wireshark column display will list the decrypted HTTP requests under each of the HTTPS lines:

![Screenshot 2022-02-14 at 17.47.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2017.47.50.png)

### Part 4: ARP Spoofing with Ettercap Command Line

------

- For this part of the lab, use all resources at your disposal to determine how this attack is performed with Ettercap.
- For the website you redirect the Windows user to, try setting up a quick Apache web server on Kali. Alternatively, redirect it to an entirely different website on the internet.

![Screenshot 2022-02-14 at 18.46.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2018.46.02.png)

- When the successful outcome is achieved, capture a screenshot of Ettercap’s terminal performing the redirect, as well as a screen of the site you sent the unsuspecting user to.

First we need to edit `etter.dns` and add the name of the website which we want the victim to get redirected to:

![Screenshot 2022-02-14 at 18.48.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2018.48.41.png)

Let's activate DNS spoofing:

![Screenshot 2022-02-14 at 18.49.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2018.49.38.png)

- When the successful outcome is achieved, capture a screenshot of Ettercap’s terminal performing the redirect, as well as a screen of the site you sent the unsuspecting user to.

![Screenshot 2022-02-14 at 19.01.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-43/Screenshot%202022-02-14%20at%2019.01.33.png)

### Part 5: Reporting

------

Answer the discussion prompts below:

- What is ARP poisoning, and how does it work?
  - ARP poisoning also known as ARP spoofing is a cyber attack carried out through malicious ARP messages. The threat actor sends fakes ARP packets that link its MAC address with an IP of a computer already on the LAN. After a successful ARP spoofing, a hacker changes the company's ARP table, so it contains falsified MAC maps. The contagion spreads.
- How is ARP spoofing different from DNS poisoning?
  - DNS poisoning is a cyber attack technique where the threat actors substitues the address for a valid website for an impostor. This technique manipulates known vulnerabilities within the domain name system(DNS). ARP spoofing refers to vulnerabilitites regarding the Addresss Resolution Protocol.
- Why might a penetration tester utilize Ettercap on a targeted subnet?
  - To test if that particular subnet is susceptible to ARP poisoning attacks.
- For what purposes would a malicious attacker use these techniques?
  - To get sensible information, to monitor a network in search of sensible data.
