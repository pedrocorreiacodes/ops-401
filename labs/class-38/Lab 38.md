## Lab 38

### Part 1: Staging

------

This lab requires Web Security Dojo VM.

![Screenshot 2022-02-02 at 12.51.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 12.51.44.png)

Juice Shop is manually launched via shell script from the start menu > targets section.

![Screenshot 2022-02-02 at 12.52.52](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 12.52.52.png)

Access the Juice Shop page to verify it is up.

![Screenshot 2022-02-02 at 14.11.06](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 14.11.06.png)

Install Git with `sudo apt update` then `sudo apt install git`.

![Screenshot 2022-02-02 at 14.12.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 14.12.32.png)

Git clone [SecLists](https://github.com/danielmiessler/SecLists) to your Web Security Dojo.

![Screenshot 2022-02-02 at 14.17.41](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 14.17.41.png)

### Part 2: TryHackMe Burp Suite Lab

------

Complete the lab at [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop). Respond to any questions/prompts here in your submission instead of on the TryHackMe page.

#### Task 1: Open for business!

Nothing to do here but to review the primer and move forward into Task 2.

#### Task 2: Let’s go on an adventure!

*Walking through the application, which is also a form of reconnaissance.*

The reviews show each user's email address. Which, by clicking on the Apple Juice product, shows us the Admin email:

![Screenshot 2022-02-02 at 15.51.04](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 15.51.04.png)

We can now see the search parameter after the /#/search? the letter q:

![Screenshot 2022-02-02 at 15.54.10](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 15.54.10.png)

![Screenshot 2022-02-02 at 15.55.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 15.55.49.png)

#### Task 3: Inject the juice

**Question #1: Log into the administrator account!**

How did you log into Bender’s account?

After we navigate to the login page, enter some data into the email and password fields.  Before clicking submit, make sure Intercept mode is on. This will allow us to see the data been sent to the server.

![Screenshot 2022-02-02 at 16.36.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 16.36.49.png)

Now let's change the "**a**" next to the email to: **' or 1=1--** and forward it to the server.

1. The character ' will close the brackets in the SQL query
   'OR' in a SQL statement will return true if either side of it is true. As 1=1 is always true, the whole statement is true. Thus it will tell the server that the email is valid, and log us into user id 0, which happens to be the administrator account.
2. The -- character is used in SQL to comment out data, any restrictions on the login will no longer work as they are interpreted as a comment. This is like the # and // comment in python and javascript respectively.

Use in the `email`field -> `' or 1=1--`

![Screenshot 2022-02-02 at 17.40.29](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 17.40.29.png)

![Screenshot 2022-02-02 at 17.24.01](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 17.24.01.png)

**Question #2: Log into the Bender account!**

Similar to what we did in Question #1, we will now log into Bender's account! Capture the login request again, but this time we will put: bender@juice-sh.op'-- as the email. 

![Screenshot 2022-02-02 at 17.44.40](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 17.44.40.png)

![Screenshot 2022-02-02 at 17.45.49](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 17.45.49.png)

#### Task 4: Who broke my lock?

We will look at exploiting authentication through different flaws. Mechanisms that are vulnerable to manipulation:

+ Weak passwords in high privileged accounts
+ Forgotten password pages

**Question #1: Bruteforce the Administrator account's password!**

 Let's try a brute-force attack. Capture a login request, but instead of sending it through the proxy, we will send it to Intruder.

![Screenshot 2022-02-02 at 19.08.17](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.08.17.png)

Let's load the **best1050.txt from Seclists** to Burp. Go to **Payloads** -> **Payload Options** -> **Load ...**:

![Screenshot 2022-02-02 at 19.12.46](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.12.46.png)

Click **Start Attack**:

![Screenshot 2022-02-02 at 19.26.02](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.26.02.png)

Password is `admin123`.

**Question #2:** **Reset Jim's password!**

The reset password mechanism can also be exploited.

![Screenshot 2022-02-02 at 19.34.50](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.34.50.png)

Ssecurity question : Samuel.

####  Task 5 AH! Don't look!

A web application should store and transmit sensitive data safely and securely. But in some cases, the developer may not correctly protect their sensitive data, making it vulnerable.

Most of the time, data protection is not applied consistently across the web application making certain pages accessible to the public. Other times information is leaked to the public without the knowledge of the developer, making the web application vulnerable to an attack. 

**Question #1:** **Access the Confidential Document!**

Navigate to the **About Us** page, and hover over the *"Check out our terms of use"*. You will see that it links to [http://MACHINE_IP](http://machine_ip/ftp/legal.md)[/ftp/legal.md](http://machine_ip/ftp/legal.md). Navigating to that **/ftp/** directory reveals that it is exposed to the public.

![Screenshot 2022-02-02 at 19.41.06](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.41.06.png)

**Question #2:** **Log into MC SafeSearch's account!**

![Screenshot 2022-02-02 at 19.45.27](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.45.27.png)

**Question #3: Download the Backup file!**

We will now go back to the [http://MACHINE_IP](http://machine_ip/ftp/)[/ftp/](http://machine_ip/ftp/) folder and try to download **package.json.bak**. But it seems we are met with a 403 which says that only .md and .pdf files can be downloaded. 

To get around this, we will use a character bypass called "**Poison Null Byte**". A Poison Null Byte looks like this: ***%00***. 

As we can download it using the url, we will need to encode this into a url encoded format.

The Poison Null Byte will now look like this: ***%2500**.* Adding this and then a **.md** to the end will bypass the 403 error!

![Screenshot 2022-02-02 at 19.52.45](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 19.52.45.png)

####  Task 6 Who's flying this thing?

Modern-day systems will allow for multiple users to have access to different pages. 

Administrators most commonly use an administration page to edit, add and remove different elements of a website.

When Broken Access Control exploits or bugs are found, it will be categorised into one of **two types**:

+ Horizontal Privilege Escalation - Occurs when a user can perform an action or access data of another user with the **same** level of permissions.
+ Vertical Privilege Escalation - Occurs when a user can perform an action or access data of another user with a **higher** level of permissions.

First, we are going to open the **Debugger** on **Firefox**. 

Then are then going to refresh the page and look for a javascript file for **main-es2015.js**

We will then go to that page at: [http://MACHINE_IP](http://machine_ip/)/main-es2015.js

This hints towards a page called “/#/administration” as can be seen by the about path a couple lines below, but going there while not logged in doesn’t work.

As this is an Administrator page, it makes sense that we need to be in the Admin account in order to view it.

A good way to stop users from accessing this is to only load parts of the application that need to be used by them. This stops sensitive information such as an admin page from been leaked or viewed.

![Screenshot 2022-02-02 at 20.07.35](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-38/Screenshot 2022-02-02 at 20.07.35.png)

**Question #2: View another user's shopping basket!**

