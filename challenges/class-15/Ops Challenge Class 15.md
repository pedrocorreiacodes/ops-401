## Ops Challenge: Class 15

### Part 1: Staging

------

#### First prepare your lab environment.

##### Standup your target, a SSH server, locally using a virtualization platform like Virtualbox.

###### For a more “black box” experience today, consider deploying [Metasploitable 2](https://information.rapid7.com/download-metasploitable-2017-thanks.html).

![Screenshot 2021-12-23 at 14.00.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.00.42.png)

 The default username and password are “**msfadmin”**.

##### Ensure that Kali Linux shares a subnet with your target.

![Screenshot 2021-12-23 at 14.15.11](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.15.11.png)

![Screenshot 2021-12-23 at 14.20.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.20.23.png)

##### Identify the following tools on your Kali Linux distribution

+ Patator

![Screenshot 2021-12-23 at 14.24.02](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.24.02.png)

- THC Hydra

![Screenshot 2021-12-23 at 14.25.07](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.25.07.png)

- Medusa

![Screenshot 2021-12-23 at 14.25.26](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.25.26.png)

- Metasploit

![Screenshot 2021-12-23 at 14.25.50](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.25.50.png)

- BurpSuite

![Screenshot 2021-12-23 at 14.26.16](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.26.16.png)

- Nmap Scripting Engine (NSE)

![Screenshot 2021-12-23 at 14.37.43](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.37.43.png)

##### In Kali, install `ipcalc`.

Run `sudo apt-get update -y` and `sudo apt-get install -y ipcalc`:

![Screenshot 2021-12-23 at 14.41.33](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.41.33.png)

![Screenshot 2021-12-23 at 14.42.07](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.42.07.png)

##### Add a new user and set this user’s password to something extremely weak.

![Screenshot 2021-12-23 at 14.51.31](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.51.31.png)

We went with the strongest password ever, `12345`.

##### Validate your SSH server is working by logging in from the Kali VM. Logout when finished testing.

![Screenshot 2021-12-23 at 14.57.51](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 14.57.51.png)

### Part 2: Scouting with Nmap

------

#### Generate the IP configuration of your Kali VM.

![Screenshot 2021-12-23 at 15.53.56](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 15.53.56.png)

#### Run ipcalc against your Kali VM’s IP address to generate some useful network information.

![Screenshot 2021-12-23 at 16.09.13](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 16.09.13.png)

#### From terminal, issue a nmap command to scan your network for hosts with open SSH ports.

Use the command `nmap -p 22 <subnet> `:

![Screenshot 2021-12-23 at 16.37.31](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 16.37.31.png)

##### Identify your target SSH server from the list of hosts.

Target is at IPaddress `192.168.60.3`.

### Part 3: Attack SSH using Brute Force

------

#### Select one of the five tools listed in Part 1.

##### Attempt to utilize its brute force attack technique to determine the SSH password of your target system.

Here I'm using **Medusa**:

![Screenshot 2021-12-23 at 17.41.46](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 17.41.46.png)

##### What do you notice about the time required to do this?

It takes a really long time.

##### This looks like it will take a very long time! Let’s speed this up by switching to a dictionary attack.

![Screenshot 2021-12-23 at 17.05.22](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-15/Screenshot 2021-12-23 at 17.05.22.png)

### Part 4: Reporting

------

##### Describe the advantages and disadvantages of using this tool.

In this particular case one disadvantage is that you have to know the username of particular machine running an ssh service on an open port. If the password is a a complex one it really could take a lot of time. 

On the other hand if the password is a basic one you just have to wait patiently sit back and relax.

##### How many authentication attempts did your tool make against the SSH server?

When using the `rockyou.txt`dictionary it only took 2 attempts because the password was on top of the list.