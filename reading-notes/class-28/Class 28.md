## Class 28

### Reading: Ethical hacking: Log tampering 101

------

Gettign caught is exactly what every hacker does not want. Logs are designed to record nearly everythign that occurs in a system, including hacking attempts, and can be determinative factor in catching hackers.

Ethical hackers need to understand how hackers tamper with logs, as it is a common practice with hackers.

Basics of log tampering:

+ Disabling auditing
+ Clearing logs
+ Modifying logs
+ Erasing command history

#### The process

There is a four step process to covering our tracks by tamping with logs that hackers know like the back of their hand:

1. Disable auditing

   Disable auditing is a smart first step for hackers because if logging is turnef off, there will be no trail of evidence.

   In Windows systems, hackers can use the command line favourite, Adufitpol, which will not only allow the hacker to disable auditing but will also allow the hacker to see the level of logging that the organization's system has set.

2. Clearing logs

   ​	Since logs preserve the evidence trail of hacking activitives, clearing logs is the logical next step for ethical hackers to know about

   + How to clear logs in Windows 

     + One way is to use the `clearlogs.exe`file. Once access to the target Windows system is obtained, the file need to be installed and then run to clear the security logs. To run the file, enter: `clearlogs.exe -sec`. This will clear security logs on the target system.

     + If the hacker does not remove `clearlogs.exe`, it will serve as hard evidence of log tampering.

     + Meterpreter - This advanced paylod is a type of shell that will help to clear all logs in a Windows system in newer versions of Meterpreter. Atfter compromising the system with Metasploit, use a Meterpreter command prompt and enter the following command:

       `Meterpreter > clearev`

       This will present the ehtical hacker with a windows stating that all of the security, application and system logs have been cleared.

     + Windows Even Viewer - Even if auditing has been disable, it is still smart to clear logs in Windows Event Viewer becaue actions like disabling auditing will display as an event. Navigate to Event Viewer under Windows Logs in the folder tree. In the left hand pane, right-click on the type of logs you want to clear and select Clear All Events.

   + Linux systems

     + Linux systems have their own process of log clearing. To perform this, you want to use the Shred tool. To shred and erase the log file on the target system, run:

       `Shred -vfzu auth.log`

3. Modifying logs

   Knowing is half the battle, and knowing where the logs are in your target system is crucial for any hacker.

4. Deleting Commands

   The thing with bash is that it retains the history of entered bash command, so unless you clear it, the administrator will be able to see that the Shred command above was entered. The retained history of bash commands is found in the file `~/.bash_history`.

Log tampering is common practice in hacking because hackers will allways want to cover their tracks from the prying eyes of an organizations administrator. It's important for an organization to understand how malicious hackers will operate in practice, so if a hacking breach is detected, log file tampering may be one of their first actions in your systems.

Organization should centrally store their system logs as much as possible to help confound malicious hackers, preferably with a SIEM solution.