## Class 31

### Reading: What are YARA rules?

------

YARA rules are rules you write and use to try to find malware in your system, like a Google search for pieces of malware code.

A set of a tools that you can use to track down malware in your computer or network. You create YARA rules to help you find what you want.

Attackers may reuse code in different malware campaigns. YARA rules can look for that code along with some of the malware's functions and features.

#### Clues

After big cyberattacks or during current cyberattacks campaigns, experts may send out YARA rules to help cyber defenders look for the potential poision in their systems.

YARA rules are only as good as the information they are based on. If attackers change up some of their code and features, defenders may have to write new YARA rules.

#### Unusual Name

Where does the name come from?

From YARA's creator, Victor Alverez: "YARA: Another Recursive Acronym or Yet Another Ridiculous Acronym... Pick your choice."

YARA rules could save you from malicious phising email or a nation-state attack designed to take down your critical infrastructure.



### Lecture

------

#### Review: FUD

Fully Undetectable 

+ Many tools exist to hilp attackers avoid detection:
  + Example: Phatom Evasion
+ Attackers want to evade defenses (e.g. Windows Defender) but making malware payload fully undetectable.
+ Py2exe is a Ptython Distuils extensions which conversts Python scripts into executable Windows programs
+ Metasploit is a penetration testing platform that enables you to find, exploit and validate vulnerabilities
  + Similiar to its cousin, PowerShell Empire

#### Threat Hunting

##### Careers in Threat Hunting

+ Threat hunters proactively seatch for cuber threats that are lurkig undetecting in a network
  + Hunters are experts on Tactics, Techniques, and Procedures (TTPs)
  + Highly knowledgeable of IT envirornments, malware attacks vectors, and threat actors
+ SQRRL developed the Threat Hunting Loop, a four-stage model for successful threat hunting
  + A hunt starts with creating a hypothesis about an observed activity
  + Hypotheses are investigated via various tools and techniques
  + Tools an techniques uncover new malicious patterns of behaviour and adversary TTPs
  + Succesful hunts form the basis for informing and enriching automate analytics

##### Indicators of Compromise

+ Indicator of compromise (IOC) i a forensic term that refers to the evidence on a device that point out to a security breach
+ The Pyramid of Pain depicts how much pain it will cause the adversary when you are able to deny IOCs to them

##### YARA

+ YARA is a boolean logic pattern matching system used in:
  + Digital forensics
  + Incident response
  + Reverse engineering
  + Threat hunting
+ Open source
+ Works on many OS
+ Target files
+ Used in many tools you might not expect
  + SIEM
  + IDS
  + Antimalware/Antivirus
+ A YARA rule checks whether the target file meets the rule or not
+ Syntax
  + Text strings
  + Hexadecimal
  + Regular expressions (regex)

##### Portable Executables

+ The Potable Executable (PE) format is a file format for executables, object code, DLLs and other used in 32-bit and 64-bit versions of Windows OS
  + Example:
    + notepad.exe
    + cmd.exe
+ What is the significance of a .exe file in the securty context?

##### ClamAV

Open source Anti Virus solution

+ How can YARA rules be practilcally applied to defensive SecOps? 
+ Clam AntiVirus (ClamAV) is an open source antimalware toolkit
  + Desined to scan files quickly
  + Great for email gateway scanning
  + Maintains a signed malware signatures database
  + Supports the YARA engine
    + YARA rules can either complement or replace the ClamAV signature database
    + ClamAV can decompress an archived file and run the YARA engine on it