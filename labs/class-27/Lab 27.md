## Lab 27

### Part 1: Staging

------

#### Start PowerShell Empire

Run `sudo powershell-empire`on the terminal:

![Screenshot 2022-01-05 at 17.48.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 17.48.48.png)

### Part 2: Setup a Listener

------

To add a listener use the command `uselistener [protocol]`we went with `http`;

![Screenshot 2022-01-05 at 17.54.39](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 17.54.39.png)

Set up a port with `set Port 80`:

![Screenshot 2022-01-05 at 18.04.05](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.04.05.png)

Start listener with the command `execute`:

![Screenshot 2022-01-05 at 18.04.58](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.04.58.png)

### Part 3: Setup a Stager

------

First let's disable Windows Defender on the Windows10 machine:

![Screenshot 2022-01-05 at 18.07.31](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.07.31.png)

Setup a stager for use with `usestager [stager]`:

![Screenshot 2022-01-05 at 18.13.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.13.08.png)

![Screenshot 2022-01-05 at 18.14.37](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.14.37.png)

Set it to our listener (http):

![Screenshot 2022-01-05 at 18.17.11](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.17.11.png)

![Screenshot 2022-01-05 at 18.17.29](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.17.29.png)

Use the command `execute`to output the malicious file:

![Screenshot 2022-01-05 at 18.20.59](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.20.59.png)

Let's check our file and send it to the Windows10 machine:

![Screenshot 2022-01-05 at 18.22.27](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.22.27.png)

If you have this error, click **...** and **Keep anyway**:

![Screenshot 2022-01-05 at 18.37.07](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.37.07.png)

Anti-virus might sound the alarm as well, click the alarm and **Allow on device**:

![Screenshot 2022-01-05 at 18.38.13](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.38.13.png)

![Screenshot 2022-01-05 at 18.39.19](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.39.19.png)

![Screenshot 2022-01-05 at 18.39.37](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.39.37.png)

Now we can click it and open it:

![Screenshot 2022-01-05 at 18.41.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.41.32.png)

It's seems that we have to bypass another alarm, **Run anyway**:

![Screenshot 2022-01-05 at 18.42.28](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.42.28.png)

One more step to go, let's disable **Real Time Protection** on **Virus and Threat Settings**:

![Screenshot 2022-01-05 at 18.48.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.48.44.png)

![Screenshot 2022-01-05 at 18.49.17](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.49.17.png)

Now as soon as we execute the malicious file on the Windows 10 machine we get this on the Kali machine:

![Screenshot 2022-01-05 at 18.50.47](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.50.47.png)

![Screenshot 2022-01-05 at 18.51.19](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.51.19.png)

Renaming agent to `class27`:

![Screenshot 2022-01-05 at 18.53.05](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.53.05.png)

Using the command `interact` to connect to the shell:

![Screenshot 2022-01-05 at 18.54.31](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.54.31.png)

Sending commands to the remote machine:

![Screenshot 2022-01-05 at 18.55.27](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-27/Screenshot 2022-01-05 at 18.55.27.png)

### Part 4: Reporting:

------

#### Why would an APT want to establish persistence on the Cyberdyne network?

Persistance is a goal for threat actors to comeback to the system at anytime.

#### What kind of threat actor are we dealing with here?

Possibly a state sponsored APT. Empire (or similar) is a choice of these threat actors because they can stay for a long time in the affected system without being discovered.

#### Based on your reproduction, how could the batch file payload have been transmitted to the victim and executed the first time?

Phishing and social engineering comes into play. Maybe through some email attachment or in our case using a web service like WeTransfer.

#### Reboot the Windows 10 VM. Is the agent still responding to Empire? Explore the limitations of such a technique.

The agent is no longer responding to Empire. A new malicious file has to be clicked again in order to restore the connection. Another kind of backdoor needs to be deployed for extended persistence.

#### Is there a way to configure the batch file to not delete itself after executing? Explain.

By setting the **delete** option to **false**.

#### Evaluate technique T1037. As the threat actor, what kind of synergy does this technique offer alongside T1059.003?

To retain access to system even if it is rebooted some kind of script has to run at startup.

#### At a high level, brainstorm what we could potentially do as defenders to protect Cyberdyne against this type of threat. Explore the various types of security controls:

##### Preventative

Windows-defender. Firewalls in general. All updated.

##### Detective

Using and IDS, like Snort.

##### Corrective

Back up data and clean the hard drive.