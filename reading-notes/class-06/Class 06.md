## Class 06

### Reading: Applying The CIA Triad To Your Enterprise File Transfer

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