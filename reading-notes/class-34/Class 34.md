## Class 34

### Lecture

------

#### Beacons

+ Beaconing is when the malware communicates with a C2 server asking for instructions to exfiltrate collect data on some predetermined asyncrhonous interval.
  + Key characteristics of a beacon
    + Timing
    + Packet size
  + Beware false positives
  + Proper beacon analysis is difficult and tedious
  +   A beacon with many connections is a strobe
+ Long connectinos may only open and cose infrequently compared to frequent beacons.
  + Top: One long connection
  + Bottom: Six shorter connecticons
+ You many need to track these differently than you're used to

#### Digital Forensics

+ Why digital forensics?
  + Answer the question: "What happened on this device?"
+ Digital Forensics & Incident Response (DFIR) is a multidisciplinary profession that focuses on identifying, investigating and remediating computer network exploitation
  + Ever seend Dexter?
  + DFIR is the cyber equivalent of the character Dexter
+ In a digital forensics investigation, investigators recover documents, photos, email and files from computer systems, hard drives and devices
  + Commonly a part of cyber crime investifaton
  + Examine computer systems to find evidence of illegal activity
  + Forensics specialists also assist with network breaches in DFIR role
+ What are the stages of a digital forensics investigation?
  + Planning
  + Indentification and preservation
    + The firs rule of digital forensics is to preserve the original evidence
    + Protect original copies of data by making copies first
    + Integrity is everything!
    + Isolate, safeguard and preserve the master copy
  + Analysis
    + Here's the part we'll be doing today in lab!
    + Construct a timeline of events
    + Build a picture of what happned
  + Documentation
    + Record, date & sign
  + Presentation
    + Present your findings without any bias or partiality

#### Data Volatility

+ Why is data volatility revelevant to forensics?
  + Volative data can be permanently lost due to mishandling of evidence
    + RAM
    + CPU cache
+ How do forensic investigators handle non-volatiele memory?
  + Follow specific procedures designed to preserve evidence integrty
  + Example
    + Clone the hard disk, ten derive a hsh valaue of both 

#### Hard Disk Copy

+ DD files (with the .dd file extension) are data containers created by hard drive copy tools
+ In Linux, DD utility uses the following command to cread a dd image file:
  + `dd if =/dev=hdr of=mydisk.dd`
  + `mydisk.dd`is a name of the destination file
+ In Windows, DD utility uses the following command to create a dd disk image:
  + `dd.exe if=\\.|PhysicalDrive0 of=d:\images\PhysicalDrive0.dd`
  + Create a duplicate copy of a source drive

#### File Types

+ A file with the DAT file extension is usually a generic data file that stores information specific to the application it refers to
  + Sometime you'll find them by themselves but often they're with other configuration files like DLL files.

#### Autopsy

+ Autopsy is an open source forensic platform that comes blundled in FLARE VM
  + Analyze mobile devices and digital media
  + Used in law enforcement, national security, litigation support, and corporate investigation
+ Why use Autopsy over manual file navigation?
  + Multi-user cases, timeline analysis, registry analysis, keyword searchm email analysis, media playback, EXIF analysis, malicious file detection