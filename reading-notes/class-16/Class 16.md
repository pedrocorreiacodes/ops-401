## Class 16

### Reading: Lessons Learned From the Capital One Data Breach

------

The Capital One data breach was one of the most devastating data breaches of all time. A trusted financial services brand, Capital One has been a leader in digital transformation within the baking industry and a sophisticated user of cloud infrastructure.

Capital One disclosed the estimated the data loss at approximately 1 million Social Insurance Numbers of Canadian credit card customers, about 140,000 Social Security numbers and 80,000 linked bank account numbers of the credit card customers.

AWS provided their assessment of the incident:

+ The attack occurred due to a misconfiguration error at the application layer of a firewall installed by Capital One, exarcebating by permissions set by Capital One that were likely broarder than intended
+ After gaining access through the misconfigured firewall and having broader permission to access through the misconfigured firewall and having broarder permissions to access resources, **a SSRF attack was used**

#### Timeline

+ January 2019 to July 2019: 'Erratic' used TOR (The Onion network) to attempt connections, develop command scripts and other readiness activities. Multiple connections were made to connect to the servers, download pilot files to test out the end-to-end scenarios 
+ April 22, 2019: Capital One's customer information (700 folders worth of data) were posted on the erratic's public GitHub pages
  + IP address of a specific AWS server
  + Code for 3 commands used for the attack
    1. Get Credentials - First command when executed obtained security credentials know as ***-WAF-Role account (an IAM account) for an elevated role access AWS Web Apllication Firewall (WAF)
    2. List Buckets - Second command, when executed, used security credentials ****-WAF-Role account to list files and folders (aka S3 buckets)
    3. Download file - Third command, when executed used ****-WAF-ROle account to download files that were accessible by the credentials
+ June 26, 2019: 'Erratic' shared the colelct information casually on a public Slack channel used by a Meeup goup to communicate with its members
+ July 17, 2019: Capial One received an email informing about leaked data

#### Likely Attack Scenario

While the indictment is not specific about the nature of the attack, the following is an best guest regarding the likely spets taken by "erratic" to compromise the data.

+ STEP1: Login to the EC2 instance using SSH
  + It's very likely an EC2 instance was left over from a previous deployment with open SSH access. This was used to perform the SSRF attack.
+ STEP2: Discover a weak IAM role
  + Using the EC2 instance, the attacker must have been able to call the metadata sevices endpoint form the SSH command prompt.
  + The endpoint must have returned a role (according to the indictment ´****-WAF Role´)
+ STEP3: Gain temporary credentials
  + Using the role name, the attacker then could have queried the specific endpoint to gain access to temporary credentaisl 
+ STEP4: Gain access to S3 buckets by calling AWS S3 list and Sync
  + CLI commands
    + `$ aws s3 ls`
    + `$ aws s3 sync s3://somebucket`
      + The sync command would download all resources from the 'somebucket'

In summary, the most likely root cause of the attack was poor security architecture design that exposed S3 buckets via AWS/EC2 instance to anyone with an AM role.

While S3 buckets are not exposed to the internet like many others breaches, an EC2 instance with an excessive IAM role might have been the culprit.

A level of indirection, and a lower priviledged IAM role might have been a better architecture decision

#### AWS Components and Predicted Configurations and Usage during the attack

+ Firewall: A misconfiguration of AWS Web Application Firewall
+ IAM role access to S3: "CapitalOne determined that the first command, when executed obtained the security credentials for an account know as ***-WAF-Role that, in turn, enabled access to certain of Capital One's folders at Cloud Computing Company"
+ SSRF attack using AWS Metadata service: An SSRF attack tricks a server into executing commands on behalf of a remote user, enabling the user to treat the server as a proxy for his or her requests and get access to non-public endpoints.
  + An EC2 Iinstance was likely used to access AWS metadata service accessible at `http://169.254.169.254`. A particularly important function of the metadata service is to provide temporary credentials that give the node access to other AWS services based on a permission policy defined in the instance's IAM role.
  + IAM role are an alternative to long-lived user access keys and secrets; rather than hard coding an access key into an application's configuration, the application simply requests credentials from the metadata endpoint periodically.
+ EC2: Exposing unnecessary shell access, probably from a left-over development / staging or a production debugging deployment.
+ S3 bucket: Capital One determined that the third command when execued, used the ***-WAF-Role to extract or copy data from those folders or buckets in Capital One's storage space for which the account had the requisite permissions
  + Suggests that the attacker had access to 'was s3 sync' command

#### Recommendations

##### AWS Governance Practices

1. Don't allow EC2 instance to have IAM roles that alllow attaching or replacing role policies in any productino environments.
2. Clean up unused cloud resources (especially EC2 instances and S3 buckets) left over from prior development or production debugging efforts.
3. Review S3 bucket permissions, policies and access via both automation and manual audits.
4. See AWS basics at https://aws.amazon.com/premiumsupport/knowledgecenter/secure-s3-resources/ .
5. Use CloudTrail, CloudWatch and/or AWS lambda services to review and automate specific action taken on S3 resrouces.
6. Peridiocally review IAM roles

Ensure each application, EC2 instance, or autoscaling group has its own IAM role. Do not share role across unrelated applications.

Scope permission of each role to enable access only to the AWS resources required. The "WAF" role described above did not require access to list S3 buckets "in the normal course of business"

If possible, include a "Condition" statement within the IAM role to scope the access to known IP address on VPC enpoints.

##### AWS Configurations

If the following AWS cloud resource configurations were followed, the attack would have been prevented:

1. AWS IAM: Ensure least privileged IAM instance roles are used for AWS resource access from instances.
2. AWS IAM: Ensure IAM policies are attached only to groups or roles
3. AWS S3: Ensure AWS S3 buckets do not allow public READ access
4. AWS S3: Ensure AWS S3 buckets do not allow public READ_ACP access
5. AWS S3: Ensure AWS S3 buckets do not allow public WRITE_ACP access
6. AWS S3: Ensure S3 buckets do not allow FULL_CONTROL access to AWS authenticated users via S3 ACLs
7. AWS S3: Ensure that Amazon S3 buckets acccess is limited only to specific IP addresses
8. AWS S3: Ensure S3 buckets do not allow READ access to AWS authenticated users through ACLs
9. AWS S3: Ensure S3 buckers do not allow FULL_CONTROL access to AWS authenticated users via S3 ACLs
10. AWS S3: Ensure all S3 buckets have policy to require server-side and in transit encryption for all objects stored in bucket
11. AWS Networking: Ensure no security groups allow ingress from 0.0.0.0/0 to port 22
12. AWS Networking: Ensure Application Load Balancer (ALB) wth administrative service: SSH (TPC:22) is not exposed to the public internet
13. AWS Networking: Ensure no security groups allow ingress from 0.0.0.0/0 to port 22
14. AWS Networking: Ensure no security group allows ingress from 0.0.0.0/0 to port 3389 (RDP)
15. AWS - Audit and Logging: Ensure S3 bucket access logging is enable on the CloudTrail S3 bucket
16. AWS - Audit and Logging: Ensure CloudTrail is enabled in all regions
17. AWS - Audit and Logging: Ensure CloudTrail trails are integrated with CloudWatch logs
18. AWS - Audit and Logging: Ensure S3 bucket used to store CloudTrail logs is not publicly accessbile
19. AWS - Monitoring: Ensure a log metric filter and alarm exists for CloudTrail configurations changes

These configurations can be part of manual deployment documentation or, ideally, be party of the Infrastructure as Code (IaC) automation within DevOps pipelines. It would prevent these misconfiguration from getting into production in the first place.

a cloud security posture management solution like Cloudneeti could be used by Cloud Ops or DevOps team to continuosly validate their security posture in pre-production and production environments.

##### Auto-remediation

The next level of defense would be auto-remediation of misconfigured resrouces.\

##### Conclusion

Misconfiguration can cause catastrophic losses. Critical flaws that enabled such a devastating breach can. be avoided when organizations deploy tools to enforce continuous compliance with cloud security best practices.

### Lecture

------

#### Rainbow Tables

+ A precomputed table for catching the output of cryptographic hash functions, usually for cracking password hashes
  + Optimized, preetermined set of hashes
  + Much fater to query
  + Hashing methods determine table type
  + Don't work on "salted" hashes

#### Salting

+ **Salting** is a cryptographic technique that protects passwords against rainbow tables by adding random characters to the plaintext prior to hashing
  + Generates a totally different hash
  + Each user should have a unique salt value
  + Salt enerated by a cryptographically secure pseudo-random number generator

#### Dictionary Attacks

+ A dictionary attack is a kind of brute force attack that attempts to guess the password by using a wordlist, such as dictionary or list of common passwords

#### IAM: A High Level View

+ Identity and Access Management (IAM) according to ISC2:
  + 5.1 Control physical and logical access to assets
  + 5.2 Manage identification and authentication of people, devices, and services
  + 5.3 Integrate identify as a third-party service
  + 5.4 Implements and manage authorization mechanisms
    + PKI
    + RADIUS
  + 5.5 Manage the identity and access provisioning lifecycle 

#### AWS IAM

+ Why should we practise AWS IAM controls?
  + IAM users, roles and policies determine what user accounts are allowed to do
  + Administrator clearances are the primary targets of threat actors (privilege escalation)
+ Example: Capital One data breach
  + Metadata service had a server side request forgery (SSRF) vulnerability
  + IAM admin role a major part of this

#### AWS IAM

+ The AWS Identity and Acces Management (IAM) services handles authentication and authorization within your AWS account.
  + Authentication: Logging in as an identity to acess private resources
  + Authorization: What people and processes are allowed to do:
  + How?
    + Users, groups, roles and federated identities

#### AWS IAM Objects

+ IAM objects include
  + Users
  + Groups
  + Roles
  + Policies
    + ARN
    + Principal
    + Actions
    + Conditions

#### AWS IAM

+ Users: Usually a physical person
+ Groups: Functions (admins devops) Team (engineering, design...) Groups contains users.
+ Roles: Internal usage within AWS resource
+ Policies (JSON Documents): Defines what each of the above cn and cannot do

#### AWS IAM Users

+ In an AWS account, the root user can perform all operations.
  + Must be protected using complex passwords and MFA
  + Not ideal for long term use
  + IAM users with appropriate clearances should be used for most day to day activities
+ IAM users sign into the AWS Managemnt console using a special UR

#### AWS IAM GROUPS

+ An IAM user group is a collecction of IAM users.
  + Example:
    + Group called "Admins" with permissions that administrators need
  + Can contain many users, and a user can belong to multiple user groups
  + Can't be nested (no groups inside groups)
  + Can't be identified as a "Principal"

#### AWS IAM Roles

+ An IAM roles is a creatable object containing specific permissions
+ Unlike users, roles can be assumed by anyone who needs it
+ Example
  + Role access between production and development environments

#### AWS IAM Policies

+ An inline policy is a policy that's embedded in an IAM identity (a user, group, or role)
  + Policy is an inherent part of the identity
  + Create policy and embed into identity
+ An AWS managed policy is a standalone policy that is created and administered by AWS
  + Standalone policy means that the policy has its own Amazon Resource Name (ARN) that includes the policy name.

#### AWS IAM Policies

+ IAM policy objects are stored in JSON.
  + The `AllowViewAccountInfo` statement allows the user to view account-level information.
  + Note the elements of a policy
    + Sid
    + Effect
    + Action
    + Resource

#### Interacting with AWS

+ How can a user interact with a AWS?
  + The AWS Management Console provides a convenient visual web interface for most AWS interactions
  + The AWS Command Line Interface (CLI) is a unified tools to manage your AWS services.
    + Supports script execution