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