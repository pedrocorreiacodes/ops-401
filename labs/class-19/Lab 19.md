## Lab 19

### Part 1: Create an AWS Lambda Function

------

#### In AWS Management Console, type “Lambda” into the search and access the Lambda service dashboard.

![Screenshot 2021-12-30 at 16.00.02](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.00.02.png)

#### Create an AWS Lambda function from a blueprint named “hello-world-python”

On the dashboard select **Create function**. Select **Use a blueprint** and search for `hello-world-python`. Select it and click **Configure**:

![Screenshot 2021-12-30 at 16.02.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.02.44.png)

![Screenshot 2021-12-30 at 16.05.21](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.05.21.png)

#### Before you can test your new Lambda function, you’ll need to create a test event if you don’t have an existing event to work with. Name it “testevent1” and save it.

Go to the **Test** tab, select **New event** choose the **hello-world** **Template** and click **Test** and **Save changes**:

![Screenshot 2021-12-30 at 16.08.54](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.08.54.png)

#### Run a test of your Lambda function, hello-world-python, using testevent1.

![Screenshot 2021-12-30 at 16.09.26](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.09.26.png)

#### Copy and paste the log output into your submission.

![Screenshot 2021-12-30 at 16.20.10](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.20.10.png)

#### Locate the corresponding CloudWatch log group and paste the ARN of this log group into your submission.

![Screenshot 2021-12-30 at 16.36.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.36.42.png)

![Screenshot 2021-12-30 at 16.37.18](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.37.18.png)

#### In CloudWatch, click the “Log Stream” within this log group. Keeping this open, execute your Lambda function again with a test. Refresh the log stream. What do you see?

Before executing:

![Screenshot 2021-12-30 at 16.48.59](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.48.59.png)

After executing:

We can see that a new entry to the log was added:

  ![Screenshot 2021-12-30 at 16.49.29](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.49.29.png)

### Part 2: Enable Amazon GuardDuty

------

#### Open the Amazon GuardDuty Management Console.

![Screenshot 2021-12-30 at 16.51.11](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.51.11.png)

Enable GuardDuty.

![Screenshot 2021-12-30 at 16.51.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.51.32.png)

#### In the Setting section, generate sample findings.

Simply go to **Smaple finding** and select **Generate sample findings**:

![Screenshot 2021-12-30 at 16.53.45](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.53.45.png)

#### Review the findings and find one that looks interesting to you. Select a high priority (red triangle) finding to analyze.

On the right side menu go to **Findings**:

![Screenshot 2021-12-30 at 16.54.38](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 16.54.38.png)

##### Identify the Finding ID value. In GuardDuty Findings, filter your view to that specific Finding ID and grab a screenshot.

![Screenshot 2021-12-30 at 17.07.58](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 17.07.58.png)

##### Download the raw JSON of this finding and paste it into a shareable GitHub gist. Link to the gist in your submission. Take a moment to analyze the JSON for useful details as to what may have occurred.

Go to **Actions** > **Export...** and click **Download**:

![Screenshot 2021-12-30 at 17.13.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 17.13.44.png)

Find GitHub gist **[HERE](https://gist.github.com/pedrocorreiacodes/fb1326ce38dc8ef577d36b2efcae11a1)**!

##### View the “Full description” and “Remediation recommendations” for this event and explain in your own words what took place, and how the company should remediate.

![Screenshot 2021-12-30 at 17.21.38](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 17.21.38.png)

An access from suspected malicious IP to a S3 bucket was detected. This API activity is commonly associated with exfiltration tactics. It's higly advisable to check S3 credentials and/or retrict permissions to the resource.

##### What resource is being targeted (being sample data it won’t necessarily exist on your cloud)?

S3 bucket `bucketName`.

##### What is the action type and source IP address?

+ Action type: AWS_API_CALL
+ IP address: 198.51.100.0

##### Review the networking information on this finding; what does this tell you about what happened?

An API call from IP address 198.51.100.0 was made targetting `arn:aws:s3:::bucketName`.

##### Is there a MITRE ATT&CK® TTP we could map this to?

ID: T1530 - Data from Cloud Storage Object

### Part 3: Log Analysis with AWS Security Hub

------

#### Open the AWS Security Hub Management Console.

![Screenshot 2021-12-30 at 17.44.59](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 17.44.59.png)

#### Enable Security Hub. Select CIS and AWS Foundational security standards.

![Screenshot 2021-12-30 at 17.46.50](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 17.46.50.png)

#### In the Security Standards menu, check account compliance.

![Screenshot 2021-12-30 at 17.48.37](/Users/baphomet/Desktop/cursed we/Screenshot 2021-12-30 at 17.48.37.png)

#### Confirm in Findings that the sample findings from GuardDuty were also reported in AWS Security Hub.

![Screenshot 2021-12-30 at 18.13.00](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.13.00.png)

##### What details were provided for these findings?

![Screenshot 2021-12-30 at 18.14.11](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.14.11.png)

#### Navigate the Insights page.

![Screenshot 2021-12-30 at 18.15.21](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.15.21.png)

##### What instance had the most findings?

![Screenshot 2021-12-30 at 18.16.19](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.16.19.png)

##### What security issues are there?

There seem to be none for the current insights.

##### What should the company address first and why?

All the **CRITIACAL** reported findings:

![Screenshot 2021-12-30 at 18.21.10](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.21.10.png)

### Part 4: Wrap Up

------

#### GuardDuty can be disabled from GuardDuty Console > Settings > Disable GuardDuty.

![Screenshot 2021-12-30 at 18.26.00](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.26.00.png)

Delete also the Lambda function:

![Screenshot 2021-12-30 at 18.31.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-19/Screenshot 2021-12-30 at 18.31.42.png)