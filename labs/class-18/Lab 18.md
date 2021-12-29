## Lab 18

### Part 1: Create a Trail with AWS CloudTrail

------

#### Access AWS CloudTrail by typing “cloudtrail” into the AWS Management Console search box.

![Screenshot 2021-12-29 at 18.43.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2018.43.17.png)

#### Using Quick trail create, create a trail for logging management events.

Select **Create a trail**, name your trail and select **Create trail** to finish:

![Screenshot 2021-12-29 at 18.45.34](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2018.45.34.png)

#### Access the trail object and note its state of “Logging”; you can start/stop logging from this screen.

![Screenshot 2021-12-29 at 18.46.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2018.46.23.png)

#### In CloudTrail console, access event history. Note that CloudTrail records the last 90 days of events for free. Change the time window to something more reasonable like 30m or 1h, then download both a JSON and a CSV of the events to your computer. Take a look at both; which is more useful for post-incident analysis?

![Screenshot 2021-12-29 at 18.49.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2018.49.15.png)

![Screenshot 2021-12-29 at 18.57.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2018.57.23.png)

![Screenshot 2021-12-29 at 19.01.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.01.57.png)

Both formats serve different purposes for different tooling. For immediate human readable format I would go with `.csv`.

#### Open the S3 bucket that’s capturing your management logs from Cloudtrail. Drill down into the folders until you can see the logs as .GZ compressed archives. Grab a screenshot of this. It’s always good to know where you’re saving logs.

Search for **S3** in AWS Management Console search box. Select the bucket created by cloudtrail:

![Screenshot 2021-12-29 at 19.07.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.07.20.png)

![Screenshot 2021-12-29 at 19.07.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.07.36.png)

![Screenshot 2021-12-29 at 19.08.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-18/Screenshot 2021-12-29 at 19.08.08.png)

![Screenshot 2021-12-29 at 19.08.21](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-18/Screenshot 2021-12-29 at 19.08.21.png)

![Screenshot 2021-12-29 at 19.08.38](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-18/Screenshot 2021-12-29 at 19.08.38.png)

### Part 2: Ingest a Trail with Amazon CloudWatch

------

#### We’ll need to configure Amazon CloudWatch to ingest log data from CloudTrail, specifically the new Trail you created. Access [this helpful blog](https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/) and complete the sections, “Create a trail in the CloudTrail console” and “Analyzing CloudTrail logs in CloudWatch”. You don’t need to create a new trail, just use the trail you already have.

![Screenshot 2021-12-29 at 19.20.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.20.49.png)

![Screenshot 2021-12-29 at 19.22.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.22.11.png)

### Part 3: Create a CloudWatch Rule

------

#### Open the CloudWatch console.

![Screenshot 2021-12-29 at 19.23.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.23.17.png)

#### In the navigation pane, choose Events, Create rule.

![Screenshot 2021-12-29 at 19.24.40](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.24.40.png)

#### Choose Event Pattern... and all of the objectives after.

![Screenshot 2021-12-29 at 19.31.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-18/Screenshot 2021-12-29 at 19.31.32.png)

![Screenshot 2021-12-29 at 19.32.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.32.43.png)

### Part 4: Create a VPC Flow Log

------

#### Under Services > Networking & Content Delivery > VPC > Your VPCs, select your VPC > Flow Logs tab.

![Screenshot 2021-12-29 at 19.35.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.35.23.png)

#### Create a flow log using `security-book-peering` as the trail name. Select the filter type and maximum aggregation interval.

#### Send the flow logs to an S3 bucket by typing `arn:aws:s3:::<YOUR BUCKET NAME>` in the S3 bucket ARN field.

![Screenshot 2021-12-29 at 19.42.08](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.42.08.png)

#### Test and validate IP traffic is being captured using a flow log.

![Screenshot 2021-12-29 at 19.44.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.44.10.png)

### Part 5: Wrap Up

------

Delete and disable anything you don’t need at this point, to keep charges down. Pay attention to S3 buckets in particular.

![Screenshot 2021-12-29 at 19.49.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-18/Screenshot%202021-12-29%20at%2019.49.32.png)

![Screenshot 2021-12-29 at 19.50.38](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-18/Screenshot 2021-12-29 at 19.50.38.png)
