## Class 36

### Reading: Cross-site scripting

------

#### What is cross-site scripting (XSS)?

**Cross-site scripting is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application.** It allows an attacker to circumvent the same origin policy, which is designed to segregate different websites from each other.

Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any action that the user is able to perform, and to access any of the user's data. If the victim user as privileged access withing the application, then the attacker might be able to gain full control over all of the application's functionality and data.

#### How does XSS work?

**Cross-site scripting works by manipulating a vulnerable web site so that it returns malicious JavaScript to users**. When the malicious code executes inside a victim's browser, the attacker can fully compromise their interaction with the application.

#### XSS proof of concept

You can confirm most kinds of XSS vulnerability by injecting a payload that causes your own browser to execute some arbitrary JavaScript. 

+ It's commaon practice to use the `alert()`function for this purpose because it's short harmless, and pretty hard to miss when it's succesfuly called.
+ From Chrome 92 onward, cross-origin iframes are prevented from calling `alert()`.
  + In this scenario, the `print()`function is recommended

#### What are the types of XSS attacks?

There are three main types of XSS attacks, these are:

+ **Reflected XSS**, where the malicious script comes from the current HTTP request.
+ **Stored XSS**, where the malicious script comes from the website's database.
+ **DOM-based XSS**, where the vulnerability exists in client-side code rather than server-side code.

#### Reflected cross-site scripting

The simplest variety of cross-site scripting. It arises when an application receives data in a HTTP request and includes that data within the immediate response in an unsafe way.

#### Stored cross-site scripting

**Store XSS** also known as persistent or second-order XSS, arises when an application receives data from an untrusted source and includes that data within is later HTTP responses in an unsafe way.

The data in question might be submitted to the application via HTTP requests, for example, comments on a blog post, user nicknames in a chat room, or contact details on a customer order. In other cases, the data might arrive from other untrusted sources, for example, a webmail application displaying messages receive over SMTP, a marketing application displaying social media posts, or a network monitoring application displaying packet data from network traffic.

#### DOM-based cross-site scripting

DOM-based XSS arises when an application contains some client-side JavaScript that processes data from an untrusted source in an unsafe way, usually by eriting the data back to the DOM.

#### What can XSS be used for?

An attacker who exploits a cross-site scripting vulnerability is typically able to:

+ Impersonate or masquerade as the victim user.
+ Carry out any action that the user is able to perform.
+ Read any data that the user is able to access.
+ Capture the user's login credentials.
+ Perform virtual defacement on the website.
+ Inject trojan functionality into the website.

#### Impact of XSS vulnerabilities

The actual impact of an XSS attack generally depends on the nature of the application, its functionality and data, and the status of the compromised user:

+ In a brochureware application, where all users are anonymous and all information is public, the impact will often be minimal.
+ In an application holding sensitive data, such as banking transactions, email, or healthcare records, the impact will usually be serious.
+ If the compromised user has elevated privileges within the applciation, then the impact will generally be critical, allowing the attacker to take full controls of the vulnerable application and compromise all users and their data.

#### How to find and test for XSS vulnerabilities

The vast majority of XSS vulnerabilities can be found quickly and reliably using Burp Suite's web vulnerability scanner.

Manyally testing for relfected and store XSS normally involves submittin some simple unique input into every entry point in the application, identifying every location where the submitted input is returned in HTTP respponses, and testing ech location individually to determine whether suitably crafted input can be used to execute arbitary JavaScript. In this way, you can determine the context in which the XSS occurs and select a suitable payload to exploit it.

Manyally testing for DOM-based XSS arising from URL parameters involves a simillar process: placing some simple unique input in the parameter, using the browser's deveoper tools to search the DOM for this input, and testing each location to determine whether it is exploitable However, other types of DOM XSS are harder to detect. To find DOM-based vulnerabilities in non-URL-based input (such as `document.cookie`) orn non-HTML-based sinks (like `setTimeout`), there is not substitute for reviewing JavaScript code, which can be extremely time-consuming. Bur Suite's web vulnerability scanner combines static and dynamic analysiss of JavaScript to reliably automate the detection of DOM-basd vulnerabilities.

#### Content security policy

Content security policy, is a browser mechanism that aims to mitigate the impact of cross-site scripting and some other vulnerabilities. If an application that CSP contains XSS-like behavior, then the CSP might hinder or prevent exploitation of the vulnerability. Often, the CSP can be circumvented to enable exploitation of the underlaying vulnerability.

#### Danglin markup injection

Dangling markupp injection is a technique that can be used to capture data cross-domain in situation where a full cross-site scripting exploit is not possible, due to input filters or other defenses. It can often be exploited to capture sensitive information that is visible to other users, including CSRF token that can be used to perform unauthorized action on behalf of the user.

#### How to prevent XSS attacks

Preventing cross-site scripting is trivial in some cases but can be much harder depending on the complexity of the application and the ways it handles user-controllable data.

In general, effectively preventing XSS vulnerabilities is likely to involve a combination of the following measures:

+ Filter input on arrival. At the point where user input is received, filter as stricly as posible based on what is expected or valid input.
+ Encode data on ouput. At the point where user-controllable data is output in HTTP responses, encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.
+ Use approrieate response headers. To prevent XSS in HTTP responses that aren't intended to contain any HTML or JavaScript, you can use the `Content-Type`and `X-Content-Type-Options`headers to ensure that browsers inerpret the responses in the way you intend.
+ Content Security Policy. As a last line of defense, you can use Content Security Policy to reduce the severity of any XSS vulnerabilities that sill occur.

#### Conclusion

+ How common are XSS vulnerabilities?
  + XSS vulnerabilities are very common, and XSS is probably the most frequently occuring web security vulnerability
+ How common are XSS attacks?
  + It is difficult to get reliable data about real-world XSS attacks, but it is probably less frequently exploited than other vulnerabilities 
+ What is the difference between XSS and CSRF?
  + XSS involves causing a web site to return malicious JavaScript, while CSRF involves inducing a victim user to perform actions they do not intend to do.
+ What is the difference between XSS and SQL injection?
  + XSS is a client-side vulnerability that targets other application users, while SQL injection is a server-side vulnerability that targets the application's database.
+ How do I prevent XSS in PHP?
  + Filter your inputs with a whitelist of allowed characters and use type hints or type casting. Escape your outputs with `htmlentities`and `ENT_QUOTES`for HTML contexts, or JavaScript Unicode escapes for JavaScript contexts.
+ How do I prevent XSS in Java?
  + Filter your inputs with a whitelist of allowed characters and use a library such as Google Guava to HTML-encode your output for HTML context, or use JavaScript Unicode escapes for JavaScript contexts.

### Lecture

------

#### Bannet Grabbing

+ Computers love to talk!
  + We can use this to our advantage anytime we're snooping for vulnerabilitites
+ Banner grabbing is a technique used by hackers and security teams to gain information about a computer system on a network and serices runing on its open ports
  + Active banner grabbing
  + Passive banner grabbing
+ NetCat utility is a versatile UNIX tools that can intereact with TCP, UDP, or UNUX-domain sockets
  + Open TCP connections
  + Send UDP packets
  + Listen on arbitrary TCP and UDP ports
  + Do port scanning
  + Suports both IPv4 and IPv6
+ Invoked in Linux with `nc`

#### Web Applications

+ Programs allowing better communication between business and their customers by way of a web browser interface
  + Frontend is usually created using languages like HTML, CSS, and Javascript supported by major borwsers.
+ Backend uses a programming stack
  + LAMP, MEAN, etc.

#### Web Application Security Careers

+ Application Security Engineer
+ Web application pentester
+ Web security specialist

#### OWASP TOP 10

+ Open Web Application Security Project is an international non-profit organization dedicated to web application security, most known for its list of top ten web application vulnerabilities
+ The OWASP top 10 is a regularly-updated report outlining security concerns for web application security including the 10 most critical risks
  + Extremley common in security interviews
  + Memorize and be able to explain how they work
+ OWAS Top 10 Web Application Security Risks (November 2021)
  1. Broken Access Control
  2. Cryptographic Failures
  3. Injection - tricking web server to do bad things
  4. Insecure Design - Bad infrastucture decisions
  5. Security Misconfiguration - People that look at policies but they don't really know how it works.
  6. Vulnerable and Outdated Components - Old software with known vulnerabilities, old dependecies
  7. Identification and Authentication Failures - Unencrypted credentials going back and forth, not supporting MFA
  8. Software and data Integrity Failures - DevOps and automations, depolyment pipeline is not secure
  9. Security Loggin and Monitoring Failures - No logs
  10. Server-Side Request Forgery (SSRF) - Acess the network and compromise the Web server.

#### HTML

+ Hyper Text Markup Language (HTML) is the standard markup language for creating Web pages

#### HTTP Cookies 

+ Small piece of data store on the user's computer by the web browser while browsing a website
  + Authentication cookies are the most common method used by web servers to know whether the user is logged in or not
  + Tracking coolies, and especially third-party tracking cookies, are commonly used as ways to compile long-term records of individuals browsing histories.
+ Cookies com in many flavors:
  + Session cookie
  + Persistent cookie
  + Secure coolie
  + HTTP-only cookie
  + Same-site cookie
  + Third-party cookie
  + Supercookie
  + Zombie cookie
  + Cookie wall

#### Cross-Site Scripting

+ Cross-site scripting (XSS) is a malicious code injection performed on client side of a web app, typically using Javascript and HTML
  + Some XSS attacks save a malicious script on the web server which can be executed in the victim's browser
+ The main purpose of this attack is to steal the other user's identity data - cookies, session token and other information.
  + In most of the cases, this attack is being used to steal the other person's cookies
  + Cookies help us to log in automatically
  + Therefore with stolen cookies, we can login with theother identities. And this is one of the reasons, why this attack is considered as one of the riskiest attacks.
+ Reflected cross-site scripting arises when the application receives data in an HTTP request and includes that data within the immedite response in an unsafe way

#### Web Security Dojo

+ Web Security Dojo is a free open-source self-contained training environment for Web Application Security penetration testing.
+ For learning and practicing web app security testing techniques
+ Self-teaching and skill assessment in self-contained environment
  + Tools, targets, and documentation

#### DVWA

+ Damn Vulneable Web App (DVWA) is a web application deliberately designed for training purposes
  + DVWA comes preinstalled on Web Security Dojo
+ W3AF is a web Application Attack and Audit Framework