## Ops Challenge 35

### Part 1: Staging

------

#### Download and import the “class-35-webserv” OVA, insert the DVWA ISO, then boot from the ISO. Set it to NAT Network.

![Screenshot 2022-01-28 at 15.32.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2015.32.52.png)

![Screenshot 2022-01-28 at 15.39.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2015.39.19.png)

![Screenshot 2022-01-28 at 15.42.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2015.42.57.png)

#### Startup Kali Linux VM on the same NAT Network. Check that you can ping the web server and view its hosted page via browser.

![Screenshot 2022-01-28 at 15.50.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2015.50.59.png)

### Part 2: Basic Nmap Scans

------

#### Perform the highest intensity service and version scan against the target. What command did you use, and what was the outcome?

`nmap <target-IPaddress> -sV --version-intensity 9`

Host is up with four open ports for four different services:

+ 21/tcp - FTP
+ 22/tcp - ssh
+ 80/tcp - http
+ 3306/tcp - mysql

![Screenshot 2022-01-28 at 15.58.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2015.58.29.png)

![Screenshot 2022-01-28 at 16.01.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.01.20.png)

#### Attempt to detect the operating system of the target. Do you think the findings are correct?

We'll use the command `nmap <target-IPaddress> -A`to enable OS detection, version detection, script scanning and trace route:

Unix, Linux seems quite correct.

![Screenshot 2022-01-28 at 16.18.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.18.26.png)

#### Have Nmap perform a port scan of only the well-known port numbers. What command did you use?

We'll utilize `nmap <target-IPaddress> -p 0-1023` to scan the well known ports, these ports are assigned to specific server service by the Internet Assigned Numbers Authority (IANA):

![Screenshot 2022-01-28 at 16.26.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.26.09.png)

### Part 3: Scanning with the Nmap Scripting Engine (NSE)

------

#### Using Nmap in NSE mode, execute http-title.nse against the target.

![Screenshot 2022-01-28 at 16.38.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.38.11.png)

#### Using Nmap in NSE mode, execute http-enum.nse against the target. Post the output in your submission doc.

![Screenshot 2022-01-28 at 16.43.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.43.42.png)

#### From Mozilla Firefox in Kali Linux, access some of the enumerated files. What did you find out about this web server?

![Screenshot 2022-01-28 at 16.46.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.46.07.png)

![Screenshot 2022-01-28 at 16.48.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2016.48.43.png)

We can 'bypass' de login for the administrator to access the backoffice.

#### Using Nmap in NSE mode, execute vulscan.nse against the target web server and save the output to a file for easy viewing.

First install **Vulscan** by following the guide [HERE](https://github.com/scipag/vulscan).

Execute with the command `

```
nmap -sV --script=vulscan/vulscan.nse www.example.com
```

![Screenshot 2022-01-28 at 17.21.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2017.21.41.png)

#### Review the output for a CVE entry. Navigate your browser to the CVE MITRE site and look up the CVE. Paste a screenshot of this in your submission doc and explain the vulnerability in your own words.

![Screenshot 2022-01-28 at 17.39.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-35/Screenshot%202022-01-28%20at%2017.39.02.png)

This vulnerability allows authenticated threat actors to execute malicious code by abusing the database.
