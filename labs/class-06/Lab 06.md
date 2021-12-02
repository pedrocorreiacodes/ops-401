## Lab 06

### Part 1: Staging

------

#### Deploy a Linux VM on a cloud provider of your choosing. Ubuntu Linux 20.04 Focal Fossa works fine for this.

On **Amazon Lightsail** go to **Create an instance** select a region and pick the instance image, **Linux/Unix** > **Ubuntu 20.04** and click **Create Instance** at the bottom of the page:

![Screenshot 2021-12-02 at 11.31.57](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 11.31.57.png)

![Screenshot 2021-12-02 at 11.34.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 11.34.08.png)

#### In your Linux VM install OpenSSH

On the terminal run:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install openssh-client
```

![Screenshot 2021-12-02 at 11.56.06](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 11.56.06.png)

![Screenshot 2021-12-02 at 12.03.47](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.03.47.png)

Run `sudo systemctl enable ssh`:

![Screenshot 2021-12-02 at 12.04.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.04.48.png)

Open firewall on tcp port 22 with `sudo ufw allow ssh`:

![Screenshot 2021-12-02 at 12.05.43](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.05.43.png)

Check status with `sudo systemctl status ssh`:

![Screenshot 2021-12-02 at 12.14.47](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.14.47.png)

### Part 2: Secure File Transmission with SFTP on Linux

------

#### Deploy a SFTP server on your cloud Linux system

On the Ubuntu machine create a directory that will house our FTP data

```
mkdir -p /data
chmod 701 /data
```



![Screenshot 2021-12-02 at 12.30.40](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.30.40.png)

![Screenshot 2021-12-02 at 12.32.03](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.32.03.png)

Create a special group for the SFTP users withs `groupadd sftp_users`:

![Screenshot 2021-12-02 at 12.33.15](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.33.15.png)

Create a special user that doesn't have regular login privileges, but does belong to our newly created sftp_users group with `useradd -g sftp_users -d /upload -s /sbin/nologin USERNAME`:

![Screenshot 2021-12-02 at 12.35.27](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.35.27.png)

`USERNAME`is the name of the user create. 

Set a user password that will be the password of the new users to log in with the sftp comand.

`passwd USERNAME`

![Screenshot 2021-12-02 at 12.37.41](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.37.41.png)

Create an upload directory, specific to the new user, and then give the directory the proper permissions with:

```
mkdir -p /data/USERNAME/upload
chown -R root:sftp_users /data/USERNAME
chown -R USERNAME:sftp_users /data/USERNAME/upload
```

![Screenshot 2021-12-02 at 12.41.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.41.23.png)

![Screenshot 2021-12-02 at 12.42.17](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.42.17.png)

Now we have to configure the SSH daemon by opening up the configuration file and adding the following to the bottom of the file:

```
Match Group sftp_users
ChrootDirectory /data/%u
ForceCommand internal-sftp
```

![Screenshot 2021-12-02 at 12.44.37](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.44.37.png)

![Screenshot 2021-12-02 at 12.45.54](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.45.54.png)

Restart SSH with the command `systemctl restart sshd`:

![Screenshot 2021-12-02 at 12.46.40](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 12.46.40.png)

Now time to test our connection to the sftp server, spoiler alert, it works!!!

![Screenshot 2021-12-02 at 13.01.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 13.01.44.png)

#### Document your setup and file transmission process with screenshots and descriptions.

Let's create a test file:

![Screenshot 2021-12-02 at 14.01.59](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.01.59.png)

Now login into the SFTP server:

![Screenshot 2021-12-02 at 14.03.26](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.03.26.png)

To upload from our current directory (the directory from which you type the `sftp` command is the local working directory and thus the source directory for this operation). Let's use the `put filename`command:

![Screenshot 2021-12-02 at 14.12.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.12.23.png)

To download to our current directoy use `get filename`command:

![Screenshot 2021-12-02 at 14.14.05](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.14.05.png)

### Part 3: Secure File Transmission with SCP on Linux

------

See OpenSHH installation above and here's the file transmission between a local machine and the UBUNTU vm:

![Screenshot 2021-12-02 at 14.42.02](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.42.02.png)

### Part 4: Encryption and Decryption on Linux

------

As the administrator of the Ubuntu Linux VM, dump the password hash file or strings:

` /etc/passwd` stores te user account information.

` /etc/shadow` the optional encrypted password file.

![Screenshot 2021-12-02 at 14.48.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.48.23.png)

![Screenshot 2021-12-02 at 14.52.33](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-06/Screenshot 2021-12-02 at 14.52.33.png)

### Part 5: Reporting

------

#### Explain the need for secure data transmission as it relates to confidentiality

Data transmission refers to data in transit. Without secure data transmission a threat actor could, capture the data in transit. That is reffered to a Man-in-the-middle attack. If data is not encrypted it could be catpured a read as plain text.

#### Explain the difference between FTP and SFTP.

File Transfer Protocol is used to transfer file between a client and server on a computer network. When you send and receive files via FTP they are not encrypted. The transmissions and the file themselves are not encrypted.

With Secure FIle Tansfer Protocol the connection is encrypted, and the fle transfer process is more secure

#### Do they use the same ports?

No, FTP uses port 21 and SFTP uses port 22.

#### Do they use the same software?

Most software that supports FTP also supports SFTP

#### What are some examples of software used to access FTP and SFTP servers?

SFTP: OpenSSH, VanDyke VShell Server, CrushFTP.

FTP: SCP Server, CrushFTP,  FileZilla.

#### How does SCP protect the data being transmitted? Does it?

SCP used SSH (port 22), SSH protocol provides authentication and encryption.

#### How difficult was it to exfiltrate credentials from Linux system files?

It was fairly easy after you know the filesystem structure and how to navigate it.