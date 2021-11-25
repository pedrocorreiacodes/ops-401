## Lab 01

------

### Part 1

------

Using the provided templates, create the following deliverables:

#### **Security Architecture Narrative**

We were brought in to help Inititrobe’s CTO conduct an assessment of their security landscape, make **recommendations**, and create and implement Initrobe’s security policy and strategy. As a fully remote company relying heavily on cloud architecture such as IaaS, PaaS, and SaaS third party vendors. 

+ **Recommended** Incident Response procedure
  + Develop an Incident Response Team headed by a Cyber Security Champion whose goal is to empower employees with first principles for corporate network security to focus on providing excellent service to clients.
+ **Recommended** Business Continuity plan
  + Consider deploying failover server for the corporate network recommendation so employees and customers experience fewer disruptions in access to Initrobe.
+ **Recommended** recovery plans
  + By using a corporate network, no secure data should be on personal computers, but instead on their user profiles associated with their job-title privileges/accessConsider third-party software such as VEEAM and/or automating the security of data created, changed, and moved around.Create and run basic logging tasks for all users on the network.
+ **Recommended** vendor and tools auditing software/solution
  + Further conversations to clarify Initrobe’s needs, but perhaps something like Netwrix auditing software could help with organization



#### **Initrobe Product Architecture**

Initrobe provides SaaS known as “Initron” to its clients via an entirely remote workforce. Employees therefore are paramount to the security architecture of the organization. Anything available on the web means network traffic is a significant risk to the CIA triad. There are extent policies to achieve some Confidentiality, Integrity, and Availability.

+ Extant Policies:
  + Data Security Acknowledgement Form
  + Laptop lending form (for employees using company computers)

+ Gap Recommendations:
  + **Recommended** Company InfoSec Champion for 1st-line of defence vigilance and awareness-raising through continual educational efforts
  + **Recommended** Company network topology; corporate network, VPN, captive portal for employees and clients.

#### **Initrobe Infrastructure**

**Product Infrastructure**

+ Describe product infrastructure, emphasizing security measures
+ The remote workforce really suggests thinking about cloud security on each endpoint. Whilst security champions and education are helpful and recommended, humans make mistakes. 
+ To help reduce human error, and inadvertent privilege creep, personnel will be authorized according to job title and corporate network access will be managed to assure users have access to only what they need to do their work.
+ **Recommended** MDM via PXE Booting corporate network login and/or secure user access via Mobile Devices with a captive portal that effectively limits access to the corporate network.

**Authorized Personnel**

+ AWS, Heroku, and Github root account access is granted only to the CTO and CEO
+ AWS IAM access is granted to CTO and CEO and our company for the duration of our contract.
+ Initrobe SSH access is granted to a limited group of Operators (standard employees)
+ Initrobe DB access is granted to a limited group of Data Operators (Finance and Sales employees)

#### **IT Infrastructure**

Initrobe uses the following cloud services for its internal infrastructure:

+ GSuite for email and Drive
+ AWS and Heroku for PaaS needs (MFA required, including for GitHub)
+ Slack for internal communication
+ Slab for internal documentation
+ Google Docs for additional documentation
+ Initron internal access via single sign-on Gdrive credentials
+ Gusto - HRIS with organizational chart information
+ Initron application access
+ Slack notifications to engineering for bugs & vulnerabilities
+ Clubhouse Project Management tool
+ Periodic static and dynamic application analysis

Access to these cloud services is limited according to the role permissions for job descriptions (see Authorized Personnel above). This is reviewed quarterly as well as via regular onboarding/offboarding tasks for new and departing employees.

#### **Initrobe Workstations**

Initrobe workstations are hardened against logical and physical attack by the following measures:

+ Full-disk encryption
+ Automatic lockscreens
+ Onboard antivirus/antimalware software
+ OS and AV automatically updated
+ Configured password manager application
+ Workstation compliance with these measures is evaluated on a quarterly basis.

#### **Remote Access**

+ Many Initrobe employees work remotely on a regular basis and connect to production and internal IT systems via the same methods as those employees connecting from the Initrobe physical office, i.e., direct encrypted access to cloud services. It is the employee’s responsibility to ensure that only authorized personnel use Initrobe resources and access Initrobe systems.

#### **Access Review**

Access to Initrobe infrastructure, both internal and product, is reviewed quarterly and inactive users are removed. Any anomalies are reported to the security team for further investigation. When employees start or depart, an onboarding/offboarding procedure is followed to provision or deprovision appropriate account access.

#### **Penetration Testing**

Initrobe commissions an external penetration test on an annual basis. All findings are immediately reviewed and addressed to the satisfaction of the CTO/CEO.

+ There are no records of third-party pentesting currently.
+ **Recommended**: schedule third-party evaluation before SOC-2 audit

#### **Initrobe Physical Security**

+ Initrobe lacks on-site premises.
+ Initrobe infrastructure is located within AWS, Heroku, and Github cloud services.
+ Initrobe does not have physical access to these services’ infrastructure.

### **Risk Assessment**

Initrobe should update its Cyber Risk Assessment on an annual basis in order to keep pace with the evolving threat landscape. The following is an inventory of adversarial and non-adversarial threats assessed to be of importance to Initrobe.

#### **Adversarial Threats**

+ Threat actors and malware may seek vulnerabilities between employees and Cloud services to exploit company data.
+ Present Domain Vulnerabilities
  + Lacks corporate NAC (with one, VPN tunnelling, captive portal, and other network access control measures can be deployed)
  + **Recommendedx2:** Put company data behind a corporate network and deploy security measures available in those software applications such as Windows Server ADAC, WSUS, and router firewall rules/configuration.

####  **Non-Adversarial Threats**

+ Employees are the first line of defense with education; without cyber security awareness, employees can be the most challenging of non-adversarial threats.
+ Domain access among contractors is lax
  + Contract employees comprise upwards of ¼ of the entire workforce, so shoring up onboarding and offboarding for this particular group is of utmost concern.
  + **Recommended** policy update/implementation for appropriate credential usage (including NON-sharing practices)

### **References**

#### **Narratives**

+ Products and Services Narrative System Architecture Narrative

#### **Policies**

+ Encryption Policy Log Management Policy 
+ Office Security Policy Remote Access Policy
+  Security Incident Response Policy 
+ Workstation Policy

#### **Procedures**

+ Apply OS Patches Review & Clear Low-Priority Alerts Review Access Review Devices & Workstations

### **Information Security Policy**

**Purpose and Scope:**

1. This information security policy defines the purpose, principles, objectives and basic rules for information security management.
2. This document also defines procedures to implement high level information security protections within the organization, including definitions, procedures, responsibilities and performance measures (metrics and reporting mechanisms).
3. This policy applies to all users of information systems within the organization. This typically includes employees and contractors, as well as any external parties that come into contact with systems and information controlled by the organization (hereinafter referred to as “users”). This policy must be made readily available to all users.

**Background:**

This policy defines the high level objectives and implementation instructions for the organization’s information security program. It includes the organization’s information security objectives and requirements; such objectives and requirements are to be referenced when setting detailed information security policy for other areas of the organization. This policy also defines management roles and responsibilities for the organization’s Information Security Management System (ISMS). Finally, this policy references all security controls implemented within the organization.Within this document, the following definitions apply:

1. *Confidentiality*: a characteristic of information or information systems in which such information or systems are only available to authorized entities.
2.  *Integrity*: a characteristic of information or information systems in which such information or systems may only be changed by authorized entities, and in an approved manner.
3. *Availability*: a characteristic of information or information systems in which such information or systems can be accessed by authorized entities whenever needed.
4. *Information Security*: the act of preserving the confidentiality, integrity, and, availability of information and information systems.
5. *Information Security Management System (ISMS)*: the overall management process that includes the planning, implementation, maintenance, review, and, improvement of information security.

**Policy:**

 *Managing Information Security*

1. The organization’s main objectives for information security include the following:
   + Good security begins with each user
   + Each user will be educated and trained to operate over the company network to maximize Confidentiality, Integrity, and Availability for Initron SaaS
2. The organization’s objectives for information security are in line with the organization’s business objectives, strategy, and plans.
3. Objectives for individual security controls or groups of controls are proposed by the company management team, including but not limited to [list key roles inside the organization that will participate in information security matters], and others as appointed by the CEO; these security controls are approved by the CEO in accordance with the Risk Assessment Policy (Reference (a)).
4. All objectives must be reviewed at least once per year.
5. The company will measure the fulfillment of all objectives. The measurement will be performed at least once per year. The results must be analyzed, evaluated, and reported to the management team.

  *Information Security Requirements*

1. This policy and the entire information security program must be compliant with legal and regulatory requirements as well as with contractual obligations relevant to the organization.
2. All employees, contractors, and other individuals subject to the organization’s information security policy must read and acknowledge all information security policies.
3. The process of selecting information security controls and safeguards for the organization is defined in Reference (a).
4. The organization prescribes guidelines for remote workers as part of the Remote Access Policy (reference (b)).
5. To counter the risk of unauthorized access, the organization maintains a Data Center Security Policy (reference (c)).
6. Security requirements for the software development life cycle, including system development, acquisition and maintenance are defined in the Software Development Lifecycle Policy (reference (d)).
7. Security requirements for handling information security incidents are defined in the Security Incident Response Policy (reference (e)).
8. Disaster recovery and business continuity management policy is defined in the Disaster Recovery Policy (reference (f)).
9. Requirements for information system availability and redundancy are defined in the System Availability Policy (reference (g)).



### **Employee Onboarding**

Employee Onboarding Procedure is designed to ensure that all employee onboarding is fully completed, all SaaS tools are provisioned, and the process is recorded to minimize risk and ensure compliance.Initrobe Onboarding Procedure:

+ Create new user via Windows ADAC to add user groups for privilege settings
+ Associate the new user with GSuite login for SSO credentials.
+ Set-up 2-step MFA
+ Security Training and Review and repeated throughout duration of employment
+ Provision Incident Response Team new-hire FAQ, authored by Cyber Champion
+ Provision corporate network remote access instructions
+ Provision requested device(s)

### **Employee Offboarding**

Employee Offboarding Procedure is designed to ensure that all employee offboarding is fully completed, all software is deprovisioned, physical access is restricted, and the process is recorded to minimize risk and ensure compliance.

Initrobe’s Offboarding Procedures:

+ Remove user profile access immediately.
+ Lock email; back up email; delete the account.
+ Retrieve any provision device, erase and reformat
+ Transfer employee assignments and accounts from their profile
+ Backup and log all user activity for as long as possible, storage permitting. 