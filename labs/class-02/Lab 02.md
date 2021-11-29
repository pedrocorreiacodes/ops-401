## Lab 02

### Part 1: Cloud Provider Research

------

#### AWS

AWS is SOC 2 compliant. AWS ensures that "Amazon employee user accounts are added, modified and deleted in a timely manner and reviewed on a periodic basis",  while keeping logs of systems incidents. “Data integrity is maintained through all phases including transmission, storage and processing” (AWS SOC 2 Report). AWS had no deviations in its audit results.

#### Azure: 

Azure shows deviation in criteria. The Azure SOC 2 Report states that  “for two of 27 sampled servers, records related to vulnerability scanning were not retained and were not available for inspection to corroborate the performance of vulnerability scanning”.

### Part 2: Provider Recommendation

------

#### Which IaaS provider should Initrobe adopt for its needs? Explain:

Based on Initrobe's needs AWS is recommended. It's SOC2 compliant without any deviations in the test results. It shows better reliability in data security.

##### **How is this provider SOC 2 compliant?**

The most recent audits show that all the standards of SOC2 are met.

##### Will Initrobe be able to store HR (PII) data on this platform? Explain.

AWS offers several methods designed to protect sensitive data for its entire lifecycle in AWS. They can help enhance  data security posture and be useful for fulfilling the data privacy regulatory requirements applicable to every organization for data protection at-rest, in-transit, and in-use.

##### Will initrobe be able to store financial (SOX) data on this platform? Explain.

AWS is fully SOC2 compliant and several major financial services also trust its services.

### Part 3: Cloud Security Policy

------

CLOUD SECURITY POLICY TEMPLATE:

1. Purpose
This policy ensures the confidentiality, integrity and availability of data stored, accessed and manipulated using cloud computing services. It establishes a framework of responsibility and actions required to meet regulatory requirements and security guidelines for cloud computing.

2. Scope
This policy applies to any and all company data that will be hosted on the cloud. Specifically, this policy applies to HR and to the financial team, as PII and financial reports will be hosted on the cloud service provider.

2.1 Information Types

This policy applies to all customer data, personal data and other company data defined as sensitive by the company’s data classification policy. The sensitive data types covered by this policy include:

+ Financial data:
  + Invoices
  + Payroll data
  + Revenue data
  + Accounts receivable data
  + Employee personal data:
  + Names and addresses
  + Social Security numbers
  + State-issued driver’s license number
  + State-issued identification card number
  + Financial account numbers, including security code, access code or password admitting access to the account  
  + Medical and/or health insurance information

3. Ownership and Responsibilities
  Cloud Security Administrator
  The person ultimately responsible for implementation, configuration and maintenance of cloud services security. This person shall address the following:

  +  Implementing security for new services

  +  Customizing the configuration of the cloud service security settings

  +  Maintaining access control and permissions management for each cloud service provided  

  + Retiring terminated services

    Service Level Manager

    + The person ultimately responsible for managing service-level agreements and acting as liaison with the cloud provider to negotiate SLA contracts and ensure the provider meets all the terms of those contracts.

4. Secure Usage of Cloud Computing Services
  All cloud-based services must be approved prior to acquisition and deployment. To ensure secure adoption and usage of cloud services, the following steps must be taken:

  + Define organizational needs and priorities.
  + Define service users, both internal and external.
  + Determine the type of cloud service to be adopted, including the physical and operational characteristics for SaaS, PaaS and IaaS solutions.
  + Define the data types to be stored.
  + Determine the security solutions and configurations required for encryption, monitoring, backups, etc.
  + Generate a list of past security incidents involving this cloud provider.
  + Request available security certifications.
  + Obtain copies of agreements with the provider, including SLAs.

4.1 Inventory
The cloud security administrator and IT security manager must perform an inventory of cloud services in use at least quarterly.

5. Risk Assessment
Data from the “Sensitive” tier of the Data Classification Policy shall be available at all times, per regulations, for discovery and audit. Cloud providers shall conform to these compliance requirements.
The Cloud Security Administrator and the IT Security team shall conduct a risk assessment at the following times:
+ Upon the implementation of a new cloud service
+ After major upgrades or updates to an existing cloud service  
+ After any changes to the configuration of a cloud service
+ When following up on a security event or incident
   Quarterly for all existing cloud service.
+ The cloud security risk assessment shall include the following:
+ Audit results, both internal and external (cloud provider system security audit results)  
+ Threat and vulnerability analysis
+ Regulatory compliance
6. Security Controls
  At the time of cloud service implementation and quarterly after that, the Cloud Security Administrator shall review each service-level agreement, as well as request and analyze the cloud provider’s security audits.
7. Security Incident Recover
  In the event of a data breach, both the cloud provider and the cloud security administrator shall perform an assessment of the systems and users that are directly or indirectly involved in the incident to determine the method of access, such as physical, via software/malware or through human error.
  Reporting requirements:
  + Daily incident reports shall be produced and handled by the IT Security Department or the Incident Response Team.
  + Weekly reports detailing all incidents shall be produced by the IT Security Department and sent to the IT Manager or Director.
  + High-priority incidents discovered by the IT Security Department shall be immediately escalated; the IT Manager should be contacted as soon as possible.
  + The IT Security Department shall also produce a monthly report showing the number of IT security incidents and the percentage that were resolved.
  + Priorities for data recovery:
    + All non-archived data classified as Sensitive is considered to have a priority of High.
    + All archived data classified as Sensitive is considered to have a priority of Moderate.
    + All data classified as Internal is considered to have a priority of Moderate.
    + All data classified as Public is considered to have a priority of Low.
8. Awareness-Raising
  The IT Security Management office shall provide quarterly security training to all users of cloud services. All users of cloud services must pass security training to maintain permissions and access to the service.
9. Enforcement
  Employees who attempt to use unauthorized services shall have their permissions revoked until they pass security training.
10. Related Documents
     Data Protection Policy
     Data Classification Policy
     Password Policy
     Risk Assessment Policy
     Encryption Policy
     Workstation Security Policy  Incident Response Policy
     Data Processing Agreement