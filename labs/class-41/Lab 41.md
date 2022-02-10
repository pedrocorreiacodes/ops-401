## Lab 41

### Part 1: Staging

------

This lab requires class-40-45-kali.ova VM.

![Screenshot 2022-02-08 at 12.21.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-08%20at%2012.21.18.png)

### Part 2: Profiling an APT Group

------

- Download the threat report for APT41.

![Screenshot 2022-02-08 at 13.27.14](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-08%20at%2013.27.14.png)

- Generally speaking, what TTPs does APT41 use (e.g. “lateral movement”)?

Insertion of malware into a build environment for later distribution with legitimate software. Lateral movement. Supply chain compromises. Incorporation of malicious code into legitimate executables and the signing of these files using legitimate digital certificates from the same compromised organization Command and control. Credential Access

- Identify and discuss at least one signature TTP, hash, or domain used by APT41. How can this knowledge help us protect against APT41?

![Screenshot 2022-02-08 at 14.00.06](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-08%20at%2014.00.06.png)

CRACKSHOT is a downloader that can download files, including binaries, and run them from the hard disk or execute them directly in memory. It is also capable of placing itself into a dormant state. We can add the file hash to our malware database to avoid its deployment on endpoints.

Let’s start with investigating the TA505 threat actor group and see what we can do to protect our organization against them.

- Use VirusTotal transformations to identify IP addresses associated with the following domains:
  - Filesharess[.]com
  - Live-en[.]com
  - See-back[.]com

![Screenshot 2022-02-10 at 11.56.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2011.56.41.png)

![Screenshot 2022-02-10 at 12.25.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2012.25.30.png)

- Include a screenshot of the resulting graph in your submission.

![Screenshot 2022-02-10 at 13.50.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2013.50.00.png)

- What can your organization do to defend its networks and users against these known malicious IP addresses? Name at least one specific tool or system you’d use.

We can blacklist the IP's associated with these domains. We can use for example a firewall like pfSense to block traffic from and to them

Next, let’s identify the hashes of known IOCs affiliated with these TA505 domains.

- Use Hybrid Analysis “Query Domain” transformation to identify the hashes and URLs of known IOCs associated with these malicious domains.
- Include this screenshot in your submission.

![Screenshot 2022-02-10 at 14.06.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2014.06.57.png)

+ Upload a hash to VirusTotal. Did this result in a positive?

![Screenshot 2022-02-10 at 15.15.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2015.15.02.png)

![Screenshot 2022-02-10 at 15.17.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2015.17.17.png)

It's a negative.

- Why or why not might an IOC hash result in a positive on VirusTotal?

It depends if the hash is already part of the VirusTotal database.

- What can your organization do to defend its networks and users against these known malicious artifacts? Name at least one specific tool or system you’d use.

We can use an Intrusion Prevention system (IPS) software capable of detecting the hashes of the malicious files. McAfee Network Security would be a good option.

### Part 3: Profiling a Company with Maltego Transforms and Machines

------

Maltego can be used to research a target organization to learn more about it in advance of an attack, such as a pentest.

+ Identify the MX record associated with myspace.com.

![Screenshot 2022-02-10 at 16.55.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2016.55.59.png)

- What is an MX record, and how does it affect mail server traffic for the domain, myspace.com?

Mail exchanger record, specifies the mail server responsible for accepting and sending email messages on behalf of a specific domain.

- If we wanted to disrupt the company’s mail server traffic, how could this information be useful to us as an attacker performing recon?

If we wanted to cmpromise email services for a specific domain we could go directly to the source.

DNS can tell us a lot about a company, if the WHOIS records are not obfuscated by the domain owner.

- Identify the email address(es) of the domain’s owner.

![Screenshot 2022-02-10 at 17.14.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.14.36.png)

![Screenshot 2022-02-10 at 17.15.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.15.02.png)

- Identify the phone number(s) of the domain’s owner.

![Screenshot 2022-02-10 at 17.16.24](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.16.24.png)

![Screenshot 2022-02-10 at 17.17.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.17.05.png)

- Where does the domain owner live? Include a screenshot of their Myspace page.

![Screenshot 2022-02-10 at 17.20.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.20.07.png)

![Screenshot 2022-02-10 at 17.21.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.21.50.png)

- How can this information be used by an attacker?

This information could be extremely usefull to an attacker in order to perform phishing or spearphishing attacks.

The “Machines” in Maltego perform automated investigations for us.

- Use the “Company Stalker” Machine against myspace.com.

 ![Screenshot 2022-02-10 at 17.29.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.29.56.png)

![Screenshot 2022-02-10 at 17.46.03](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.46.03.png)

- Explain how Maltego was able to retrieve this information using the Company Stalker Machine. In other words, what does the Company Stalker Machine do?

Apparently takes the emails associated with the domain and relates them with accounts created in myspace.

Pull up the Myspace page for one of the email addresses on the graph and include a screenshot of it (keep it work-appropriate!)

![Screenshot 2022-02-10 at 17.57.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.57.18.png)

Next, let’s try to find associated web entities to myspace.com.

- Using Machines, perform a Level 1 Footprint against the domain, myspace.com.

![Screenshot 2022-02-10 at 17.58.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.58.17.png)

- Include a screenshot of the results. What did this return?

![Screenshot 2022-02-10 at 17.59.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2017.59.15.png)

- Identify the mail servers associated with myspace.com. How did Maltego determine this relationship? (Hint: How does the internet work?)

Going through the DNS records associated with myspace.com. Maybe some kind o nslookup.

### Part 4: Reporting

Using the myspace.com Level 1 Footprint graph, generate a Maltego PDF report, upload it to your Google Drive, then link to it in your submission.

![Screenshot 2022-02-10 at 18.06.40](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/Screenshot%202022-02-10%20at%2018.06.40.png)

You can find the report [HERE](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-41/class41-report.pdf)
