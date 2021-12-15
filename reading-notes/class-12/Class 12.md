## Class 12

### Reading: What Is a Security Operations Center (SOC)?

------

A security operations center (SOC), also called an information security operations center (ISOC), is a centralized location where an information security team monitors, detects, analyzes and responds to cybersecurity incidents, typically on a 24/7/365 basis.

The security team overseeas all activity on:

+ Servers
+ Databases
+ Networks
+ Applications
+ Endpoint devices
+ Websites

With the purpose of pinpointing potential security threats an thwarting them as quickly as possible. They also monitor external sources (such as threat lists) that may affect the organization's security posture.

A SOC deals with security problems in real time, while continually seeking ways to improve the organization's security posture.

On a larger scaale, there are also Global Securit Operations Centr (GSOC), coordinating security offices that literally span the globe.

#### What is the importance of a SOC?

SOCs offers assurance that threats will be detected and prevented in real time.

SOCs can:

+ Respond faster. The SOC provides a centralized, complete, real-time view of how the entire infrastructure is performing from a security standpoint, even if you have several locations and thousand of endpoints. You can detect, identify, prevent and resolve issue before they cause too much trouble for the business.
+ Protect consumer and customer trust. Consumers are already skeptical of most companies and are worried about their privacy. Creating a SOC to protect consumer and customer data can help built trust in your organization.
+ Minimize costs: While many organizations think establishing a SOC is cost prohibitive, the cost associated with a breach, including the loss of data, corrupted data or customer defection are much higher. Additionally, SOC personnel will ensure that you're using the right tools for your business to their full potential,, so ou won't waste money on ineffective tools.

#### What does a SOC do?

+ Proactive, around-the-clock surveillance of networks, hardware an software for threat and breach detection, and incident response.
+ Expertise on all the tools your organization uses, including third-party vendors, to ensure they can easilty resolve security issues.
+ Installation, updating and troubleshooting of application software.
+ Monitoring and managing of firewall and intrusion prevention systems.
+ Scanning and remediation of anitvirus, malware and ransomware solutions.
+ Email, voice and video traffic management.
+ Patch management and whitelisting.
+ Deep analysis of security log data from various sources.
+ Analysis, investigation and documentation of security trends.
+ Investigation of secuirty breaches to understand the root cause of attacks and prevent future breaches.
+ Enforcement of secuirty policies and procedures.
+ Backup, storage and recovery.

While not detecting threats. SOC is taksed with finding weaknesses. SOC staff are proactively looking at ways to improve security.

#### Who works in a SOC?

A typical team might be structured something like this:

+ Level 1: The first line of incident responders.They watch for alerts and determine each alert's urgency as well as when to move it up to Level2. Level 1 personnel may also manage security tools and run regular reports.
+ Level 2: These personnel usually have more expertise, so they can quickly get to the root of the problem and assess which part of the infrastructure is under attack. They will follow procedures to remediate the problem and repair any fallout, as well as flag issues for additional investigation.
+ Level 3: At this level, personeel consists of high-level expert security analysts who are actively searching for vulnerabilitties within the network. They will use advanced threat detection tools to diagnose weaknesses and make recommendations for improving the organization's overall security.
+ Level 4: This level consists of high-level managers and chief officers with the most years of experience. This groups oversees all SOC team activities and is responsible for hiring and training, plus evaluating individual and overall performance. Level 4s step in during crises, and, specifically, serve as the liaison between the SOC team and the rest of the organization. They are also responsible for ensuring compliance with organization, industry and government regulations.

#### What are the best practices for building a SOC?

Develop a strategy: A SOC is an important investment; there's a lot riding on your security planning. To create a strategy that covers your secuirty needs you have to consider:

+ What do you need secure? A single on-premises network, or global? Cloud or hybrid? How many endpoints? Are you protecting highly confidential data or consumer information? What data is most valuable, and most likely to be targeted?
+ Will you merge your SOC with your NOC or create two separate departments?
+ Do you need 24/7 availability from the SOC staff?
+ Will you build the SOC entirely in-house, or outsouce some or all functions to a third-party vendor?

Make sure you have visibility across your entire organization: It's imperative that you SOC has access to everything, no mater how small or seemingly insignigicant, that could impact security.

Invest in the right tools and srvices:

+ Security Information Event Manager (SIEM): This single security management system offers full visibility into activity within your netowrk, collecting, parsing and categorizing mavhine data from a wide range of sources on the network and analyzing that data sso you can act on it in real time.
+ Endpoint protection systems
+ Firewall
+ Automated application secuirty
+ Asset discovery system
+ Data monitoring tool
+ Governance, risk and compliance (GRC) system
+ Vulnerability scanners and penetration testing
+ Log management system

Hire the best and train them well, highest-level security analysts should possess these skills:

+ Ethical hacking
+ Cyber forensics
+ Reverse engineering
+ Intrusion prevention system expertise: Monitoring network traffic for threats would be impossible without tools. Your SOCs need to know the ins and outs of how to use them properly.

Consider all your options:

+ Internal SOCs
+ Virtual SOCs
+ Outsourced SOCs

A SIEM collects and organizes all the data coming from various sources within you network and offers your SOC team insigts so that they can quickly detect and respond to internal and external attacks, simplify threat management, minimize risk, and gain organization-wide visibility and security intelligence.

SIEM is critial for SOC taks, such as monitoring, incident response, log management, compliance reporting and policy enforcement. Its log management capabilities alone make it a necessary tool for any SOC. SIEM can parse through huge batches of security data coming from thousand of sources to find unusual behavior and malicious activity and stop it automatically. Much of that activity goes undetected without the SIEM.

### Lecture

------

#### Splunk Boss

Conference for security professional with challenges and exercises around splunk

+ Web site defacement (someone will hack into an web server and deface it)
+ Cyber kill chain (the order by which attackers get into environments)
+ Web vulberability scanners
+ OSINT 
+ Brute force attack
+ Dynamic DNS (DDNS)
+ Boss of the SOC
+ Demo

#### Advanced Persistent Threats

+ A skilled and determined cyber criminal who can use multiple vectors and entry points to navigate around defenses, breach your network in minutes and evade detection for months. APTs present a challenge for organizational cyber security efforts.

#### Web Site Defacement

+ Web site defacement is typically a form of haktivism, where the attacker infiltrates a web server and alters the front page to send a message
+ A hacktivist uses offensive security skills to influence policy and attempt to bring about social change

#### Cyber Kill Chain

+ Is a security model outlining the sequential phases of a cyber attack
+ Used by defenders to plan ways to interrupt or "break" the cyber kill chain and hopefully thwart the attacl entirely
+ Originially developed by Lockheed Martin
  1. Reconnaissance
     * Attacker is assessing the target from outside
     * Cost-benefit analysis
     * Gathering infromation
       * Active information gathering
       * Passive information gathering
  2. Weaponization
     + Threat actor develops malware payload designed to target newly-discovered vulnerabilities
     + Tools customized to target network
       + Whst will work?
       + How will I develop it?
       + Can I source the weapon from the dark web?
       + Can I tailor it to the target?
  3. Delivery
     + Malware payload delivered to target network or system
     + Example: Spear phishing attack, USB drop
     + Target email with a malicious attachment
     + Exploit mismanaged or misconfigured servers
  4. Exploitation
     + Malware executed
     + Discovered vulnerabilities exploited
     + Superuser access granted to threat actor
  5. Installation
     + Malware embeds itself into target systems
     + Additional malware components downloaded
  6. Command and Control
     + Management and communication established from attacker to malware infection
     + Facilitates greater movement witthin target network
  7. Action on Objectives
     + The goal of the threat actor
     + Mission-specific action are finally taken to achieve original objectives

#### Web Vulnerability Scanners

+ Automated tools that scan web applications to look for security vulnerabilities such as cross-site scripting (XSS), SQL injection, and cross-site request forgery (CSRF).
  + Burp suite

#### OSINT

+ Includes information that can legally be gathered for free, public sources about an individual or organization
+ Community databases of useful security information
  + Threatminer
  + VirusTotal: Is a community database of malware IOCs and has an API
  + Hybrid Analysis: is "a free malware analysis service for the community that detects and analyzes unknown threats using a unique Hybrid Analysis technology"
  + ThreatMiner is a threat intelligence portal designed to enable analysts to research under a single interface

#### Brute Force Attack

+ A brute force attack involves using automated authentication attempts to expedite the process of "guessing" the credentials to an account.

#### Dynamic DNS

+ Is a service that automatically updates a DNS with a web property's correct IP, even if that IP address changes.

#### Splunk Commands

+ The `metadata` command returns a list of sources, sourcetypes, or hosts from an index or search peer.
  + Returns information accumulated over time
  + Snapshot of an index over time frame, e.g. "last 7 days"