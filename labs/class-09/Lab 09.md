## Lab 09

### Part 1: Staging

------

You will need two VMs for today’s lab:

- Windows 10
- Ubuntu Linux Desktop

First prepare the Windows 10 environment.

- Download and install [Gpg4win 3.1.13](https://www.gpg4win.org/).

![Screenshot 2021-12-08 at 12.26.31](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2012.26.31.png)

![Screenshot 2021-12-08 at 12.27.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2012.27.26.png)

![Screenshot 2021-12-08 at 13.02.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.02.59.png)

### Part 2: Message Encryption with Gpg4win on Windows 10

------

#### Create a keypair in Kleopatra.

Open Keopatra and click **New Key Pair**:

![Screenshot 2021-12-08 at 13.06.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.06.54.png)

![Screenshot 2021-12-08 at 13.20.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.20.10.png)

#### Export the public key to your desktop as an OpenPGP Certificate and name it “public_key”.

Right click the new created key and click **Export...** name it `public_key`:

![Screenshot 2021-12-08 at 13.22.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.22.53.png)

#### View the public key with a text editor.

Right click the icon on the Desktop and select **Open With...** and choose **Notepad**:

![Screenshot 2021-12-08 at 13.24.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.24.32.png)
![Screenshot 2021-12-08 at 13.24.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.24.48.png)

#### Export the private (“secret”) key to your desktop and name it “private_key”.

Right click the keys and click **Backup Secret Keys...**:

![Screenshot 2021-12-08 at 13.30.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.30.00.png)

Name the file `private_key`and click **Save**:

![Screenshot 2021-12-08 at 13.39.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.39.49.png)

![Screenshot 2021-12-08 at 13.40.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.40.30.png)

#### Create a text file on the desktop with a secret message inside it (some text).

![Screenshot 2021-12-08 at 13.44.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.44.26.png)

#### Use Kleopatra to encrypt the message.

Select **Sign/Encrypt** and select the newly created `secret_text.txt`file, click **Open**:

![Screenshot 2021-12-08 at 13.46.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.46.33.png)

![Screenshot 2021-12-08 at 13.47.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.47.41.png)

![Screenshot 2021-12-08 at 13.48.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.48.15.png)

#### Once you have received the encrypted message from your lab partner, decrypt it.

Right click and select **Decrypt and verify** the encrypted file:

![Screenshot 2021-12-08 at 13.55.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.55.56.png)

![Screenshot 2021-12-08 at 13.57.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.57.49.png)

To encrypt a file for others specify the email adress when encrypting:

![Screenshot 2021-12-08 at 13.59.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.59.20.png)

### Part 3: Email Encryption with GPG on Ubuntu Linux Desktop

------

Perform a full keypair generation operation in GPG:

You can check **GPG** version on your system with `gpg --version`:

![Screenshot 2021-12-08 at 14.42.28](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2014.42.28.png)

![Screenshot 2021-12-08 at 14.44.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2014.44.01.png)

#### Launch GNU Privacy Assistant (GPA) GUI key manager application. Your new keypair from GPG should appear here.

![Screenshot 2021-12-08 at 14.54.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2014.54.45.png)

#### Export your public key to your Ubuntu Linux desktop with a .txt file extension as “public_key”

Right click keys and select **Export Keys...** name them and click **Save**:

![Screenshot 2021-12-08 at 15.02.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.02.42.png)

![Screenshot 2021-12-08 at 15.02.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.02.55.png)

#### Export your private key to your Ubuntu Linux desktop with a .txt file extension as “public_key”.

Right click keys and select **Copy Private Key**:

![Screenshot 2021-12-08 at 15.22.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2013.22.53.png)

Create a text file on the desktop `private_key.txt`and paste from the clipboard:

![Screenshot 2021-12-08 at 15.25.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.25.05.png)

![Screenshot 2021-12-08 at 15.25.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.25.23.png)

![Screenshot 2021-12-08 at 15.26.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.26.29.png)

#### Compose a cleartext secret message.

![Screenshot 2021-12-08 at 15.27.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.27.45.png)

#### Encrypt the secret message with your recipient’s public key and sign it.

Open the `secret_message.txt`with GNU Privacy Assistant click on **File** and **Encrypt**:

![Screenshot 2021-12-08 at 15.29.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.29.32.png)

![Screenshot 2021-12-08 at 15.29.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.29.45.png)

![Screenshot 2021-12-08 at 15.30.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.30.05.png)

![Screenshot 2021-12-08 at 15.32.08](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2015.32.08.png)

#### When you receive the encrypted message from your lab partner, decrypt it.

Go to **File Manager** open the encrypted text an select **Decrypt the selected file**:

![Screenshot 2021-12-08 at 16.36.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2016.36.55.png)

### Part 4: Certificates and SSL with OpenSSL

------

penSSL can help us with handling digital certificates. In this part of the lab you will create a CA, sign and issue certificates using [OpenSSL](https://pki-tutorial.readthedocs.io/en/latest/) certificate tutorial.

- The tutorial consists of three labs. Complete the Simple lab first. The subsequent Advanced and Expert labs are stretch goals.

  1. [Simple PKI](https://pki-tutorial.readthedocs.io/en/latest/simple/index.html):

     

  1. Create Root CA

  ![Screenshot 2021-12-08 at 18.35.34](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.35.34.png)

![Screenshot 2021-12-08 at 18.37.47](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.37.47.png)

2. Create Signing CA

![Screenshot 2021-12-08 at 18.40.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.40.42.png)

3. Operate Signing CA

![Screenshot 2021-12-08 at 18.45.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.45.43.png)

![Screenshot 2021-12-08 at 18.47.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.47.45.png)

4. Output Formats

![Screenshot 2021-12-08 at 18.54.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.54.56.png)

5. View Results

![Screenshot 2021-12-08 at 18.57.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-09/Screenshot%202021-12-08%20at%2018.57.18.png)

### Part 5: Reporting

------

#### How can public key encryption utilities ensure integrity and confidentiality of data between two parties?

Encryption is known as the process of converting plaintext into cipher text. That means that ecrypted text is unreadable for human eyes. In the case of public key encryption one algorithm is used for encryption and a related algorithm decryption with pair of keys, one for encryption and other for decryption. Plain text is encrypted using receiver public key. This will ensures that no one other than receiver private key can decrypt the cipher text.

Confidentiality is achieved when we the message is kept private, only the sender and receiver can read the message.

The digital signature also ensures the authentication of the sender. The sender wil encrypt the plain text using his own private key.  This will make sure the authentication of the sender because the receiver can decrypt the cipher text using sends public key only. Using signatures, we can cryptographically prove the integrity and ownership of a message.

#### Is PGP a secure protocol to be using? 

The original PGP might present some security issues, newer versions such as OpenPGP are recommended.

#### Why is PGP not very popular among casual computer users?

Due to it's complexity of use. Slower comunication. 

#### Identify a website on the internet that does NOT have HTTPS (SSL) encryption in place

http://www.videolan.org/

#### Why do you think the website lacks SSL encryption?

Possibly they're keeping the security mechanism hidden from the user.

#### What steps should the web administrator take in order to reconfigure the site to use SSL encryption?

1. Identify all web servers and services that need to be encrypted. 
2. Get certificates for web servers and services that need them.
3. Configure the web server to use HTTPS, rather than HTTP. 
4. Administer and manage certificates.
