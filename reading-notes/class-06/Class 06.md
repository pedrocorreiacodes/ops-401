## Class 06

### Readings: Applying The CIA Triad To Your Enterprise File Transfer

------

THE **CIA Triad** is on of the basic building blocks of information security:

+ Confidentiality 
+ Integrity
+ Availability

Likewise the triad is a vital piece in establishing secure enterprise file transfers.

In order to establish a secure system you need to achieve these three objectivres:

#### Confidentiality

Refers to the principle of restricting access to or knowledge of certain pieces of information to certain individuals. Why?

+ A company might not want compeptitors to know its trade secrets, key personnel salaries, list of customers, products in development, or sales and maketing plans
+ A law firm might want to preserve attorney-client privilege
+ A healthcare organization may want to secure ePHI and comply with HIPPA/HITECH requirments
+ Trading partners might want to keep transaction details between themselves

#### Integrity

Pertains to the principle of preventing data from being tampered. Data integrity is particularly crucial in business transactions where anaunthorized alterations to data (either intentional or accidental) can lead to disputes, report misstatments and financial losses

Like confidentiality, integrity can likewise be compromised during data transfers through either man-in-the-middle attacks or through a direct hack on the server.

#### Availability

Making sure data is available at all times. Power interruptions, network disruptions, server failures, missing files, DDoS attacks, and natural disasters are just some of the many unfortunate events that can render data inaccessible.

Availability can be a serious problem especially if they involve business-critical data. More so ig the data is part of a supply chain, where serveral organizations or business units can suffer.

#### Technical solutions for achieving confidentality in enterprise file transfers

##### Confidentiality

Encryption is by far one of the most closely methods associated with confidentiality. Renders data unreadable, preserving that data's confidentiality.

Encryption solutions are grouped into two categories:

+ Those that encrypt data-at-rest
  + Usually achieve through **OpenPGP** or other disk-level or file-level encryption solutions
+ Those tht encrupt data-in-transit
  + SSL (e.g. FTPS, HTTPS. WebDAVs)
  + SSH (e.g. SFTP)

File transfers require both. Confidentiality exist while files are traversing the network (data in transit) and while they're stored on the server (data-at-rest).

When your encrypt data before (while in the sender's server), during (while traversing the network) and after (upon arrival ath the recipient's server) a file transfer, you call that end-to-end encryption.

Another method you can use to secure data confidentiality is authentication. Can help you restrict access to your confidential data to authorized individuals.

##### Integrity

To achieve data integrity in file transfer we can use:

+ **Hash functions**
+ **Digital Signatures**

These security elements are already available in secure file transfer protocols like FTPS, HTTPS, SFTP, and WebDAVs. These solutions will enable file transfer recipients to determine if the files they receive have been tampered along the way.

##### Availability

The best way to ensure file transfer service availability is to set up a high availability (HA) cluster. There are two ways:

+ **Active-passive HA configuration**: Setting up one or more failover server that can immediately take over should the primary server go down.
+ **Active-active HA configuration**: Set two or more servers in a way that they are both active servers. The main purpose of and active-active configuration is to distribute the workload and reduce the chance of a server from going down due to overload.



### Readings: What Are MD5, SHA-1, and SHA-256 Hashes, and How Do I Check Them?

------

Hashes are the products of cryptographic algorithm designed to produce a string of characters. Often thse strings have a fixed length, regardless of the size of the input data. Despite a very minor change in the input data, the resulting hashes are all very different from one another. Even if someone modifies a very small piece of the input data, the hash will change dramatically.

There are different hash functions like:

+ MD5
+ SHA-1
+ SHA-256

Sofware creeators often take a file download an run it through a hash function that they offer in an official list of the hashes on their websites. The user then can download the file and run the hash function to confirm that they have the original file and it hasn't been corrupted during the download process-

Usell to confirm the legitimacy of files.

'Collisions' have been found with the MD5 and SHA-1 functions. It's always prefered to use the SHA-256 when possible.

The hashes will always be identical if you're using the same hashing function on the same file. It doesn't matter which operating system you use.

##### Windows

`Get-FileHash C:\path\to\file.iso`

By default the command will show the SHA-256 hash for a file. We can specify the hashing algorithm to use:

`Get-FileHash C:\path\to\file.iso -Algorithm MD5`

`Get-FileHash C:\path\to\file.iso -Algorithm SHA1`

`Get-FileHash C:\path\to\file.iso -Algorithm SHA256`

`Get-FileHash C:\path\to\file.iso -Algorithm SHA384`

`Get-FileHash C:\path\to\file.iso -Algorithm SHA512`

`Get-FileHash C:\path\to\file.iso -Algorithm MACTripleDES`

`Get-FileHash C:\path\to\file.iso -Algorithm RIPEMD160`

##### macOS

`md5 /path/to/file`

`shasum /path/to/file`

`shasum -a 1 /path/to/file`

`shasum -a 256 /path/to/file`

##### Linux

`md5sum /path/to/file`

`sha1sum /path/to/file`

`sha256sum /path/to/file`

##### Conlusion

While hashes can help you confirm af ile wasn't tampered with, there's still one avenue of attack here. An attacker could gain control of a Linux distribution's website and modify the hashes that appear on it, or an attacker could performa a man-in-the-middle attack and modify the web page in transit if you were accessing the website via HTTP instead of HTTP.

That's why modern Linux distribution often provide more than hashes lists on web pages. They cryptographically sign these hashes to help protect against attackers that might attempt to modify the hashes. Cryptographic signature must be verified to ensure the hash file was actually signed by the Linux distribution.



### Lecture

------

