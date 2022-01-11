## Lab 28

### Part 1: Staging

------

Note that the Windows 10 Pro endpoint is not joined into the CORP domain, so let's do that first:

![Screenshot 2022-01-10 at 13.01.14](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2013.01.14.png)

![Screenshot 2022-01-10 at 13.05.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2013.05.00.png)

Also it seems that this VM doesn't have Splunk's universal forwarder installed. Go **[HERE](https://www.splunk.com/en_us/download/universal-forwarder.html)** and download the Universal Forwarder for Win10:

![Screenshot 2022-01-10 at 14.16.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2014.16.49.png)

When it gets downloaded open it and start the installation process and accept the license agreement then go to **customize options**:

![Screenshot 2022-01-10 at 14.18.22](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2014.18.22.png)

Click, **Next** and **Next**. Select **Local System**. Configure like this:

![Screenshot 2022-01-10 at 14.19.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2014.19.54.png)

Now configure the **Receiver Indexer** with the IP address of the SIEM VM.

![Screenshot 2022-01-10 at 15.21.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2015.21.21.png)

After the installation has finished you can check configurations at **Program Files > SplunkUniversalForwarder > etc > system > local** and open `ouputs.conf`:

![Screenshot 2022-01-10 at 15.29.34](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2015.29.34.png)

And we're receiving logs in our SIEM:

![Screenshot 2022-01-10 at 15.47.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2015.47.18.png)

### Part 2: Log Clearing

------

#### Execute both of the following Atomic Tests as documented in the Atomic Red Team repo, entry T1070.001:

##### Atomic Test #1 - Clear Logs

Logs before executing the command:

![Screenshot 2022-01-10 at 17.17.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2017.17.51.png)

![Screenshot 2022-01-10 at 17.35.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2017.35.01.png)

After cleaning the **Security** logs, note the log concerning the deletion:

![Screenshot 2022-01-10 at 17.34.04](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2017.34.04.png)

##### Check whether this impacted the logs stored on your SIEM.

Logs are still stored on the SIEM, and we can check the log of the deletion:

![Screenshot 2022-01-10 at 17.41.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2017.41.33.png)

##### Atomic Test #2 - Delete System Logs Using Clear-EventLog

Before running the script:

![Screenshot 2022-01-10 at 17.51.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2017.51.49.png)

Running the script:

![Screenshot 2022-01-10 at 18.21.14](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2018.21.14.png)

They're gone:

![Screenshot 2022-01-10 at 18.22.06](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2018.22.06.png)

We can see on the SIEM that the clearing of the logs is logged and we still have the previous log entries:

![Screenshot 2022-01-10 at 18.24.08](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2018.24.08.png)

#### What are the conditions or requirements needed in order for the attacker to perform this kind of activity on the system?

The attacker must have root privileges and access to the endpoints. Either in person or through RCE.

#### Document the steps you took and your findings.

##### Verify that your log clearing operation was successful in Win10.

All verified and documented above.

##### Check whether this impacted the logs stored on your SIEM.

It didn't. All verified and documented above.

#### Analyze the event log(s) generated by your test.

##### What type of event log is this, Sysmon or regular Windows?

The event logs reported above came from **WinEventLog**.

##### What is the nature of this event log (what category does it fall into)?

They fall into the **Log clear** category:

![Screenshot 2022-01-10 at 18.35.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2018.35.02.png)

How does the event log indicate the user account that executed the log clearing operation?

![Screenshot 2022-01-10 at 18.41.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2018.41.20.png)

##### Take a look at Atomic Test #3 - Clear Event Logs via VBA and explain how this test works. Why does it require MS Word, and what about MS Word does it exploit?

This test uses the Visual Basic for Applications. VBA macros are a form of malware where VBA is used to automate functions, allowing programs like Word and Excel to execute code. In the case of this particular test, code to clear event logs via Microsoft Word.

### Part 3: Detection

------

#### For both Atomic Tests 1 and 2, create and test an alert that can detect log clearing behavior on a Windows 10 endpoint that is forwarding logs to Splunk.

To create a test go to the **Alerts** tab in splunk. You can follow **[THIS](https://docs.splunk.com/Documentation/Splunk/latest/Alert/Alertexamples)** example to create an alert based on the **Log clear** category. My current version of splunk does not support this feature.

![Screenshot 2022-01-10 at 19.14.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-28/Screenshot%202022-01-10%20at%2019.14.05.png)
