## Challenge 40

### Part 1: Staging

------

This lab requires the class-40-45-kali.ova and class-40-target.ova imported into your local Virtualbox.

- Import class-40-45-kali.ova into your local Virtualbox Manager.
  - Assign system resources. Suggested values:
    - 4096MB RAM
    - 4 CPUs
    - 128MB Video Memory
    - Network: NAT Network

![Screenshot 2022-02-07 at 11.01.21](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.01.21.png)

- Import class-40-target.ova into your local Virtualbox Manager.
  - Assign system resources. Suggested values:
    - 1024MB RAM
    - 1 CPU
    - 12MB Video Memory

![Screenshot 2022-02-07 at 11.14.29](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.14.29.png)

+ Check that the Nessus service is running by accessing the terminal and entering `sudo systemctl status nessusd`

![Screenshot 2022-02-07 at 11.16.40](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.16.40.png)

- Access the Nessus web portal by following the shortcut “Nessus” in the “class-40” directory.

![Screenshot 2022-02-07 at 11.17.14](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.17.14.png)

- Obtain an activation code for Nessus Essentials. Activate your copy of Nessus and note the credentials for future reference.

![Screenshot 2022-02-07 at 11.13.16](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.13.16.png)

![Screenshot 2022-02-07 at 11.24.19](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.24.19.png)

- Now that you have Nessus working on a stable baseline copy of class-40-45-kali.ova, this is probably a good time to take a VM snapshot with Virtualbox in case anything goes wrong later.

![Screenshot 2022-02-07 at 11.18.19](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.18.19.png)

### Part 2: Scanning the Target

------

#### Basic Network Scan

Perform a basic network scan to identify your target IP.

- What does the basic network scan do?
- What is the IP address of your target system (class-40-target.ova)?

![Screenshot 2022-02-07 at 11.38.19](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.38.19.png)

![Screenshot 2022-02-07 at 11.41.33](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.41.33.png)

Select it and click **Launch** on the right:

![Screenshot 2022-02-07 at 11.43.02](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.43.02.png)

![Screenshot 2022-02-07 at 11.51.48](/Users/baphomet/Desktop/Screenshot 2022-02-07 at 11.51.48.png)

IP address of the machine 10.0.2.2.

#### Using Policies

Nessus has a feature called “policies,” which are essentially scan templates you can configure in advance then select from to speed up your work. For each of these scans include screenshots of the scan results.

- Create a new policy named “Host Discovery Policy.”

![Screenshot 2022-02-07 at 11.58.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.58.32.png)

![Screenshot 2022-02-07 at 11.59.03](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 11.59.03.png)

- Configure the policy to perform a host enumeration scan of the targeted network.

![Screenshot 2022-02-07 at 12.01.20](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.01.20.png)

+ Create and execute a new scan that uses this policy.

![Screenshot 2022-02-07 at 12.12.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.12.49.png)

![Screenshot 2022-02-07 at 12.17.16](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.17.16.png)

Create two additional policies and execute new scans for each one:

- OS identification policy

When creating the Policy go to **Settings** -> **Discovery** -> **Scan Type** and select **OS Identification**:

![Screenshot 2022-02-07 at 12.18.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.18.42.png)

![Screenshot 2022-02-07 at 12.48.30](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.48.30.png)

- Port scan policy (common ports)

![Screenshot 2022-02-07 at 12.49.35](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.49.35.png)

![Screenshot 2022-02-07 at 12.53.47](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 12.53.47.png)

#### Answer the following questions:

- How successful were your new scan policies?
  - The scans were successful
- Do you think the results were accurate?
  - Yes fairly accurate.
- What tool does this remind you of, that we’ve used in class before?
  - Nmap/Zenmap

#### Web Application Vulnerability Scan

Nessus is quite versatile in that it can be a web application vulnerability scanner as well as a general network or system vulnerabilities scanner. In this part of the lab you will perform a web application vulnerability scan.

- Scan today’s target system, class-40-target.ova.

  ![Screenshot 2022-02-07 at 13.01.38](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 13.01.38.png)

+ Identify the highest severity vulnerability and explain how it works in your own words.

![Screenshot 2022-02-07 at 13.03.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 13.03.48.png)

![Screenshot 2022-02-07 at 13.05.01](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 13.05.01.png)

The scan shows a high severity vulnerability. The app is vulnerable to a sql injection attack.

+ What other vulnerabilities may exist on the target system’s web app?

  ![Screenshot 2022-02-07 at 13.16.51](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-40/Screenshot 2022-02-07 at 13.16.51.png)

+ Generate an executive summary PDF report from Nessus and upload it to your Google Docs. Include a link to it in your submission doc.

Click on **Report** select your format and template and then **Generate Report**:

![Screenshot 2022-02-07 at 13.18.04](/Users/baphomet/Desktop/Screenshot 2022-02-07 at 13.18.04.png)

Click HERE for the report.