## Lab 36

### Part 1: Staging

------

#### This lab requires Web Security Dojo OVA.

![Screenshot 2022-01-31 at 18.53.33](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 18.53.33.png)

### Part 2: XSS on DVWA

------

#### Login to DVWA as the administrator. For each successful outcome achieved, include the string you typed into the field and a screenshot of the outcome.

#### Set DVWA Security to “Low”

![Screenshot 2022-01-31 at 19.02.18](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.02.18.png)

#### Perform the following XSS (Reflected) exploits:

##### Have the site return your name as a larger font

`<h1>Pedro</h1>`

![Screenshot 2022-01-31 at 19.07.16](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.07.16.png)

##### Have the site return your name in a different color

`<font color ="pink">Pedro</font>`

![Screenshot 2022-01-31 at 19.10.00](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.10.00.png)

##### Have the site return your name in a popup box

`<script>alert("Pedro")</script>`

![Screenshot 2022-01-31 at 19.12.54](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.12.54.png)

### Set DVWA Security to “Medium”

![Screenshot 2022-01-31 at 19.15.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.15.08.png)

### Perform the following XSS (Reflected) exploits:

#### Have the site return your name in a popup box

Just add another atribute to the <script> tag. `<script type="application/javascript">alert("Pedro")</script>`

![Screenshot 2022-01-31 at 19.26.51](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.26.51.png)

#### Have the site return the session cookie in a popup box

We can use the document property `document.cookie`. `<script type="application/javascript">alert("Pedro" + document.cookie)</script>`

![Screenshot 2022-01-31 at 19.29.11](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.29.11.png)

### Part 3: Evaluating InsecureWebApp with w3af

------

#### Launch w3af (GUI version)

#### Scan http://insecure.local:8080/insecure/public/Login.jsp

![Screenshot 2022-01-31 at 19.38.55](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.38.55.png)

#### Include a screenshot of the rendered response of the XSS vulnerability as discovered in w3af GUI that is associated with the “Forgot Login” page

#### Include a screenshot of the results of the web crawler.

![Screenshot 2022-01-31 at 19.40.57](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-36/Screenshot 2022-01-31 at 19.40.57.png)

### Part 4: Reporting

------

#### What is XSS, and why is it a security threat?

XSS stands for Cross site scripting, a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. With these attacks threat actors can steal the other user's identity data, cookies, session token and other information.

#### What is a session cookie?

It's basically a pice of data store in the user's computers by the web browser while browsing a website. It keeps track that users session within that website.

#### How can a session cookie be abused by an attacker?

If an attacker can get hold on a session cookie it can basically usurp the users identity.