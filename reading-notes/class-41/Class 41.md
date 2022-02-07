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



#### Lecture

------

