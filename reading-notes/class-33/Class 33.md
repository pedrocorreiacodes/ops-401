## Class 33

### Reading: What is Threat Hinting and Why Is It So Important?

------

Threat hunting is not responsive, it is proactive. We're going to see if our systems have some indicator of compromise.

The result we get is a compromise assessment.

+ Search the network for signs of compromise
+ Active/Proactive activity
  + Resuts driven
    + Target behaviour, not "signatures"
+ Should include all devices - Servers, desktops, network hardware, IIoT, BYOD
+ Output is a compomise assessment
  + Are any of our systems currently compromised?

### Lecture

------

#### Threat Hunting

+ SQEEL developed the Threat Hunting Loop, a four-stage model for successful threat hunting
  + A hunt starts with creating a hypothesis about an observed activity
  + Hypotheses are investigated via various tools and techniques
  + Tools and techniques uncover new malicious patterns of behaviour and adversary TTPs
  + Succesful hunts form the basis for informing and enriching automated analytics

How can YARA rules be practically applied to defensive SecOps?

+ Log generation source to perform disocovery.

Clam AntiVIrus is an open source antimalware toolkit

+ Designed to scan files quickly
+ Great for email gateway scanning
+ Supports the YARA engine
  + YARA rules can either complement or replace the ClamAV signatures database
  + ClamAV can decompress an archived file and run the YARA engine on it

#### Malware Traffic Analysis

+ Malware incidents leave a bread crumb trail; logs and packets
+ What have you been practicing doing?
  + Log generation and ingestion
  + Packet capture
+ We can use behavior patterns to spot suspicious activities
+ We can pinpoint "invisible" threats
+ Ultimately, minimize damage and profit loss
+ **Traffic analysis** consists of capturing network traffic into a packet capture (PCAP) file, the analyzing that file
+ If part of an investigation, answer who what when where and why
+ Packets may contain valuable IOCs (Inficators of compromise) that tell us:
  + what happened?
  + Identified after the attack took place
  + Alerts, system log entries, files
  + These are the "breadcrumbs" that lead to detection
  + Not the easiest to find
+ MTA examples:
  + Unusual Outbound Network Traffic
  + Anomalies in Privileged User Account Activitty
  + Geographical Irregularities
  + Log-In Red Flags
  + Increases in Database Read Volume
  + HTML Response Sizes
  + Large Numbers of Requests for the Same File
  + Mismatched Port-Application Traffic
  + Suspicious Registry or System File Changes
  + Unusual DNS request
  + Unexpecting Patching of Systems
  + Mobile Device Profile Changes
+ An indicator of attack is similar to an IOC but is instead a forensic analysis of attack taking place right now
+ **OpenIOS** is a framework that attempts to standardize the workflow of reporting IOCs
  + Initial leads
  + IOC Creation
  + Deploy IOC
  + Identify Suspect Systems
  + Preserve/Collect Evidence
  + Analyze Data
+ **CybOX** is a standardized language for encoding and communicating high-fidelity information about cyber observables.
  + CybOX is to IOC as SQL is to relatonal database transactions