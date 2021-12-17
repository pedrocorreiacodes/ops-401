## Lab 13

### Part 1: Staging

------

#### Download and extract the JSON file from github aws collection `ec2_proxy_s3_exfiltration.zip`

![Screenshot 2021-12-17 at 16.17.28](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2016.17.28.png)

#### ![Screenshot 2021-12-17 at 16.17.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2016.17.48.png)

#### Create `index="mordor-aws"` in Splunk

#### Add the JSON file to Splunk data inputs and the Mordor index

#### ![Screenshot 2021-12-17 at 16.32.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2016.32.01.png)

![Screenshot 2021-12-17 at 16.34.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2016.34.44.png)

![Screenshot 2021-12-17 at 16.41.16](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2016.41.16.png)

### Part 2: Log Analysis

------

#### The data set you’ll be analyzing today is now imported into Splunk as the index name of mordor-aws. Access the full index using index="mordor-aws" and paste the first log you see into your submission.

![Screenshot 2021-12-17 at 17.27.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2017.27.23.png)

#### Open the JSON file in VS Code. Compare it to the same data set in Splunk. What do you observe?

![Screenshot 2021-12-17 at 18.24.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2018.24.50.png)

The same data formated in a different way.

#### How is the attacker accessing the company’s AWS systems? Check the `userAgent` and `eventType` attributes.

The adversary is trying to access the company's AWS system through API calls to a EC2 instance:

![Screenshot 2021-12-17 at 18.31.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2018.31.38.png)

#### Find evidence that the following tactics were utilized, and paste the logs into your submission:

##### TA0001

Initial Acess. The adversary is trying to get into the Network

![Screenshot 2021-12-17 at 19.01.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2019.01.52.png)

First access filtered with `reverse`.

##### TA0003

Persistence. The threat actor is trying to maintain their foothold:

We can see this **eventName** **Assume Role**, according to the AWS docs *Returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to.*

![Screenshot 2021-12-17 at 19.34.28](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2019.34.28.png)

##### TA0004

Privilege Escalation

Threat actor is trying to gain higher-level permissions. Trying to get all the key pairs of the user.

![Screenshot 2021-12-17 at 19.42.35](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2019.42.35.png)

##### TA0005

The adversary is trying to avoid being detected. **DescribeAlarms** tetrieves the specified alarms. You can filter the results by specifying a prefix for the alarm name, the alarm state, or a prefix for any action

![Screenshot 2021-12-17 at 19.52.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2019.52.59.png)

##### TA0009

Collection where the adversary is trying to gather data of interest to their goal.

![Screenshot 2021-12-17 at 20.00.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2020.00.26.png)

The `GetObject` retrieves objects from Amazon S3. The goal of the threat actor.

#### Find evidence that the following techniques were utilized, and paste the logs into your submission (may overlap with previous findings in “tactics” section):

##### T1078.004

Valid Accounts: Cloud Accounts.

Adversaries may obtain and abuse credentials of a cloud account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion.

![Screenshot 2021-12-17 at 20.04.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2020.04.00.png)

##### T1530

Data from Cloud Storage Object. Adversaries may access data objects from improperly secured cloud storage.

![Screenshot 2021-12-17 at 20.06.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2020.06.00.png)

### Part 3: Reporting

------

### Summarize in your own words how the attacker was able to exfiltrate data from the S3 bucket. Be sure to include:

#### When did the attack take place?

The attack took place September 14th of 2020 from 00:44:23 to 00:45:36

#### How was the attacker interacting with AWS?

 Using Botocore package, AWS-CLI.

#### Did you find any information about the attacker/attack origin?

Source IPadress: 1.2.3.4

![Screenshot 2021-12-17 at 20.18.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-13/Screenshot%202021-12-17%20at%2020.18.56.png)
