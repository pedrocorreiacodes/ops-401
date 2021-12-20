## Class 14

### Reading: The Pros & Cons of Intrusion Detection Systems

------

Intrusion detection systems are a lot like fire alarms. Just as a fire alarma detects smoke, an intrusion detection system identifies incidents and potential threats.

They are useful for raising awareness, but if your don't hear the alrma or react appropriately your house may burn down.

While a firewall is there to keep out malicious attacks, an IDS is there to detect whether someone or something is trying up to suspicious or nefarious activity. When it detects something, it notifies the system administrator.

An IDS is a visibility tools that sits off to the side of the network and monitors traffic. It consists of a management console and sensors. When the sensors encounter something tha matches up to a preciously detected attack signature, they report the activity to the console. An IS can notify security personll of infections, spyware or key looters, as well as accidental information leakage, security policy violations, anauthorized clients and servers, and even configuration error.

#### Intrusion Detection Systems (IDS) vs. Intrusion Prevention Systems (IPS)

An IPS is similar to an IDS, except that they are able to block potential threats as well. They monitor, log, and report activities, similarly to an IDS, but they are also capable of stopping threats without the system administrator getting involved. If an IPS is not tuned correctly, it can also deny legitimate traffic, so they are not suitable for all applications.

#### Network Intrusion Detection Systems vs. Host Intrusion Detection Systems (HIDS)

An NIDS and and HIDS are complementary systems that differ by the position of the sensors: network-based (monitoring the ethernet or WiFI) and host-based respectively. Because of this, their uses and deployment are quite different.

Network-based sensors have a quicker response than host-based sensors and they are also easier to implement. A NIDS doens't need to alter the existing infrastructure and they monitor everything on a network segment, regarless of the target host's operating system. As they do not need software loaded and managed at the different hosts in the network, they have a lower cost of setup and ownership.

An NIDS can detect attacks that an HIDS will miss because it looks at packet headers in real-time. In saying this, an HIDS will also be able to pick up some things that an NIDS will miss, such as unauthorizes users making changes to the system files. An HIDS monitors event and audit logs, comparing new entries to attack signatures. This is resource intensive, so your organization will need to plan for the additional hardware required.

Another benefit of an NIDS is that they detect incidents in real-time, meaning that they can log evidence that an attacker may otherwise try to erase. While the real-time detection abilities of an NIDS allows for quicker responses, they also turn up more false positives than an HIDS. Hybrid NIDS and HIDS solutions are also available.

#### Pros of Network Intrusion Detection Systems:

+ They can be tuned to specific content in network packets
  + This can be used for uncoverng intrusion such as exploitation attacks or compromised endpoint devices that are part of a botnet.
+ They can look at data in the context of the protocol
  + When a NIDS performs protocol analysis, it looks at the TCP and UDP payloads.
  + The sensors can detect suspicious activity because they know how the protocols should be functioning.
+ They can qualify and quantify attacks
  + An IDS analyses the amount of types of attacks.
  + This information can be used to change security systems or implementing new controls that are more effective. It can also be analyzes to identify bugs or network device configuration problems. The metrics can be used for future risk assessments.
+ They make it easier to keep up with regulation
  + IDS gives you greater visibility across your network, they make it easier to meet security regulations.
  + You can use IDS logs as part of the documentation to meet certain requirements.
+ They can boost efficiency
  + IDS sensors can detect network devices and hosts, they can inspect the data within the network packets and identify the services or operating systems that are being utilized. This saves a lot of time when compared to doing it manually. An IDS can also automate hardware inventories, further reducing labor. These improved efficiencies can help reduce an organization's staff costs and offset the cost of implementing the IDS

#### Cons of Network Intrusion Detection Systems

+ They will not prevent incidents by themselves
  + Does not block or prevent attacks
  + IDS needs to be a part of a comprehensive plan that includes other security measure and staff who know how to react appropriately
+ And experienced Engineer is needed to administer them
  + The usefulness all depends on what you do with the information that they give you.
  + Detection tools don't block or resolve potential issues
+ They do not process encrypted packets
  + IDS's cannot see into encrypted packets, so intruders can use them to slip into the network.
  + This is a huge concern as encryption is becoming more prevalent to keep our data secure
+ IP Packets can still be faked
  + The information from an IP packet is read by an IDS, but the network address can still be spoofed. If an attacker is using a fake address, it makes the threat more difficult to detect and assess.
+ False positives are frequents
  + In many cases false positives are more frequent than actual threats. An IDS can be tuned to reduce the number of false positives, however your engineers will still have to spend time responding to the. If they don't care to monitor the false positives, real attacks can slip through or be ignored
+ They are susceptible to protocol based attacks
  + An NIDS analyzes protocols as they are captured, which means that they face the same protocol based attacks as network hosts. An NIDS can be crashed by protocol analyzer bugs and also invalid data
+ The signature library needs to be continually updated to detect the latest threats
  + An IDS is only as good as its signature library. If it isn't updated frequently, it won't register the latest attacks and it can't alert you about them. Another issue is that your systems are vulnerable until a new threat has been added to the signature library, so the latest attacks will always be a big concern.