## Lab 42

### Part 1: Staging

------

You will need two target systems for this exercise.

- class-42-target1-win7.ova (credentials are labuser/labuser)
- class-42-target2-win7.ova (credentials are labuser/labuser)

![Screenshot 2022-02-11 at 17.50.17](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 17.50.17.png)

### Part 2: Someone Pass the Hash

------

Follow the [Pass the Hash Tutorial](https://cqureacademy.com/blog/identity-theft-protection/pass-hash-attack-tutorial) to achieve an administrator shell from target1 to target2.

- Dump the hashes of local user accounts and identify the hash of the secret NT Administrator user.

The first thing here is to elevate to the Local System as we have to get access to the secret hives in the registry.  *psexec.exe -s -i -d cmd.exe.* (Download the sysinternals ->  https://download.sysinternals.com/files/PSTools.zip)

![Screenshot 2022-02-11 at 18.40.50](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 18.40.50.png)

![Screenshot 2022-02-11 at 18.41.31](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 18.41.31.png)

The next stage is to go to the tools folder and I will use CQHashDumpV2. I will use option /samdump. This allows me to perform the live hash dump.

![Screenshot 2022-02-11 at 18.50.05](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 18.50.05.png)

`Administrator:500:aad3b435b51404eeaad3b435b51404ee:10eca58175d4228ece151e287086e
824:::`

- Using the included tools in C:\Tools, create a local terminal that assumes the identity of the secret NT Administrator user.

![Screenshot 2022-02-11 at 19.00.07](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.00.07.png)

We will grab the Debug Privilege first: *privilege::debug*. This is the privilege we need in order to work with processes like lsass.exe.

![Screenshot 2022-02-11 at 19.01.27](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.01.27.png)

When we get it then the next stage is to use: sekurlsa::pth for Pass The Hash. Then the specified username – in this case administrator – and then domain: localhost, because in this case, we don’t have any kind of domain credentials and /ntlm with that particular hash. The command looks like this:

*sekurlsa::pth   /user:Administrator   /domain:localhost /ntlm:<here you put NT Hash>*

![Screenshot 2022-02-11 at 19.09.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.09.48.png)

- Abuse your newfound powers to establish a persistent administrator shell to class-42-target2-win7.

![Screenshot 2022-02-11 at 19.26.04](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.26.04.png)

![Screenshot 2022-02-11 at 19.28.12](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.28.12.png)

- Create a file on target2’s desktop. Once you’re able to remotely manipulate the target computer as the Administrator user, this portion of the lab is complete.

![Screenshot 2022-02-11 at 19.32.54](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.32.54.png)

![Screenshot 2022-02-11 at 19.36.11](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-42/Screenshot 2022-02-11 at 19.36.11.png)