## Lab 04

### Part 1: Staging

------

#### Enable AWS Config.

In **Services** search **AWS Config**. Click **1-click setup**.

![Screenshot 2021-11-30 at 10.49.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2010.49.53.png)

![Screenshot 2021-11-30 at 10.50.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2010.50.36.png)

#### Enable AWS Security Hub. Allow two hours for it to setup before use.

In **Services** search **AWS Security Hub** and **Enable Security Hub**.

![Screenshot 2021-11-30 at 10.52.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2010.52.38.png)

![Screenshot 2021-11-30 at 10.55.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2010.55.10.png)

![Screenshot 2021-11-30 at 10.57.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2010.57.13.png)

### Part 2: Manual EC2 instance hardening with CIS

------

#### In the free tier of EC2, launch a new instance of Windows Server 2019.

![Screenshot 2021-11-30 at 16.02.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.02.54.png)

![Screenshot 2021-11-30 at 16.03.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.03.21.png)

![Screenshot 2021-11-30 at 16.06.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.06.10.png)

![Screenshot 2021-11-30 at 16.06.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.06.52.png)

#### Establish remote connectivity to your new instance via RDP.

Go to **Connect to instance** and **Download remote desktop file** to open with the RDP client:

![Screenshot 2021-11-30 at 16.09.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.09.44.png)

![Screenshot 2021-11-30 at 16.09.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.10.32.png)

![Screenshot 2021-11-30 at 16.34.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2016.34.01.png)

![Screenshot 2021-11-30 at 17.02.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.02.09.png)

#### Select the following six benchmarks from your AMI’s benchmark document in the CIS benchmark list and reconfigure your Windows Server instance, using the GUI via RDP, to achieve the standard indicated.

##### 1.1.5 (L1)

![Screenshot 2021-11-30 at 17.07.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.07.33.png)

To enable the policy via Group Policy Editor set the followng UI path to `Enabled`:

`Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Password must meet complexity requirements`

And here is the configuration on our Windows Server:

![Screenshot 2021-11-30 at 17.11.31](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.11.31.png)

##### 1.1.6 (L1)

![Screenshot 2021-11-30 at 17.13.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.13.23.png)

To establish the recommended configuration via GP, set the following UI path to `Disabled`:

`Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Store passwords using reversible encryption`

The configuration on Windows Server:

![Screenshot 2021-11-30 at 17.18.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.18.21.png)

##### 1.2.1 (L1)

![Screenshot 2021-11-30 at 17.20.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.20.11.png)

To establish the recommended configuration via GP, set the following UP path to 15 or more minute(s):

`Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Account Lockout Policy\Account lockout duration`

On the Windows Server (this Policy has to be implemented after the next one, otherwise it will not work):

![Screenshot 2021-11-30 at 17.27.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.27.37.png)

##### 1.2.2 (L1)

![Screenshot 2021-11-30 at 17.25.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.25.26.png)

To establish the recommended configuration via GP, set the following UI path to 10 or fewer invalid login attempt(s), but not 0:

`Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Account Lockout Policy\Account lockout threshold`

On the Windows Server machine:

![Screenshot 2021-11-30 at 17.23.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.23.49.png)

##### 18.3.2 (L1)

![Screenshot 2021-11-30 at 17.33.08](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.33.08.png)

To establish the recommended configuration via GP, set the following UI path to Enabled: Disable driver (recommended):

`Computer Configuration\Policies\Administrative Templates\MS Security Guide\Configure SMB v1 client driver`

##### Export the AMI for use later. Include a screenshot of your saved AMI.

On **EC2 > Instances** select the instance, click on **Actions > Image and templastes > Create image**:

![Screenshot 2021-11-30 at 17.44.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.44.37.png)

Name it and click on **Create image**:

![Screenshot 2021-11-30 at 17.45.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.45.59.png)

![Screenshot 2021-11-30 at 17.46.35](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2017.46.35.png)

![Screenshot 2021-11-30 at 18.15.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.15.32.png)

#### Write a PowerShell script that automates the configuration of the required settings:

Find script in the same folder as this document.

And the script running on Windows Server:

![Screenshot 2021-11-30 at 18.34.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.34.18.png)

### Part 4: Pre-hardened EC2 instance deployment

Deploy a pre-hardened AMI in AWS EC2. Ideally selected the hardened version of the OS you just worked on.

On **Launch Instance** search for **cis windows server**:

![Screenshot 2021-11-30 at 18.38.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.38.09.png)

![Screenshot 2021-11-30 at 18.39.03](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.39.03.png)

##### Access the CIS standards and verify the six benchmarks are achieved on the hardened instance:

#### **1.1.5 (L1)**

![Screenshot 2021-11-30 at 18.57.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.57.56.png)

#### **1.1.6 (L1)**

![Screenshot 2021-11-30 at 18.58.47](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.58.47.png)

#### **1.2.1 (L1)**

![Screenshot 2021-11-30 at 18.59.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.59.20.png)

#### **1.2.2 (L1)**

![Screenshot 2021-11-30 at 18.59.46](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2018.59.46.png)

### Part 5: Scanning for CIS Benchmarks

------

#### Turn on your normal AMI. Both AMIs should be running.

![Screenshot 2021-11-30 at 19.02.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.02.58.png)

#### Run or await an automated CIS scan.

Go to **Security Hub > Security Standards > CIS AWS Foundations Benchmark v1.2.0**:

![Screenshot 2021-11-30 at 19.05.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.05.13.png)

 ![Screenshot 2021-11-30 at 19.07.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.07.44.png)

#### Assess your findings. Make one change that improves the result of your CIS scan.

![Screenshot 2021-11-30 at 19.21.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.21.58.png)

![Screenshot 2021-11-30 at 19.28.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.28.57.png)

![Screenshot 2021-11-30 at 19.29.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.29.33.png)

![Screenshot 2021-11-30 at 19.34.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-04/Screenshot%202021-11-30%20at%2019.34.45.png)
