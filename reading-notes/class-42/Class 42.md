## Class 42

### Reading: What is Mimikatz: The Beginner's Guide

------

Benjamin Deploy originally created Mimitkatz as a proof of concept to show Microsoft that their authentication protocols were vulnerable to attack. Instead, he inadvertently created one of the most widely used and downloaded hacker tools of the past 20 years.

#### What is Mimikatz?

Mimikatz is an open-source application that allows users to view and save authenication credentials like kerberos tickets.

Attackers commonly use Mimikatz to **steal credentials** and **escalate privileges**: in most cases, endpoint protection software and anti-virus systems will detect and delete it.

Pentesters use Mimikatz to detect and exploit vulnerabilities in your networks so you can fix them.

#### What Can Mimikatz Do?

Mimikatz originally demonstrated how to exploit a single vulnerability in the Windows authentication system. Now the tool demonstrates several different kinds of vulnerabilities **Mimikatz can perform credential-gathering techniques** such as:

+ Pass-the-Hash: Windows used to store password data in an NTLM hash. Attackers use Mimikatz to pass that exact hash string to the target computer to login. Attackers don't even need to crack the password, they just need to use the hash string as is. It's the equivalent of finding the master key to a building on the floor. You need that one key to get into all the doors.
+ Pass-the-Ticket: Newer version of windows store password data in a construct called a ticket. Mimikatz provides functionality for a user to pass a kerberos ticket to another computer and login with that user's ticket. It's basically the same as pass-the-hash otherwise.
+ Over-Pass the Hash (Pass the Key): Yet another flavor of the pass-the-hash, but this techniques passes a unique key to impersonate a user you can obtain from a domain controller.
+ Kerberos Golden Ticket: This is a pass-the-ticket attack, but it's a specific ticket for a hidden account called KRBTHT, which is the account that encrypts all of the other tickets.  A golden ticket gives you domain admin credentials to any computer on the network that doesn't expire.
+ Kerberos Silver Ticket: Another pass-the-ticket, but a silver ticket takes advantage of a feature in Windows that makes it easy for you to use services on the network. Kerberos grants a user a TGS ticket, and a user can use that ticket to log into any services on the network. Microsoft doesn't always check a TGS after it's issued, so it's easy to slip it past any safeguards.
+ Pass-the-Cache: Finally an attack that doesn't take advantage of Windows! A pass-the-cache attack is generally the same as a pass-the-ticket, but this one uses the save and encypted login data on a Mac/UNIX/Linux system.