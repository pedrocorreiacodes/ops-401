## Class 41

### Reading: What is penetration testing?

------

A penetration test, also known as a pen test, is a simulated cyber atack against your computer system to check for exploitable vulnerabilities.

Pen testing can involve the attempted breaching of any number of application systems (e.g., application protocol interfaces (APIs), frontend/backend servers) to uncover vulnerabilitites such as unsanitized inputs that are susceptible to code injection attacks.

Insights provided bu the penetration test can be used to fine-tune you WAF security policies and patch detected vulnerabilities.

##### Penetration Testing Stages

1. Panning and reconnaissance
   + Defininf the scope and goals of a test, including the systems to be addressed and the testing methods to be used.
   + Gathering intelligence (e.g., network and domain names, mail server) to better understand how a target works and its potential vulnerabilitites
2. Scanning - Understand how the target application will respond to various intrusion attempts
   + Static analysis - Inspecting and application's code to estimate the way it behaves while running. These tools can scan the entirety of the code in a single pass.
   + Dynamic analysis - Inspecting an application's code in a running state. This is a more practical way of scanning, as it provides a real-time view into an application's performance.
3. Gaining Access - This stage uses web application attacks, such as cross-site scripting, SQL injection and backdoors, to uncover a target's vulnerabilitites. Testers then try and exploit these vulnerabilities, typically by escalating privileges, stealing data, intercepting traffic etc, to understand the damage they can cause.
4. Maintaining Access - The goal of this sage is to see if the vulnerability can be used to achieve a persistent presence in the exploited system - long enough for a bad actor to gain in-depth access. The idea is to imitate advanced persistent threats, which often remain in a system for months in order to steal an organization's most sensitive data
5. Analysis - The results of the penetration test are then compiled into a report detailing:
   + Specific vulnerabilities that were exploited
   + Sensitive data that was accessed
   + The amount of time the pen tester was able to remain in the system undetected

#### Penetration testing methods

##### External testing

External penetration tests target the assets of a company that are visible on the internet, e.g., the web application itself, the company website, and email annd domain name servers. The goal is to gain access and extract valuable data.

##### Internal testing

In an internal test, a tester with access to an application behind its firewall simulates an attack by a malicious insider. This isn't necessarily simulating a rogue employee. A common starting scenarion can be an employee whose credentials were stolen due to a phishing attack.

##### Blind testing

In a blind test, a tester is only given the name of the enterprise that's being targeted. This gives security personnel a real-time look into how an actual application assault would take place.

##### Double-blind testing

In a double blind test, security personnel have no prior knowledge of the simulated attack. As in the real world, they won't have any time to shore up their defenses before an attempted breach

##### Targeted testing

In this scenario, both the tester and security personnel work together and keep each other appraised on their movements. This is a valuable training exercise that provides a security team with real-time feedback from a hacker's point of view.



### Lecture

------

#### Vulnerability Analyst 

Security professional that detects weakness in networks and then takes measures to help the organization correct and strengthen the system's security levels.

+ Develops risk-based mitifation strategies for networks, operating system, and applications
+ Organizate network-based scans to identify possible network security attacks and host-based scans to identify vulnerabilities in workstations, servers, and other network hosts.

#### Vulnerability Assessments

+ A vulnerability is a weakness in an information system, system security procedures, internal controls, or implementation that could be exploited or triggered by a threat source
  + Important to differentiate vulnerability, expliot, and risk
  + Not all vulnerabilitites are likely to be exploited or high risk
  + Prioritize your vulnerabilitites
+ Common Weakness Enumeration (CWE) is a community-developed list of software and hardware weakness types
+ Tenable's Nessus is a commercial vulnerability scanning software

#### Pentester Careers

+ Penetration testers perform simulated cyber attacks against your computer system to check for exploitable vulnerabilities and communicate findings
+ Not entry-level
+ Why do organizations request penetration testing?
  + Compliance
  + Confidentiality, revenue, goodwill
  + Verify secure configuration
  + Security training
  + Testing new technology
+ An ethical hacker is someone who performs the legal exploitations of vulnerabilitites for companies with their express permission
  + Not a professional job title
  + Not a useful industry terminology
+ A penetration test is formalized hacking process where vulnerabilities are discovered and exploited
  + Simulate real-world attacks
  + Findings are documented and reported
+ Security testing
  + Not a penetration test
  + Test software behavior for security problems
  + Bring an outdated system up to date
  + Software security testing during SDLC
+ Vulnerability testing
  + Not a penetration test
  + Finding vulnerabilitites but not exploiting them

#### Phase  1: Pan & Recon

+ Planning
  + How will we approach this pentest?
  + What does the client need from us?
  + Report deliverables
    + Offensive Security Pentest Report
  + Scope of work
    + Rules of engagement ditacte in clear, unambiguous terms the limits to the pentest engagement
    + Example: Allowed to access a system but not chane it or damage it
  + Pentesters perform reconnaissance against their taget in order to gain more information aout what they're about to attack
  + Types of reconnaissance
    + Passive: OSINT, observing, and sniffing. Information Gathering
    + Active: Interacting with target and probing network for weaknesses
  + Desired intelligence and outcomes
    + Company background
    + Document: Penetration testing plan
    + Penetration test objectives and scope
    + Objectives
      + List exactly what will be tested
      + Mutually agreed boundaries
      + Exclusions and constraints
      + Downtime and affected parties
      + Approach and documentation
      + Key findings
      + Business metrics and impact

#### Maltego

+ How can we perform target invesigation to learn more about a company and its web footprint?
+ "Maltego is an open source intelligence (OSINT) amd graphical link analysis tool for gathering and connecting information for investigative tasks"
  + Desktop client
  + Supports data integration
+ A Maltego object/entity is either:
  + A person, company, domain, etc.
  + An artifact of online activity
+ A Maltego transform helps the user discover relationships to existing entities

