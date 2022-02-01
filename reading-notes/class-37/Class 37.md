## Class 37

### Reading: What is Burp Suite?

------

Burp Suite is a suite of Tools from PortSwigger designed ot aid in the penetration testing of web applications over both HTTP and HTTPS. The primary tools is a proxy designed to allow the analysis and editing of web traffic. The proxy can intercept web requests and responses and read and edit them in real-time before they reach their respective destinations.

The proxy itself allows you to configure which domains have their web traffic intercepted and what sort of traffic is shown. For example, intercepting web requests is helpful as you can edit them to test how the wesit reacts to unusual requests, howeber intercepting the responses there's no real point in editing the.

Many of the tools included in Burp Suite are designed to integrate with the main proxy and can have requests imported to them.

+ Intruder allows you to import a request and then configure arrange of payloads to attempt and can then run through them automatically.
+ Repeater allows you to import a web request and them make manual modification to it and see the response side by side allowing you to make minor adjustments to attempted exploits and easily see if it's working.
+ A dashboard feature shows a list of identified issues, allthough these need to be manually checked for false positives.
+ Sequencer is designed to analyse the randomness of data such as sessions IDs, CSRF tokens, and password reset token. The analysis requires more than 100 samples but can identify weaknesses in how supposedly random values are being generated.
+ Decoder allows you to decode strings from a range of encoding standards as well as allowing you to encode data again.
+ Comparer allows you to compare two strings to check for minor differences.

A broad range of community-written extensios is available for free from within the app, although some require features limited to the paid version of Burp Suite. 

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