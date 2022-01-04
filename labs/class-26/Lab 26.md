## Lab 26

### Part 1: Staging

------

![Screenshot 2022-01-04 at 12.58.50](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 12.58.50.png)

![Screenshot 2022-01-04 at 13.20.39](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 13.20.39.png)

### Part 2: Analysis of a Sample Data Set

------

#### **In this part of the lab, we will investigate the data set by consulting the PsExec Artifacts Reference as a guide for obtaining critical information from our sample data set. Get ready to practice your SPL querying skills as we comb through a sizeable data set.**

##### In Windows Server VM, access Splunk at http://10.0.0.5:8000/en-US/app/launcher/home and login with spunkadmin/splunkadmin.

Note that to access Splunk you must go to **http://10.0.0.54:8000**:

![Screenshot 2022-01-04 at 15.02.16](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 15.02.16.png)

##### Perform the search `index="class-26"` to view today’s sample data set that has been imported from Mordor Data Sets.

I you're getting this error:

![Screenshot 2022-01-04 at 15.07.25](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 15.07.25.png)

It means that the Splunk license expired or you have exceeded your license limit too many times.
To change that option go to `Setting --> Licensing - > change license group `and choose **Free license**, restart Splunk.

![Screenshot 2022-01-04 at 15.09.06](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 15.09.06.png)

![Screenshot 2022-01-04 at 15.13.54](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 15.13.54.png)

##### Identify the three event logs where a network connection was established using powershell.exe

###### Include a screenshot of Splunk indicating the SPL query you used to exclusively display these three logs according to the stated attributes

![Screenshot 2022-01-04 at 16.01.21](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 16.01.21.png)

![Screenshot 2022-01-04 at 16.07.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 16.07.23.png)

##### What port was used throughout the attack?

Port 64545.

##### What is the domain prefix and account name that invoked PsExec (e.g. RIVENDELL\Elessar)?

**THESHIRE** (Oh those Hobbits...)

![Screenshot 2022-01-04 at 16.13.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 16.13.08.png)

- ##### When did this invocation take place?

  ![Screenshot 2022-01-04 at 16.21.40](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 16.21.40.png)

- ##### What is the location of the executable that this process used?

![Screenshot 2022-01-04 at 16.30.34](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 16.30.34.png)

#### What TTPs were used in this attack?

Command and Scripting Interpreter - Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of [Unix Shell](https://attack.mitre.org/techniques/T1059/004) while Windows installations include the [Windows Command Shell](https://attack.mitre.org/techniques/T1059/003) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).

**T1059.001 PowerShell** - "Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system. Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include the Start-Process cmdlet which can be used to run an executable and the Invoke-Command cmdlet which runs a command locally or on a remote computer (though administrator permissions are required to use PowerShell to connect to remote systems)."

#### What part of the kill chain is this?

Execution. ID: TA0002

Lateral Movement. ID: TA0008

### Part 3: Simulation of this

------

#### In Windows Server VM, access Splunk at http://10.0.0.5:8000/en-US/app/launcher/home

Note that in this case we access Splunk on **http://10.0.0.54:8000**:

![Screenshot 2022-01-04 at 17.15.55](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 17.15.55.png)

#### Check that regular event logs are being correctly forwarded from Win10 by querying host="DESKTOP-62LU9FS".

![Screenshot 2022-01-04 at 17.16.57](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 17.16.57.png)

#### Check that Sysmon logs are being correctly forwarded from Win10 by querying `source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"`.

![Screenshot 2022-01-04 at 17.27.25](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 17.27.25.png)

#### From Windows Server, access `C:\Users\Administrator\Desktop\ops-cyber-401\Invoke-PsExec.ps1` using PowerShell IDE running as Administrator.

![Screenshot 2022-01-04 at 17.30.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 17.30.49.png)

#### Execute this script a few times.

![Screenshot 2022-01-04 at 17.31.59](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 17.31.59.png)

#### Review your event logs and Sysmon logs. Did this activity generate new logs? Include a screenshot of them.

![Screenshot 2022-01-04 at 18.38.52](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-26/Screenshot 2022-01-04 at 18.38.52.png)

No data, I suspect the Windows 10 endpoint provided does not correspond to this particular objective. It's not joined to the CORP domain nor forwarding logs to the SIEM. I need to work on that in the future.

#### Create a Splunk alert to detect this RCE technique. The alert should trigger an email to send to you whenever the alert is triggered. Include in your submissions details on how you configured the alert.

Complete guide **[HERE](https://docs.splunk.com/Documentation/Splunk/8.1.3/Alert/Emailnotification)**.

### Part 4: Reporting

------

#### Explain:

#### Summarize what you’ve done and learned today. What are your key takeaways?

I learned about RCE threats, how to detect them using Splunk and create alerts based on certain events.

#### How do Sysmon logs differ from regular event logs?

Which type was more useful in this scenario?

Sysmon logs look more detailed than event logs.

#### How can a Windows system be vulnerable to RCE?

Living-Off-the-Land Attacks provide the threat actor tools that are already in the environment they try to exploit. That's the case of Powershell. All computers that are in a network are susceptible to these kind of attacks. 

#### Referencing MITRE ATT&CK, what are some other tools and techniques besides Invoke-PsExec that can be used to perform RCE?

Tecniques in ID: T1059 - Command and Scripting Interpreter

What are some countermeasures against RCE?

Constant network monitoring, strong firewall configurations, strict permission for executing scripts.