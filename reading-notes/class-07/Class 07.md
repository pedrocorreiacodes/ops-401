## Class 07

### Reading: Data Protection: Data In transit vs. Data At Rest

------

**Data in transit** is data actively moving from one location to antoher, across the internet or through a private network.

Data protection in transit is the protection of data while it's traveling from network to network or being transfered from a local storage device to a cloud storage device. Data protectin measures for data in transit are critical as data is often considered less secure while in motion.

**Data at rest** is data at is not actively moving from device to decvice or network to network such as data stored on a hard drive, laptop, flash drive, or archived/stored in some other way.

Data protection at rest aims to secure inactive data stored on any device or network. Although data at rest is sometimes considered to be less vulnerable than data in transit, attackers often find data at rest a more valuable target than data in motion.

#### The role of encryption in data protection in transit and at rest 

There are multiple approaches to protecting data in transit and at rest. Encryption plays a major role in data protection and is a popular tool for securing data both in transit and at rest. For protecting data in transit, enterprises often choose to encrypt sensitive data prior to moving and/or use encrypted connections to protect the contents of data in transit. For protecting data at rest, enterprises can simply encrypt sensitive files prior to storing them and/or choose to encrypt the storage drive itself.

#### Best practices for data protection in transit and at rest

Unprotect data leaves enterprises vulnerable to attack. There are security measures that offer robust data protection across endpoints and networks to protect data in both states

In addition to encryption, best practices for robust data protection for data in transit and data at rest include:

+ Implement robust network security controls to help protect data in transit.
  + Firewalls
  + Network access control
+ Don't rely on reactive security to protect valuable data. Use proactive security measures to identify at-risk data. Implement effective data protection for data in transit and at rest.
+ Choose data protection solutions with policies that enable user prompting, blocking, or atomatic encryption for sensitive data in transit. such as when files are attached to an email message or moved to cloud storage, removable drives, or transferred elsewhere.
+ Create policies for systematically categorizing and classifying all company data, no matter where it resides, in order to ensure that the appropriate data protection measure are applied whle data remains at rest and triggred when data classified as at-rsk is accessed, used, or transferred.

Don't rely on the cloud service to secure data. Who has access to your data, how is it encrypted, and how often you data is backed up are all imperative questions to ask.



### Lecture

------

### Protecting Data at Rest

------

#### Cryptographic Cyphers

Ciphers: Algorithms used for encryption or decryption

+ Classical Ciphers 
  + Substitution Cipher: Plaintext substituted for ciphertext
  + Transposition Cipher: Plain text rearranged to form ciphertext
+ Key-based
  + Symmetric key algorithm
  + Asymmetric key algorithm
+ Input-based
  + Block cipher
  + Stream cipher

#### XOR Cipher

+ Additive cipher
+ Common component of other ciphers
+ It's perfectly balanced:
  + For a given plaintext input 0 or 1, the ciphertext result is equally likely to be either 0 or 1 for a truly random key bit

#### Symmetric vs. Asymmetric

##### Symmetric Encryption

+ Stream Cipher
+ Block Cipher

+ Uses a single key to encrypt and decrypt data

##### Asymmetric Encryption

+ Commonly referred to as Public-Key Cryptography
+ Widely used in certificate base authentication or PKI (Pubic Key Infrastructure)

#### Stream Ciphers

+ Start with a secret key or "seed"
+ Generate a keying stream
+ Combine the stream with Plaintext to produce cipher text
+ German Enigma machine, RC-4 and most pre-WWII ciphers were stream ciphers-
+ DIfficult to truly generate "random" key stream, XOR is typically used in most stread ciphers

#### Block Ciphers

+ Groups data into blocks instead of bits.
  + Typical block sizes are 64, 128 and 256 bits.
+ Whenever text is smaller than the block size is encrpted "padding" must be addedd to the data to help obscure it.
+ Usage
  + AES 256 is a 256 bit block cipher
    + Widely used globally

#### Ransonware

Is a type of malware that upon execution will encrypt sectors of the targeted file server or hard disk

+ Key belongs only to the ransomware creator
+ Payments to nation state actors may incur legal liability on the ransoware victim
+ Increase data availability by securely backing up important data to an outside location

How do we defend against ransomware? 

+ CyberHigiene 
+ Backups
+ Monitor logs
+ TEST the backup plan

#### Rootkit

A **rootkit** is a set of software designed to access areas of a computer that are restricted:

+ Hardware or firmware rootkit
+ Bootloader rootkiit
+ Memory rootkit
+ Kernel mode rootkits