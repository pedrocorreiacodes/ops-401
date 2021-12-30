## Class 19

### Reading: What is Amazon GuardDuty?

------

**Amazon GuardDuty is a continuous security monitoring service** that analyzes and processes the following Data sources:

+ VPC Flow Logs
+ AWS CloudTrail management event logs
+ CloudTrail S3 data event logs
+ DNS logs

It uses threat intelligence feeds, such as lists of malicious IP addresses and domains, and machine learning to idenitfy unexpected and potentially unauthorized and malicious activity within your AWS environment. This can include issues like:

+ Escalation of privileges
+ Uses of exposed credentials
+ Communication with malicious IP addresses, or domains

GuardDuty can detect compromised EC2 instances serving malware or mining bitcoin. It also monitors AWS acount access behavior for signs of compromise, such as unauthorised infrastructure deployments, like instances deployed in a Region that has never been used, or unusual API calls, like a password policy change to reduce password strength

GuardDuty informs you of the status of your AWS environment by producing security findings that you can view in the GuarDuty console or though Amazon CloudWatch events.

