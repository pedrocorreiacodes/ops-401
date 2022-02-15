## Class 44

### Reading: What is Metasploit? And how to use this popular hacking tool

------

Metasploit is a widely used penetration testing tool that makes hacking way easier than it used to be. It has become and indispensable tool for both red tead and blue team.

Metasploit is a penetration testing framework that makes hacking simple. I's an essential tool for many attackers and defenders. Point Metasploit at your target, pick and exploit, what payload to drop and hit Enter.

#### History of Metasploit

HD Moore began working on Metasploit in the early oughts, and released 1.0, written in Perl, in 2003. The project has grown dramatically since then, from the original 11 exploitds the project came with to more than 1,500 now, plus around 500 payloads, with a switch to Ruby under the hood along the way.

#### How to use Metasploit

During the information gathering phase of a pentest, Metasploit integrates seamlessly with Nmap, SNMP scanning and Windows patch enumeration, among others. There's even a bridge to Nessus. Every reconnaissance tool you can think of integrates with Metasploit.

Once the weakness is identified, hunt through Metasloit's large and extensible database for the exploit that will crack open that chink and get you in. 

Once on a target machine, Metasploit's quiver contains a full suite of post-exploitation tools, including privilege escalation, pass the hash, packet sniffing, screen capture, keyloggers, and pivoting tools. You can also set up a persitent backdoor in case the machine in question gets rebooted.

### Lecture

------

+ Windows prefers to use Kerberos when it's available for authentication processes
+ Originally developed by MIT in the late 80s, Kerberos is a computer network security protocol that authenticates service requests between two or more trusted hosts across an untrusted network.
  + Uses secret-key cryptography and a trusted third party for authenticating client-server application and verifying users' identities.

+ TA0008: Lateral Movement is a post-exploitation tactic used to maneuver deeper into a network in search of sensive data or high-value assets
  + In T1550: Use Alternate Authentication Material, adversaries use alternate authentication material, such as password hashes, Kerberos tickets, and application access tokens, in order to move laterally within an environment

#### Traffic Sniffing

+ Man-in-the-middle attacks occur when the adversary positions themselves between multiple network devices to perform either network sniffing or transmitting data manipulation.
  + MITRE ATT&CK tecnique T1557, under tactic Crdentials Access
  + Abuses common network protocols that facilitate network traffic flow
  + Can be used to deny traffic, resulting in a denial-of-service
+ Goals
  + Information gathering
  + Ideal - Gather admin credentials
+ Sniffing is the process of monitoring and capturing all the packets passing through a network using tools
  + In passive sniffing trafic is observed but not altered
  + In active sniffing traffic may also be altered to suit the attack technique
+ Difference: Hub vs switch?
  + Collision domain determine what ports can see your traffic

#### Vulnerable Protocols

+ Vulnerable protocols
  + HTTP (port 80)
    + Hypertext transfer protocol is used at layer 7 of the OSI model and lacks encryption to ensure confidentiality
    + HTTPS (port 443) instead encrypts traffic as it leaves layer 7
  + Telnet (port 23)
  + Unencrypted predecessor to SSH 
+ HTTPS (port 443)
  + Not considered vulnerable to MITM
  + If encryption key is obtained, checkmate
+ How can HTTPS keys be obtained?
  + Option 1: Session Keys Log file
    + Web browser must be configured to dump keys to a log file
    + Requires a foothold on the target PC
  + Option 2: Private Key of the Web Server

#### DNS Cache Poisoning

+ DNS cache poisoning is the act of entering false information into a DNS cache, so that DNS queries return and incorrect response and users are directed to the wrong websties
  + Incorrect DNS information remains in cache until the the time to live expires, or until it is removed manually

#### ARP Poisoning

+ Address resolution protocol (ARP) translates Internet Protocol (IP) addresses to a Media Access Control (MAC) adress, and vice versa
  + Devices use ARP to contact the router or gateway for intenet acess
+ In address resoltution protocol (ARP) poisoning, also known as ARP spoofing, attackers changes a MAC address associeated with the impersonated IP by altering targeted computer's ARP cache with a fprged ARP request and reply message 