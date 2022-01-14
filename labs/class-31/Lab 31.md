## Lab 31

### Part 1: Staging

------

#### Download and import the Flare VM OVA.

![Screenshot 2022-01-13 at 18.18.31](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2018.18.31.png)

#### Set the network adapter to NAT Network.

![Screenshot 2022-01-13 at 18.24.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2018.24.09.png)

#### Login as labuser / labuser.

![Screenshot 2022-01-13 at 18.36.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2018.36.38.png)

### Part 2: My First YARA Rule

------

#### Access the “yara tools” folder on the desktop. This shortcut will take you to the directory where yara64.exe is installed. You’ll need to call yara64.exe from command line to use it.

![Screenshot 2022-01-13 at 18.49.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2018.49.50.png)

#### Create a text file containing a string of your choosing.

![Screenshot 2022-01-13 at 18.52.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2018.52.15.png)

#### Create a YARA rule that tests whether the target file contains the string of your choosing.

#### Include comments in your YARA rule.

![Screenshot 2022-01-13 at 19.13.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2019.13.56.png)

#### Execute the YARA rule against the target file.

Go to `C:\ProgramData\chocolatey\lib\yara\tools`:

![Screenshot 2022-01-13 at 19.27.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2019.27.48.png)

#### Explain whether the rule tested positive or negative. How can you tell?

The rule tested positive. Upon execution it printed to the console the name of the rule that was triggered.

#### Create a file that does not contain your string. Run your rule against it to generate a negative. Note the difference in output.

![Screenshot 2022-01-13 at 19.30.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2019.30.51.png)

![Screenshot 2022-01-13 at 19.33.22](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2019.33.22.png)

The rule tested negative. There was not output to the console.

### Part 3: Customizing ClamAV with YARA Rules

------

Go to `C:\Program Files\ClamAV\conf_examples`modify the example to look like this:

![Screenshot 2022-01-13 at 20.27.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.27.44.png)

![Screenshot 2022-01-13 at 20.41.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.41.05.png)

Rename it to `clamd.conf`and move it up in directory to `ClamAV`:

![Screenshot 2022-01-13 at 20.30.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.30.13.png)

#### Run Fresh Clam to pull the latest virus signatures database into ClamAV’s database directory. You may need to edit the configuration files in ClamAV directory to facilitate the process.

![Screenshot 2022-01-13 at 19.44.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2019.44.48.png)

#### Practice running ClamAV to perform a scan against the eicar.com file in the ClamAV directory.

#### Include a screenshot of the positive detection.

![Screenshot 2022-01-13 at 20.44.37](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-31/Screenshot 2022-01-13 at 20.44.37.png)

#### Use ClamAV to scan your target text file from Part 2 using the rule you created in Part 2. Do this by instructing ClamAV to use your YARA rule instead of its signature database. Include a screenshot and explanation of how you achieved this.

![Screenshot 2022-01-13 at 20.48.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.48.15.png)

With the `-d`flag we specify the database for ClamAv to use, in our case a YARA rule. Note that the rule must have the `.YARA`extention.

#### Next, instruct ClamAV to scan the target text file from Part 2 using both the rule we created and ClamAV’s signature database. Include a screenshot and explanation of how you achieved this.

First we have to move our rule to ClamAv's database:

![Screenshot 2022-01-13 at 20.50.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.50.26.png)

Now we scan with the default database (spoiler alert, it works!):

![Screenshot 2022-01-13 at 20.52.02](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.52.02.png)

#### Create a new YARA rule named “is_pe_file_clamav_1.yara”.

#### Write the rule to look for the string “MZ” in its target.

![Screenshot 2022-01-13 at 20.57.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2020.57.07.png)

#### Test the rule using ClamAV against a PE file and a non-PE file. Include screenshots and discussion.

Testing against a PE file:

![Screenshot 2022-01-13 at 21.01.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2021.01.51.png)

It detects it against the rule.

And now testing against a non-PE file:

![Screenshot 2022-01-13 at 21.03.35](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-31/Screenshot%202022-01-13%20at%2021.03.35.png)

It does not detect it as in infected file.

### Part 4: Reporting

------

#### What else can YARA detect?

YARA can be used for anomaly detection on files. I can also detect the size of certain files and metada data such as the author and date of the files.

#### What if you don’t have a single string to search for in the target?

We can search with regular expressions or hexadecimal strings.

#### How would you explain ClamAV’s “file decomposition” feature?

File decomposition is a feature that allows the user to analyze a file that reside in an archive or packed in an executable. ClamAV will proceed to unpack the file and the run the YARA engine on top of it.
