## Lab 07

### Part 1: Staging

------

#### Class-05-cryptor VM

![Screenshot 2021-12-03 at 16.53.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2016.53.50.png)

![Screenshot 2021-12-03 at 17.09.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2017.09.02.png)

#### Windows 10 VM

A fresh Windows 10 box ready to go:

![Screenshot 2021-12-03 at 18.05.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.05.42.png)

![Screenshot 2021-12-03 at 18.23.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.23.30.png)

### Part 2: Windows FDE

------

In this particular machine I don't have a DC setup so let's edit the local group policy with `gpedit.msc`:

![Screenshot 2021-12-03 at 18.24.25](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.24.25.png)

Go to `Local Computer Policy > Computer Configuration > Administrative Templates > Windows Components > BitLocker Drive Encryption > Operating System Drives`:

![Screenshot 2021-12-03 at 18.25.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.25.19.png)

Toggle `Require additional authentication at startup` to `Enabled` and tick the box for “Allow BitLocker without a compatible TPM (requires a password or a startup key on a USB flash drive)":

![Screenshot 2021-12-03 at 18.25.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.25.44.png)

#### Save state your Windows 10 VM before proceeding

![Screenshot 2021-12-03 at 18.27.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.27.05.png)

#### Find BitLocker settings in Windows 10 and toggle it on.

Go to **Control Panel > System and Security > BitLocker Drive Encryption** and click **Turn on BitLocker**:

![Screenshot 2021-12-03 at 18.27.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.27.41.png)

#### Under “Choose how to unlock your drive at start” select “Enter a password” and enter your usual password.

![Screenshot 2021-12-03 at 18.28.34](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.28.34.png)

#### Under “How do you want to backup your recovery key” select “Print the recovery key” and save a PDF to your Desktop for now. In a production environment you’d want to save this to a backed up file server for recovery in the event of lockout.

![Screenshot 2021-12-03 at 18.29.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.29.53.png)

#### Select “Encrypt entire drive” since we’re attempting FDE.

![Screenshot 2021-12-03 at 18.32.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.32.21.png)

#### Select “New encryption mode”.

![Screenshot 2021-12-03 at 18.33.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.33.00.png)

#### Tick the box for “Encryption check” option.

![Screenshot 2021-12-03 at 18.33.29](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-07/Screenshot 2021-12-03 at 18.33.29.png)

#### Reboot. Grab a screenshot of “Enter the password to unlock this drive.”

![Screenshot 2021-12-03 at 18.33.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.33.29.png)

![Screenshot 2021-12-03 at 18.35.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.35.00.png)

#### After entering the password, it will take you to the normal user login. Login as normal. On the system tray at the bottom right, BitLocker should now begin encrypting your Windows C: drive. You’ll want to take a screenshot when it completes.

![Screenshot 2021-12-03 at 18.36.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.36.43.png)

### Part 3: Linux Directory Encryption

------

#### SSH into class-05-cryptor using cryptor/cryptor credentials.

![Screenshot 2021-12-03 at 18.51.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.51.19.png)

![Screenshot 2021-12-03 at 18.51.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2018.51.51.png)

#### Mount a new encrypted directory using eCryptfs.

Let's create a new directory called `secured`:

![Screenshot 2021-12-03 at 19.11.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2019.11.58.png)

Now we can encrypt the directory by mounting it with the file system type *ecryptfs* with `mount -t ecryptfs <pathtodirectory> <pathtodirectory>`. Select the secure password "passphrase",s elect cipher and specify options:

![Screenshot 2021-12-03 at 19.16.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2019.16.10.png)

#### Create a new .txt document within the encrypted directory. 

#### Try viewing the document. You should be able see the document because the directory is currently mounted.

![Screenshot 2021-12-03 at 19.26.03](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2019.26.03.png)

![Screenshot 2021-12-03 at 19.34.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2019.34.02.png)

#### Unmount the directory with the `umount` command.

![Screenshot 2021-12-03 at 19.28.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2019.28.26.png)

#### Try viewing the document. You should now only see the ciphertext. Include a screenshot of the ciphertext on your submission.

 ![Screenshot 2021-12-03 at 19.35.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-07/Screenshot%202021-12-03%20at%2019.35.51.png)

### Part 4: Reporting

------

#### What is the purpose of the TPM chip and why is it normally required in order to operate BitLocker on a Windows 10 PC?

THe purpose of the TPM chip is to protect any important passwords or encryption keys when they sent in an unencrypted form.

#### Are laptop computers secured against theft out of the box? What precautions can be taken to insure data confidentiality in the event of laptop theft?

Laptops are not secured against theft out of the box. We can encrypt sensible data to ensure confidentiality. Encryption can be applied to a single file or to a full disk (FDE).

#### What data theft scenarios do today’s tools *not* defend against?

A ransomware attack. Your encrypted data could be encrypted with another key. 

#### Consider data at rest VS data in motion. How do these two categories affect how you approach securing data?

Data at rest refers to data that is stored in some kind of database or hard drive. Data that is stationary. If a threat actor finds a way to get into this data the fact that the data is encrypted offers another layer of security. When you deal with data in motion you have to consider the type of connection the data is going through and the endopoint security. In the event of man-in-the-middle attack you want to be sure that the data is encrypted.
