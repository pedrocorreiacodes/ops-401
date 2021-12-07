## Class 09

### Readings: Public Key Infrastructure (PKI)

------

Public Key Infrastructure (PKI) is a technology for authenticating users and devices in the digital world.

The basic ideia is to have one or more trusted parties digitally sign documents certifying that a particular cryptographic key belongs to a particular user or device. The key then ca n be used as an identity for the user in digital networks.

Users and devices that have keys are often just called entities. In general, anything can be associated with a key that it can use as its identity such as program, process, manufacturer, component, or something else. The purpose of a PKI is to securely associate a key with an entity.

The trusted party signing the document associating the key with the device is called a certificate authority (CA). The certificate authority also has a cryptographic key that it uses for signing these documents. These documents are called certificates.

In the real world, there are many certificate authorities, and most computers and web browsers trust a hundred or so certificate authorities by default.

A public key infrastructure relies on a digital signature technology, which uses public key cryptography.

The secret key of each entity is only known by that entity and is used for signing. This key is called he private key. 

The public key derives from the private key, which is used for verifying signatures but cannot be used to sign. This public key is made available to anyone, and its typically included in the certificate document



### Lecture

------

#### Encoding

+ **Encoding** is the process of putting a sequence of characters into a specialized format
+ **Decoding** is the process of converting an encoded format back into the original sequence of characters

#### Public Key Infrastructure

Asymmetric key cryptography

+ Public key cryptography
+ Public key infrastructure (PKI
  + Certificates
  + HTTPS
  + Pretty Good Privacy (PGP)

#### Symmetric Encryption

+ Same secret key is used for encryption and decryption
+ Fast-suitable for bulk encryption of large amounts of data
+ Problem storing and distributing key securely
+ Confidentiality - only sender and recipient know the same key

#### Symmetric Algorithms

+ Modern, secure symmetric algorithms
  + **AES** (Advanced Encryption Standard, also known as Rijndael) is the most popular and widely used symmetric encryption algorithm
+ Insecure symmetric algorithms
  + **DES** 56-bit key size, practically broken, ca be brute-forced
  + **3DES (TRIPLE DES)** 64-bit cipher, considered broken
  + **RC2** 64-bit cipher, considered broken
  + **RC4** stream cipher, broken, pratical attacks demonstrated
  + **Blowfish** old 64-bit cipher, broken, practical attacks demonstrated
  + **GOST** Russian 64-bit block cipher, disputable security, considered risky

#### Asymmetric Encryption

+ Public/private key pair
  + If the public key encrypts, only the private key can decrypt
  + If the private key encrypts, only the public key can decrypt
  + Private key cannot be derived from the public key
  + Private key must be kept secret
  + Public key is easy to distribute (anyone can have it)
+ Message size is limited to key size not suitable for large amounts of data
+ Used for small amounts of authentication data

#### Asymmetric Alorithms

+ Assymmetric key cryptosystems provide:
  + Key-pair generation
  + Encryption algorithms
  + Digital signature algorithms
  + Key exchange algorithms
+ In public key cryptosystems, a message encrypted by the public key is later decrypted by the private key

#### Public Key Cryptography Algorithms

+ RSA algorithm (Rivest, Shamir, Adleman)
  + Basic of many public key cryptography schemes
  + Trapdoor function
  + Easy to calculate with the public key, but difficult to reverse without the private key
+ Eliptic curve cryptography (ECC)
  + Conerns about RSA being vulnerable to cryptanalysis
  + Another type of trapdoor function
  + Can use smaller keys to obtain same security

#### Public Key Infrastructure

+ Public Key Infrastructure (PKI) is a technology for authenticating users and devices in the digital world.
  + One or more trusted parties digitally sign documents certifying that a particular cryptographic key belongs to a particular user or device.
  + Key used as an identify for the the user in digital networks.
+ Advantage o PKI:
  + Scalable data and identity security
  + Credibility of keys validated by third party
    + Identity of the public key owner validated
+ Basic functions of PKI:
  + Establish the identity of endpoints on a network
  + Encrypt the flow of data via the network's communication channels

#### Public Key Infrastructure

What is PKI used for?

+ Secure Browsing (via SSL/TLS)
+ Securing Email (signing and encrypting messages)
+ Secure Code-signing
+ Network Security
+ File Security (via Encrypted File Systems

#### Public and Private Key Usage

+ Public key crytography
  + When you want others to send you confidential messages, you give them your public key to use to encrypt the message
  + When you want to authenticate yourself to others, you create a signature and sign it by encrypting the signature with your private key
+ But how does someone trust the public key?
+ Public key infrastructure (PKI) validates the identity of the owner of a public key
+ Public key is wrapped in a digital certificate signed by a certificate authority (CA)
+ Sender and recipient must both trust the CA

#### Certificate Authorities

+ Private CAs versus third-party CAs
+ Define services offered
+ Ensure validity of certificate and users
+ Establish trustworthy working procedures
+ Manage servers and keys

Example use case for PKI certificates:

+ Your organization is subject to export compliance regulation by the US government. The compliance officer must submit export compliance reports regularly to DECCS. but her computer is prompting for a certificate to validate her identity. Research DECCS policy and diagram the process.

How is PKI used?

+ HTTPS
  + Defends against a MitM and session hijacking
  + Preferred over HTTP (clear text)
+ Authenticating users and computers with SSH
+ Email signing and encryption using Pretty Godd Privacy (PGP)

#### Pretty Good Privacy (PGP)

+ Email signing and encryption using Pretty Good Privacy (PGP)
+ OpenPGP is the most current version
+ Original PGP developed in the 90s
  + Backwards compatibility means possibility of downgrade attack
  + Original PGP considered an insecure encryption method

#### GPC4Win

+ Gpg4win (GNU Privacy Guard for Windows) is encryption software for files and emails.
  + Securely transport emails and files with the help of encryption and digital signatures
  + Includes Kleopatra, a certificate manager
  + GNuPG is the backend that performs encryption processes
  + GPG is the Gnu Privacy Guard tools for Linux
  + GP (GNU Privacy Assistant) provides a GUI for KEy management in Linux