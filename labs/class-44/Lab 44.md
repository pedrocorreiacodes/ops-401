## Lab 44

### Part 1: Staging

------

First, import the class-44-target.ova into Virtualbox. Assign it to NAT Network alongside your Kali Linux VM.

Next, import final-proj-kali-linux.ova into Virtualbox. Load all pentest scripts into this VM. Assign it to a NAT Network alongside your target box. You may opt to use your own existing Kali Linux instead, if you prefer.

![Screenshot 2022-02-15 at 15.29.40](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2015.29.40.png)

### Part 2: Enumeration

------

Now that you have imported the target system to Virtualbox, first determine its IP address using an enumeration tool of your choice.

Let's use Nmap to perform host discovery.

![Screenshot 2022-02-15 at 16.16.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2016.16.58.png)

![Screenshot 2022-02-15 at 16.18.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2016.18.37.png)

Target system's IP ` 10.0.2.21`.

After identifying the target system’s IP, you’ll need to get an idea of its vulnerabilities by using techniques such as:

- Port scanning
- Vulnerability scanning
- Banner grabbing/service fingerprinting

Let's keep using Nmap this time around with service and version detection:

`nmap -sS -sV <Target Ip>`

![Screenshot 2022-02-15 at 16.37.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2016.37.11.png)

```
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
23/tcp   open  telnet      Linux telnetd
25/tcp   open  smtp        Postfix smtpd
53/tcp   open  domain      ISC BIND 9.4.2
80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
111/tcp  open  rpcbind     2 (RPC #100000)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
512/tcp  open  exec        netkit-rsh rexecd
513/tcp  open  login?
514/tcp  open  shell?
1099/tcp open  java-rmi    GNU Classpath grmiregistry
1524/tcp open  bindshell   Metasploitable root shell
2049/tcp open  nfs         2-4 (RPC #100003)
2121/tcp open  ftp         ProFTPD 1.3.1
3306/tcp open  mysql       MySQL 5.0.51a-3ubuntu5
5432/tcp open  postgresql  PostgreSQL DB 8.3.0 - 8.3.7
5900/tcp open  vnc         VNC (protocol 3.3)
6000/tcp open  X11         (access denied)
6667/tcp open  irc         UnrealIRCd
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)
8180/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1
MAC Address: 08:00:27:2A:A6:94 (Oracle VirtualBox virtual NIC)
Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

Bingo, several ports running different services open:

![Screenshot 2022-02-15 at 16.39.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2016.39.02.png)

Let's try to exploit SSH to connect to the system and also try to exploit the database server.

### Part 3: Exploitation

------

Let's try to exploit a ftp brute force login:

`use auxiliary/scanner/ftp/ftp_login`

![Screenshot 2022-02-15 at 16.55.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2016.55.01.png)

Set the path of the file that contains the wordlist:

![Screenshot 2022-02-15 at 16.58.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2016.58.26.png)

Set the target IP address, user list and run:

![Screenshot 2022-02-15 at 17.07.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2017.07.54.png)

Let's create a simple user name and password list for demonstration purposes:

![Screenshot 2022-02-15 at 17.27.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2017.27.42.png)

Now let's brute force the SSH Service with `auxiliary/scanner/ssh/ssh_login`:

![Screenshot 2022-02-15 at 17.29.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2017.29.20.png)

Set host, user pass file and run:

![Screenshot 2022-02-15 at 17.37.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2017.37.30.png)

Success! We created 3 sessions. To interact with one of the three sessions, we use the command **msf > sessions –i 3** (for connecting with session 3):

![Screenshot 2022-02-15 at 17.39.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2017.39.48.png)

Let's try and exploit MySQL database:

Let's use the **mysql_login** module and try to bruteforce mysql username and password.

![Screenshot 2022-02-15 at 18.48.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2018.48.55.png)

![Screenshot 2022-02-15 at 18.52.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2018.52.21.png)

And we're in:

![Screenshot 2022-02-15 at 18.55.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/Screenshot%202022-02-15%20at%2018.55.41.png)

### Part 4: Reporting

------

Document your findings in the OSCP-OS-XXXXX-Lab-Report_Template3.2.docx file, removing any irrelevant templated example data. Upload this file to your Google Drive and link to it in your submission.

Find the report [HERE](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-44/OSCP-OS-XXXXX-Lab-Report_Template%202.pages).
