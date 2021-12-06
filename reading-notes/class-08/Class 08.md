## Class 08

### Reading: What is Data Loss Prevention (DLP)?

------

Data loss preventin (DLP) is a set of **tools and processes** used to ensure that sensitive data is not loss, misused, or accessed by anauthorized users. DLP sotware classifies regulated, confidential and business critical data and identifies violations of policies defined by regulatory compliance such ash HIPPA, PCI-DSS or GDPR. Once violations are identified, DLS enforces remediation with alerts, encryption and other protective actions to prevent end uses from accidentally or maliciously sharing data that could put the organization at risk.

+ Monitor and control endpoint activities
+ Filter data streams on corporate networks
+ Monitor data in the cloud

All this to protect data **at rest**, **in motion** and **in use**.

+ Provides reporting to met compliance and auditing requirements
+ identify areas of weakness and anomalies for forencsic and incident response

#### 3 main use cases for Data Loss Prevention

+ Personal Information Protection / Compliance
+ IP Protection
+ Data Visibility

#### Why Data Loss Prevention?

The DLP makert evolved to include manage services, cloud functionallity and advanced threat protection amongst other things.

Nine trends that are driving the wider adoption of DLP:

+ The Growth of the CISO Role.
  + DLP provovides clear business value and gives CISOs the necessary reporting capabilities to provide regular updates to the CEO.
+ Evolving Compliance Mandates.
  + Global data protection regulation constantly change.
+ There are More Places to Protect Your Data.
+ Data Breaches are Frequent and Large
+ Your Organization Stolen Data is Worth More
+ There's a Security Talent Shortage

#### Data Loss Preventino Best Practices

+ Determine your primatry data protection objective.
+ DLP is not a security-only decision, buy-in from other executives
+ When researching DLP vendors, establish your evaluation criteria:
  + What types of deployment architectures are offered?
  + Do they support Windows, Linux, and OS X wit feature parity?
  + What deployment options do they offer? Do they provide managed services?
  + Do you need to defend against mainly internal or external threats? Or both?
  + Do you need to perform content or context-bases inspection and classification? Will your users be able to self-classify documents?
  + Are you most concerned with protecting structured or unstructured data?
  + Do you plan to see and enforce data movement based on policies, events, or users?
  + What compliance regulations are you bound by? What new regulations are on the horizon?
  + Who are their technology alliance partners and what technologies would you like to integrate with your DLP?
  + How quickly do you need to deploy or DLP program?
  + Will you need additional staff to manage your DLP program?
+ Clearlt define the roles and responsibilities of the individuals involved in your organization's DLP program.
+ Start with a clearly defined quick win.
+ Work together with business unit heads to define the DLP policies that will govern your organization's data. There's no right way to develop DLP policies. Often, DLP strategy will align with your corporate culture.
+ Document your processes carefully.
+ Define success metrics and share reporting with business leaders
+ DLP is a program, not a product, installing a dlp tool is just the first step in Data loss Prevention. DLP is a constant process of understanding your data and how usersm systems, and events interact with that data to better protect it.

#### Experts weigh in on data loss prevention

1. Data protection is everyone's job. "Everyone in a company is responsible for upholding data security standards. While the IT department does the majority of the everyday work with these systems and processes, stakeholders across your organization influence security policy and implementation".
2. Encryption is important. "Security is more than encryption, of course. But encryption is a critical component of security. While it's most invisible, you use strong encrption every day, and our Internet-laced world would be a far riskier place if you di not."
3. Be mindful of insider threats. Be proactive:
   1. Internal training for business users to feel responsible with knowledge, skill and awareness.
   2. Monitor activities that companies can employ that set up rules and parameters on what is considered appropriate for various employees to do as part of their work functions and flag instances that are outside of those rules.

### Lecture

------

#### Data protection

+ Data at rest
  + In some sort of persistent storage media
  + Encrypt the data, using techniques such as whole disk encryption, databae encryption, and file- or folder-level encryption
  + Apply permissions, Access Control Lists (ACLs)  to ensure only authorized users can read or modify the data
+ Data in transit (or data in motion)
  + Transmitted over a network
  + Protected by transport encryption, such a TLS or IPSec
+ Data in use
  + Present in volatile memory, such as system RAM or CPU registers and cache
  + Malicious intruder with rootkit access to the computer may be able to access it
  + Trusted execution environments/enclaves

Encryption ca be used to:

+ Protect confidentiality of data at rest
+ Protect confidentiality data in motion

How do we monitor what data gets transmitted?

+ ​	Data exfiltration:
  + Corporate espionage
  + Trade secrets 

#### Data Roles and Responsibilities

+ Oversight and management of a range of information assets within the organization
+ Data owner
  + Ultimate responsibility
+ Data steward
  + Data quality and oversight
+ Data custodian
  + Information systems management
+ Data privacy officer (DPO)
  + Oversight of personally identifiable information (PII) assets
+ Organizational roles in privacy legislation
  + Data controllers and data processors

#### Data Classifications

+ Public (unclassified)
  + No confidentiality, but integrity and availability are important
+ Confidential (secret)
  + Subject to administrative and/or technical access controls
+ Critical (top-secret)
+ Proprietary
  + Owned information of commercial value
+ Private/personal data
  + Data that can identify an individual
+ Sensitive
  + Special categories of personal data, such as beliefs, ethnic origin, or sexual orientation

#### Data Types

+ Personally identifiable information (PII)
  + Data can be used to identify, contact, or locate and indiviual
+ Customer data
  + Institutional information
  + Personal information about the customer's employees
+ Health information
  + Medical and insurance records and test results
+ Financial information
  + Data hel about bank and investment acccounts, plus information such as payroll and tax returns
+ Government data
  + Legislative requirements

#### Privacy Notices and Data Retention

+ Legislation and regulations
  + General Data Protection Regulation (GDPR)
  + Rights of data subjects
+ Privacy notices
  + Purpose of collecting personal information
  + Consent to delcared uses and storage
+ Impact assessments
  + Assess and mitigate risks from collecting personal data
+ Data retention
  + Keeping data securely to comply with policy/regulation/legislation
  + Audit requirements versus privacy requirements

#### Data Sovereignty and Geographical Considerations

+ Data sovereignty
  + Jurisdiction that enforces personal data processing and storage regulation
+ Geographical considerations
  + Select storage location to mitigate sovereignty issues
  + Define access controls on the basis of client location

#### Privacy Breaches and Data Breaches

+ Definition of a breach event
  + *At what point becomes a breach?*
  + Data breach versus privacy breach
+ Organizational consequences
  + Reputation damage
  + Identify theft
  + Fines
  + IP theft
+ Notifications of breaches
+ Escalation
+ Public notification and disclosure

#### Data Sharing and Privacy Terms of Agreement

+ Service level agreement (SLA)
  + Require access controls and risk assessment to protect data
+ Interconnection security agreement (ISA)
  + Requirements to interconnect federal systems with third-party systems
+ Non-disclosure agreement (NDA)
  + Legal basis for protecting information assets
+ Data sharing and use agreement
  + Specify terms for the way a dataset can be analyzed
  + Proscribe use of reidentification techniques

#### Why DLP?

+ Key drivers of DLP adoption
  + Growth of CISO role
  + Compliance
  + Complexity of technologies/mobile devices
  + Data breaches
  + Stolen data sold on dark web

#### Data Exfiltration

+ Data exfiltration methods
  + Removable media
  + Transferring over the network
  + Communicating data over the phone or by video
  + Taking a picture or video of text data
+ Ordinary countermeasures
  + Ensure that all sensitive data is encrypted at rest
  + Create and maintain offsite backups of data
  + Ensure that systems stroring or transmitting sensitive data are implementing access controls
  + Restric the types of network channels that attackers can use
  + Train users about documents confidentiality and the use of encryption to store and transmit data securely

#### Data Loss Prevention

*These tools analize raw data* 

They can run on the network layer by analyzing packets and dropping them.

+ DLP products scan files for matched strings and prevent unauthorized copying or transfer
  + Policy server
  + Endpoint agents
  + Network agents 
+ Cloud-based DLP
+ Remediation
  + Alert only
  + Block
  + Quarantine
  + Tombstone

#### Detection Scenarios

+ **True positive** occurs when an actual threat is detected
  + Optimal
+ **False positive** occurs when a non-real threat is detected
  + Annoying false alarm
+ **True negative** occurs when no threat was present, and no threat was detect
  + Optimal
+ **Flase negative** occurs when an actual threat was present, but no threat was detected
  + Most dangerous scenario

#### DLP Concepts

+ Detection
  + Positive match - Data scanned meets policy
+ Data type
  + What data classification is associated (and therefore, compliance)
+ Pattern
  + Text patterns the DLP system is lookinng for 
+ Policy
+ Confidence level 
  + How confident is the pattern detection rule that the detection is a true positive 