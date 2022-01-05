## Class 27

### Reading: PowerShell Empire Framework Is No Longer Maintained

------

The Empire post-exploitation framework used by hackers of all hats has been discontinued.

Empire was released in 2015 at he BSides Las Vegas conference to show how PowerShell could be used beyond the infection stage of an attack.

Its open-source nature and modular architecture allowed it to grow and fulfill the needs of offensive security teams, who saw in it an opportunity to test defenses by imitating attacks from real threat actors.

One of its major advantages is that it uses encrypted communication with the command and control server and made it difficult to detect its traffic, especiall in large networks.

And adversary can use Empire to control an agent planted on the compromised host and forward the attack. Further developmetn removed the necessity of powershell.exe on the infected machine.

Over time, numerous ecploit modules were added to the framework for various hacking needs, and a Python agent for Linux and macOS systems.

Empire was also embraced for malicious activities. Researchers saw it used y various threat groups, from nation-sate hackers to financially-driven ones.

The framework is very popular with malware operators due to being "lightweight and extensible for modular development"

Although discontinuing Empire is a blow to hackers on both side of the law, there are alternative frameworks available for red teams:

+ Apfell
+ Covenant
+ Silver
+ Faction

### Lecture

------

#### Modeling PsExec

+ Can `Invoke-PsExec`be prevented from executing?
  + Firstly, where is it originating?
  + Within the LAN, or...
  + Outside the LAN
+ What defenses can help us?
  + Firewalls
  + SIEM
  + Group Policy
  + Prevent privilege escalation
+ What logs does Invoke-PsExec generate?
  + SIEM
+ What does `Invoke-PsExec`traffic look like?
  + Network traffic analysis
  + Wireshark
+ If we know what logs look like, what can we do?
+ In addition to a traditional network topology, we need to depict traffc flows on the diagram
  + Protocol of the traffic
  + Direction of the traffic

#### Threat Analysis

+ Cyber threat analysis is a process used by cybersecurity threat analyst to study and align a particular organization's defenses against its potential or relaized cyber threats
+ Threats analysis aims to answer: 
  + What are we working on?
  + What are the things that can go wrong?

#### T1059.001

Adversaries may abuse PowerShell commands and scripts for execution

+ Executing commands
+ Leveraging encoded commands
+ Obfuscation (with and without encoding)
+ Donwloading additional payloads
+ Launching additional processes
+ Examples
  + `Star-Process`cmdlet
    + Executes processes
    + `Invoke-Command`cmdlet
      + Runs a command locally or on a remote computer
+ Required: Administrator permissions to connect

#### Persistence

------

+ Persistence is a tactic in which the adversary attempts to maintiain their foothold on the targeted network.
  + TA003 in MITRE ATT&CK
  + Tecniques that adversaries use to keep acess to system across restarts, changed credentials, and other interruptions that could cut off their access
  + Access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code.

#### Atomic Testing

+ Testing coverage is fundamental to improving security outcomes
+ Testing should be fast and easy
+ Defenders need to keep learning how adversaries are operating
+ Have a testing method
  + Without a testing method, admin will just download a VM and pull 100 viruses from VirusTotal to test their defenses
+ Atomic Red Team is a "library of simple tests that every security team can execute to test their defenses. Tests are focused, have few dependencies, and are defined in a structured format that can be used by automation frameworks".
+ Every Atomic Red Team test is a small, higly portable detection test mapped to the MITR ATT&CK Framework.
  + Mapped to a tactic
  + Facilitates defensive testing in a proactive actionable fashion

#### PowerShell Empire

+ Isn't Empire retired?
  + Infamous for its used by nation-state APTS
  + Encrypted C2 traffic
  + Popular post-exploitation framework
+ PowerShell Empire is a pure PowerShell post-exploitation agent built on cryptographically-secure communications and a flexible architecture.
  + Similar to Metaspliut framework, Empire sought to draw attention to the potential for PowerShell to be weaponised
  + Its original mission has since been fulfilled and it is no longer maintained by its authors as of 2019
+ What are the important components of Empire?
  + A **listener** is a process that runs on the C2 server and awaits connection requests from compromised hosts. This allows STDOUT data to route back to the C2 server's hell so the attacker can see what's happening.
  + And agent is a program that maintains a connection between C2 and the compromised host.
  + A **stager** is a snippet of code that allows malicious code to be run via the agent on the compromised host.
+ Stager types
  + The launcher stager (./lib/stagers/laucher.py) is a commonly-used stager module, and generates a one-liner stage0 launcher for an Empire agent
  + The launcher _bat stager generates a self-deleting .BAT file that executes a one-liner stage0 launcher for an Empire agent.
  + The macrostager generate and office macro that lauches and Empire stager. This macro can be embedded into any office document for the puposes of phishing.
  + The dll stager generates a reflectivly-injectable MSF-compliant .DLL that loads up the .NET runtime into a process and execute a download-cradle to stage and Empire agent. These .DLLs are the key to running Empire in a process that's not powershell.exe. Using these .DLLs with Metasploit is described here.
  + Modules execute malicious commonads, which can harvest credentials and escalate privileges, etc for the attacker