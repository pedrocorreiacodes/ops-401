## Lab 12

### Part 1: Staging

------

#### Log in as student1 with a password of student1

![Screenshot 2021-12-15 at 21.13.35](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.13.35.png)

![Screenshot 2021-12-15 at 21.17.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.17.07.png)

#### Log into the same Splunk server you used yesterday and run the BOTSv1 app to access the lab instructions. You’ll want to use the public server for querying data, and your private one for following the instructional prompts.

![Screenshot 2021-12-15 at 21.18.49](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.18.49.png)

### Part 2: BOTSv1

------

#### Run the Splunk app, Investigating with Splunk Workshop.

![Screenshot 2021-12-15 at 21.26.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.26.43.png)

#### You’ll now be working on completing the following sections in Boss of the SOC (BOTS) Version 1, Scenario #1 - APT:

##### Reconnaissance

Drilling down on the sourcetype of stream:http to see what kind of web data is being seen on the wire.

![Screenshot 2021-12-15 at 21.43.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.43.36.png)

Selecting `src_ip`fields:

![Screenshot 2021-12-15 at 21.46.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.46.58.png)

![Screenshot 2021-12-15 at 21.48.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.48.51.png)

A threat actor made a vulnerabily scan from the ip `40.80.148.42`:

![Screenshot 2021-12-15 at 21.50.09](/Users/baphomet/Library/Application Support/typora-user-images/Screenshot 2021-12-15 at 21.50.09.png)

Now it's important to validate this finding. 

If we take the IP address we found with our stream data and change our sourcetype to Suricata (an IDS tool and more), we can see a number of logged events coming from that source IP address.

Web server signatures meaning that this IP address is indeed scanning our website.

![Screenshot 2021-12-15 at 21.59.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2021.59.30.png)

 When hunting or handling incidents, results may lead to additional questions and searches may build on one another. Outputs from previous questions may provide you with hints. We can now search for traffic from 40.80.148.42 and examine the src_headers for clues related to the tool being used for the scan.

In the source headers, we can see information that says (Acunetix Web Vulnerability Scanner - Free Edition):

![Screenshot 2021-12-15 at 22.05.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.05.26.png)

If we see something in our logs and we don’t know what it is, Google fu!

[Google for Acunetix](https://splunk2.samsclass.info/en-GB/static/@8a94541dcfac:0/app/investigate_workshop/APT-google-accunetix.png)

Acunetix is in fact a web vulnerability scanner so we can confirm our earlier findings.

![Screenshot 2021-12-15 at 22.09.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.09.21.png)

How do we figure out the systems that are operating within the environment? "e want to know what is running on our website because IT and Dev may not have told us how our production applications are built.

Let's check the IP of the victim:

![Screenshot 2021-12-15 at 22.16.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.16.13.png)

We can again drill down and see what source IP addresses are associated with our domain. It appears that only two source IPs are seen in the http traffic. One of them is associated with 95% of the traffic, so a reasonable assumption would be that this address is the one of greatest interest. We can start to check the URLs or URIs to get an idea of the kind of files and directory structures being requested. 

![Screenshot 2021-12-15 at 22.17.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.17.50.png)

Joomia is an open source CMS system. 

Let's get a configrmation, starting with adding a response header of 200 to our search to indicate successful page loads. Adding the search command called `stats` that will allow us to count the number of events grouped by URI and another transformational command called sort and return results in descending order based upon the count so that our result set is formatted in the manner we would like to see it:

![Screenshot 2021-12-15 at 22.22.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.22.36.png)

We could search the IIS logs and examine the URI strings being accessed to find indicators and verify that the http response code equals 200.

![Screenshot 2021-12-15 at 22.24.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.24.30.png)

![Screenshot 2021-12-15 at 22.25.22](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.25.22.png)

![Screenshot 2021-12-15 at 22.25.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-15%20at%2022.25.52.png)

##### Exploitation

What IP address is likely attempting a brute force password attack against imnotreallybatman.com?

Stream data allows us to look at HTTP traffic, we start with a very broad search of the index and the sourcetype:

![Screenshot 2021-12-16 at 13.07.47](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2013.07.47.png)

Because we know our webserver is 192.168.250.70, we can look for http traffic going to that IP address.

![Screenshot 2021-12-16 at 13.08.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2013.08.59.png)

If we pivot to look at the http_method of these requests, we see nearly twice as many POSTs as GETs. Since we are talking about a brute force password attack of a web site:

![Screenshot 2021-12-16 at 13.37.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2013.37.52.png)

A brute force password attack to a web page would most likely be a POST, so let's add this to our search

![Screenshot 2021-12-16 at 13.40.12](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2013.40.12.png)

If the website is not encrypted or it is being decrypted for logging, we may be able to see login attempts.

The form_data field contains information being passed from the client browser to the web server. The table command will take a result set and place specific fields into a tabular view that is easy to read. It will also remove all other values from the result set.

![Screenshot 2021-12-16 at 13.42.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2013.42.48.png)

The stats command allows us to do computations grouped by one or more fields. We want a count grouped by the source address, or src field.

The source address of 23.22.63.114 is seen 412 times

![Screenshot 2021-12-16 at 13.59.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2013.59.13.png)

![Screenshot 2021-12-16 at 14.09.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.09.26.png)

![Screenshot 2021-12-16 at 14.10.21](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.10.21.png)

![Screenshot 2021-12-16 at 14.11.40](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.11.40.png)

Now we are looking for the first password used, we will want to include the form_data and at least one additional field as well.

The `reverse` command takes the output of our result set and flips the order of the results. In this case, our oldest results are now on top. 

![Screenshot 2021-12-16 at 14.23.16](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.23.16.png)

Using the ***rex\*** command in Splunk provides a way, using regular expression syntax, to do an extraction of the password that creates a new field containing password string values that can be easily manipulated with Splunk.

![Screenshot 2021-12-16 at 14.24.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.24.37.png)

 Extracted the password values with regular expressions:

![Screenshot 2021-12-16 at 14.27.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.27.13.png)

By adding the ***values\*** function to our ***stats\*** command, we can see that the brute force attack came from 23.22.63.114 but it appears that the actual penetration with the correct password came from 40.80.148.42.

![Screenshot 2021-12-16 at 14.32.47](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.32.47.png)

The next logical step is to get an idea of the time and the URI that is associated with the actual penetration

![Screenshot 2021-12-16 at 14.35.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.35.54.png)

![Screenshot 2021-12-16 at 14.36.27](/Users/baphomet/Library/Application Support/typora-user-images/Screenshot 2021-12-16 at 14.36.27.png)

![Screenshot 2021-12-16 at 14.37.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.37.17.png)

By using AS after the stats calculation we can rename the output of that calculation without using the ***rename\*** command. It’s just an efficient way to change the name of the calculated value.

Let's calculate an average for the passwords lengths If we want the answer rounded off to the integer, we can add another `eval` command with the `round` function to specify the field we want to round:

![Screenshot 2021-12-16 at 14.40.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.40.13.png)

We now want to understand when the brute force attack gave the adversary the correct password and when the adversary used this password to get into the system. We know the password of interest is "batman" because we saw it being used twice, once during the scan and again from a different IP address to login. Based on that, we should look for the delta in time between these batman login events.

The `transaction` command gives us an easy way to group events together based on one or more fields and returns a field called duration that calculates the difference between the first and last event in a transaction:

![Screenshot 2021-12-16 at 14.42.03](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.42.03.png)

While investigating the brute force attempt, gathering more information about the attack is important.

Calculating the number of unique passwords helps understand the spread of the password attempts.Calculating the number of unique passwords helps understand the spread of the password attempts.

With the use of the `distinct count (dc)`function within the `stats` command, this becomes very easy. Distinct count will look for every unique value within a field and count them.

![Screenshot 2021-12-16 at 14.43.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-12/Screenshot%202021-12-16%20at%2014.43.41.png)

### Part 3: Reporting

------

#### Explain in your own words:

##### What kind of attack was taking place on Wayne Enterprises systems?

Brute force attack resulting in web stite defacing.

##### Describe your findings for each stage of the kill chain:

###### Reconnaissance

In the Reconnaissance phase we descovered the IP scanning the web server and the type of vulnerability scanner used. Also the web server targeted

###### Weaponization

The threat actor methodologies and tools used for the attack

###### Delivery

Malware used for the attack

###### Exploitation

Origin of the brute force attack, first password use to attempt a login. All the passwords used for the login and the one who granted access. We also explored the time sequence of the events and the unique number of paswords used during the brute force attack

###### Installation

Determined the hash of the uploaded file and the malicious executable.

###### Command & Control (C2)

Exposed the FQDN of the threat actor system.

###### Actions on Objectives

The file responsible for the web site defacing

##### How could the kill chain have been disrupted to prevent the attacker from progressing?

Simple measures to prevent a brute force attack. Limiting the number of password attempts, two factor authentication and more long and complext passwords.
