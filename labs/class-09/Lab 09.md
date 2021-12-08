## Lab 09

### Part 1: Staging

------

You will need two VMs for today’s lab:

- Windows 10
- Ubuntu Linux Desktop

First prepare the Windows 10 environment.

- Download and install [Gpg4win 3.1.13](https://www.gpg4win.org/).

![Screenshot 2021-12-08 at 12.26.31](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 12.26.31.png)

![Screenshot 2021-12-08 at 12.27.26](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 12.27.26.png)

![Screenshot 2021-12-08 at 13.02.59](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.02.59.png)

### Part 2: Message Encryption with Gpg4win on Windows 10

------

#### Create a keypair in Kleopatra.

Open Keopatra and click **New Key Pair**:

![Screenshot 2021-12-08 at 13.06.54](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.06.54.png)

![Screenshot 2021-12-08 at 13.20.10](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.20.10.png)

#### Export the public key to your desktop as an OpenPGP Certificate and name it “public_key”.

Right click the new created key and click **Export...** name it `public_key`:

![Screenshot 2021-12-08 at 13.22.53](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.22.53.png)

#### View the public key with a text editor.

Right click the icon on the Desktop and select **Open With...** and choose **Notepad**:

![Screenshot 2021-12-08 at 13.24.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.24.32.png)![Screenshot 2021-12-08 at 13.24.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.24.48.png)

#### Export the private (“secret”) key to your desktop and name it “private_key”.

Right click the keys and click **Backup Secret Keys...**:

![Screenshot 2021-12-08 at 13.30.00](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.30.00.png)

Name the file `private_key`and click **Save**:

![Screenshot 2021-12-08 at 13.39.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.39.49.png)

![Screenshot 2021-12-08 at 13.40.30](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.40.30.png)

#### Create a text file on the desktop with a secret message inside it (some text).

![Screenshot 2021-12-08 at 13.44.26](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.44.26.png)

#### Use Kleopatra to encrypt the message.

Select **Sign/Encrypt** and select the newly created `secret_text.txt`file, click **Open**:

![Screenshot 2021-12-08 at 13.46.33](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.46.33.png)

![Screenshot 2021-12-08 at 13.47.41](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.47.41.png)

![Screenshot 2021-12-08 at 13.48.15](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.48.15.png)

#### Once you have received the encrypted message from your lab partner, decrypt it.

Right click and select **Decrypt and verify** the encrypted file:

![Screenshot 2021-12-08 at 13.55.56](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.55.56.png)

![Screenshot 2021-12-08 at 13.57.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.57.49.png)

To encrypt a file for others specify the email adress when encrypting:

![Screenshot 2021-12-08 at 13.59.20](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 13.59.20.png)

### Part 3: Email Encryption with GPG on Ubuntu Linux Desktop

------

Perform a full keypair generation operation in GPG:

You can check **GPG** version on your system with `gpg --version`:

![Screenshot 2021-12-08 at 14.42.28](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 14.42.28.png)

![Screenshot 2021-12-08 at 14.44.01](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 14.44.01.png)

#### Launch GNU Privacy Assistant (GPA) GUI key manager application. Your new keypair from GPG should appear here.

![Screenshot 2021-12-08 at 14.54.45](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 14.54.45.png)

#### Export your public key to your Ubuntu Linux desktop with a .txt file extension as “public_key”

Right click keys and select **Export Keys...** name them and click **Save**:

![Screenshot 2021-12-08 at 15.02.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.02.42.png)

![Screenshot 2021-12-08 at 15.02.55](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.02.55.png)

#### Export your private key to your Ubuntu Linux desktop with a .txt file extension as “public_key”.

Right click keys and select **Copy Private Key**:

![Screenshot 2021-12-08 at 15.22.53](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.22.53.png)

Create a text file on the desktop `private_key.txt`and paste from the clipboard:

![Screenshot 2021-12-08 at 15.25.05](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.25.05.png)

![Screenshot 2021-12-08 at 15.25.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.25.23.png)

![Screenshot 2021-12-08 at 15.26.29](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.26.29.png)

#### Compose a cleartext secret message.

![Screenshot 2021-12-08 at 15.27.45](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.27.45.png)

#### Encrypt the secret message with your recipient’s public key and sign it.

Open the `secret_message.txt`with GNU Privacy Assistant click on **File** and **Encrypt**:

![Screenshot 2021-12-08 at 15.29.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.29.32.png)

![Screenshot 2021-12-08 at 15.29.45](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.29.45.png)

![Screenshot 2021-12-08 at 15.30.05](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.30.05.png)

![Screenshot 2021-12-08 at 15.32.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 15.32.08.png)

#### When you receive the encrypted message from your lab partner, decrypt it.

Go to **File Manager** open the encrypted text an select **Decrypt the selected file**:

![Screenshot 2021-12-08 at 16.36.55](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-09/Screenshot 2021-12-08 at 16.36.55.png)

### Part 4: Certificates and SSL with OpenSSL

------

penSSL can help us with handling digital certificates. In this part of the lab you will create a CA, sign and issue certificates using [OpenSSL](https://pki-tutorial.readthedocs.io/en/latest/) certificate tutorial.

- The tutorial consists of three labs. Complete the Simple lab first. The subsequent Advanced and Expert labs are stretch goals.

  1. [Simple PKI](https://pki-tutorial.readthedocs.io/en/latest/simple/index.html)

  