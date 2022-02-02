## Class 37

### Reading: ZAP - Getting Started

------

#### Security Testing Basics

Software security testing is the process of assessing and testing a system to discover risks and vulnerabilitites of the system and its data. There is no universal terminolog, aassessments is the analysis and discovery o vulnerabilitites without attempting to actually exploit those vulnerabilitites.

Security testing:

+ **Vulnerability Assessment** - The system is scanned an analyzed for security issues.
+ **Penetration Testing** - The system undergoes analysis and attack from simulated malicious attackers.
+ **Runtime Testing** - The system undegoes analysis and security testing from an end-user.
+ **Code Review** - The system code undergoes a detailed revieew and analysis looking specifically for security vulnerabilities.

Risk assessment is not included in this list because risk assessment is not actually a test but rahter the analysis of the perceived severity of different risks and any mitigation steps for those risks.

#### More About Penetration Testing

Pentesting is carried out as if the tester was a malicious external attacker with a goal of breaking into the system and either stealing data or carrying out some sort of denial-of-service atack.

Pentesting has the advantage of being more accurate because it has fewer false positives (result that report a vulnerability that isn't actually present), but can be time-consuming to run.

Pentesting is also used to test defense mechanism, verify response plans, and confirm security policy adherence.

Automated pentesting is an important part of continuous integration validation. It helps to uncover new vulnerabilities as well as regressions for previous vulnerabilities in an environment which quickly changes, and for which the development may be highly collaborative and distributed.

#### The Pentesting Process

Both manual and automated pentesting are used, often in conjunction, to test everything from servers, to networks, to devices, to endpoints. This document focuses on web application or web site pentesting.

Pentesting usually follows these stages:

+ Explore - The tester atempts to learn about the system being tested. This includes trying to determine what software is in use, what endpoints exists, what patches are installed, etc. It also includes searching the site for hidden content, known vulnerabilities, and other indications of weakness.
+ Attack - The tester attempts to exploit the known or suspected vulnerabilitites to prove they exist.
+ Repot - The tester reports back the results of their testing, including the vulnerabilities, how they exploited them and how difficult the exploits were, an the severity of the exploitation.

##### Pentesting Goals

**The ultimate goal of pentesting is to search for vulnerabilities so that these vulnerabilities can be addressed**. It can also verify that a system is not vulnerable to a known class or specific defect; or, in the case of vulnerabilities that have been reported as fixed, verify that the system is no longer vulnerable to that defect

### Lecture

------

#### OWASP Top 10

+ OWASP Top 10 Web Application Security Risks (November 2021)
  1. Broken Access Control
  2. Cryptographic Fails - poorly implemented or legacy.
  3. Injection attack - SQL injection attack
  4. Insecure Design - *Poor ways to implement an website*
  5. Security Misconfiguration
  6. Vulnerable and Outdated Components - time from disclosure to patch being released and implemented - *1 to 3 weeks*.
  7. Identification and Authenticatin Failures
  8. Software and Data Integrity Failures
  9. Security Logging and Monitoring Failures
  10. Server-SIde Request Forgery (SSRF) - *grabbing your cookies and leverage them*

#### HTTP cookies

+ Tracking cookies - Data to track all the interactions with the website
+ Sessions cookies - Data to track your session on the website

#### Cross-Site Scripting

+ The main purpose of this attack is to steal the other user's identity data - cookies, sessions tokens and other information
  + In most of the cases, this attack is being used to steal the other person's cookies.

#### WebSocket

+ WebSocket is a compouter communication protocol, providing full-duplix communication channels over a single TCP connection
  + Enables interaction between web browser and web server over TCP 443 or 80
  + Separate protocol from HTTP but both on layer 7, reliant on TCP at layer 4.
  + All popular browsers support WebSocket

#### Zen Attack Proxy

+ OWASP Zed Attack Proxy (ZAP) is a web application security test tool that acts as a MITM proxy.
  + Features include:
    + Intercepting Proxy
    + Active and Passive Scanners
    + Traditional and Ajax Spiders
    + Brute Force Scanner (more common with HTTP)
    + Web sockets

#### Proxy Server

+ Traditionally, a proxy servers acts as a gateway between you PC and the internet.
  + Gives them a bottlenet source.
  + A separate computer with its own IP.
  + Historically, on-orem enterprises used proxies to secure traffic into and out of the company LAN.
+ We can setup ZAP as a "proxy" to Mozilla Firefox
  + All web traffic will be routed to and from ZAP, which will make the finaldecisions regarding when traffic will pass through

#### Zed Attack Proxy

+ Why use ZAP to perform web app security assessments?
  + Automated CI/CD testing via ZAP API
  + More "experimental" than the traditional go-to Burp
  + Free and open source flagship active OWASP project
  + No rate throttling brute force attacks, simpler. to usem don't have to pass to Hydra
  + Automatic scanning
  + Drawbacks VS Burp
    + Less "mature"
    + Somewhat less popular

#### Exploration

*We want to know what's there, what it is vulnerable to*. Discovery,

+ How do I use ZAP
  + First, perform web app exploration procedures
    + The Traditional Spider (Crawlers) discoer the HTML resources (hyperlinks etc) in the web application
    + The Ajax Spider works better if the application heavily relies with Ajax calls
    + Proxy Regression /Unit Test are good for security regressions testing
      + Use if you already have a test suite or unit tests in place
    + OpenAPI/SOAP Definition works if you have a well defined OpenAPI definition

#### Performing Scans

+ Next, scan for vulnerabilitites
+ In a passive scan, all requests proxied through ZAP or initialized by Spider are passively sccaned
  + Passive scanning does not change or modify requests
+ Active scans are attacks against the trarget URL.
  + VIew status
  + View results
  + Stop active scanning
+ Getting results
  + Security vulnerabilities are displayed as alerts sorted by priority (risk)

#### Authenticated Scans

+ ZAP is able to perform authenticated scans against the target
  + Form-based authentication
  + Script-based authentication
  + JSON-based authentication
  + HTTP/NTLM based authentication (VERY UNSAFE)
+ General steps
  + Step 1. Define a context
  + Step 2. Set the authentication mechanism
  + Step 3. Define your auth parameters
  + Step 4. Set relevant logged in/out indicators
  + Step 5. Add a valid user and password