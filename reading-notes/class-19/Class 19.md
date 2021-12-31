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

### Lecture

------

#### Event-Driven Security

##### Learning Objectives

+ What is event-driven architecture?
+ How can we use events to automate incident response in the cloud?
+ What is serveless close?
+ How can I programmatically respond to changes in the cloud?
+ What should I use for threat detection in the cloud?
+ Do I have access to CTI to improve the quality of threat detection?  

#### Event-Driven Architecture

+ Even-Driven Architecture consists of decloupled systems that run in response to events.
  + Events trigger and communicate between separate services
  + Modern applications
    + Microservices
  + Three key components:
    + Event producers
    + Event routers
    + Event consumers

#### Serveless Code

+ AWS Lambda is a compute service that runs code without the need for provisioning or managing servers (serverless)
  + Code is executed on cloud compute infrastructure (no instances necesary)
  + Run Lambda functions in response to events
    + Example, state changes in a S3 bucket
    + Respond to security concerns automatically
    + Alternatively, deveopers can build serveless applications with Lambda
  + Security purposes
    + CloudTrail integration
    + CloudWatch Events integration

#### Canary in the Coal Mine

+ Origins of "Canary in the coal mine"
  + From 1911 to 1986, coal minters brought caged canaries (birds) into coal mines to detect toxic gases
  + Upon detectio, canary screeched (or died) and warned miners of danger
+ Why a canary?
  + A "sentinel species" more sensitive to carbon monoxide and toxic gas
+ "Canary in the coal mine" as a detection tecnique
  + Execute a Lambda function at a regular scheduled internval to check the state of a resource
  + Anomalies detected lead to CloudWatch alarms triggered

#### Threat Detection

+ Amazon GuardDuty is a continuous security monitoring service that analyzes and processes the following data sources:
  + VPC Flow Logs
  + AWS CloudTrail management event logs
  + Couldtrail S3 data event logs
  + DNS logs
+ Comes integrated with up-to-date threat intelligence feeds from
  + AWS
  + CrowdStrike
  + Proofpoint