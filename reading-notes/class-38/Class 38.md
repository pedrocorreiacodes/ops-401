## Class 38

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