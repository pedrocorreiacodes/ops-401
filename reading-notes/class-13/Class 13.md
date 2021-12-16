## Class 13

### Reading: What is a reverse proxy? | Proxy servers explained

------

 A reverse proxy is a server that sits in front of web servers and forwards client request to those web servers.

Reverse porxies are implemented to help increase:

+ Security
+ Performance
+ Reliability

#### What's a proxy server?

 A forward proxy, often called a proxy, proxy server, or web proxy, is a server that sits in front of a group of client machines. Whent those computers make requests to sites and services on the internet, the proxy server intercepts those requests and then communicates with web servers on behalf of those clients, like a middleman.

Why add this middleman?

+ **To avoid state or institutional browsing restrictions** - Some governments, schools, and other organizations use firewalls to give their users access to a limited version of the internet. A forward proxy can be usd to get around these restrictions, as they let the user connect to the proxy rather than directly to the sites they are visiting.
+ **To block access to certain content** - Conversly, proxy can also be set up to block a group of users from accessing certain sites. For example, a school network might be configured to connect to the web through a porxy which enables content filtering rules, refusing to forward responses from Facebook and other social media sites.
+ **To protect their identify online** - In some cases, regular internet users simply desire increased anonymity online, but in other cases, internet users live in places where the fovernment can impose serious consequences to political dissidents. Criticizing the government in a web forum or on social media can lead to fines or imprisionment for these users. If one of these dissidents uses a forward proxy to connect to a website where they post politically sensitive comments, the IP address used to post the comments will be harder to trace back to the dissident. Only the IP address of the proxy server will be visible.

#### How is a reverse proxy different?

A reverse proxy is a server that sits in front of one or more web servers, intercepting requests from clients. This is different from a forward proxy, where the proxy sits in front of the clients. With a reverse proxy, when clients send requests to the origin server of a website, those requests are intercepted at the network edge by the reverse proxy server.

The reverse proxy server will then send requests to and receive responses from the origin server.

The difference between a forward and reverse proxy is subtle but important. A reverse proxy sits in from of an origin server and ensures that no client ever communicates directly with that origin server.

Benefits of a reverse proxy:

+ **Load balancing** - A website that gets millions of users every day may not be able to handle all of its incoming site traffic with a single origin server. Instead, the site can be distributed amogn a pool of different servers, all handling requests for the same site.

  In this case, a reverse proxy can provide a load balancing solution which will distribute the incoming traffic evenly among the different servers to prevent any single server from becoming overloaded. In the event that a server fails completely, other servers can step up to handle the traffic.

+ **Protection from attacks** - With a reverse proxy in place, a web site or service needs to reveal the IP address of their origin server(s). This makes it much harder for attackers to leverage a target attack against them, such as DDOS attack. Instead the attackers will only be able to target the reverse proxy.

+ **Global Server Load Balancing (GSLB)** - In this form of load balancing, a website can be distributed on several servers around the globe and the reverse proxy will send clients to the server that's geographically closest to them. This decreases the distances that requests and responses need to travel, minimizing load times.

+ **Caching** - A reverse proxy can also cache content, resulting in faster performance. For example, if a user in Paris visits a reverse-proxied website with web servers in Los Angeles, the user might acually connect to a local reverse proxy server in Paris, which will then have to communicate with the origin server in L.A. The proxy server can then cache (or temporaily save) the response data. Subsequent Parisian users who browse the site will then get the locally cached version from the Parisian reverse proxy server, resulting in much faster performance.

+ **SSL encryption** - Encrypting and decrypting SSL (or TLS) communication for each client can bee computationally expensive for an origin server. A reverse proxy can be configured to decrypt all incoming request and ecnrypt all outgoing responses, freeing up valuable resources on the origin server.

#### How to implement a reverse proxy

Some copanie build their own reverse proxies, but this requires intensive software and hardware engineering resources, as well as significant investment in physical hardware. One of the easiest and most cost-effective ways to reap all the benefits of a reverse proxy is by signing up for a CDN service.