## Lab 39

### Part 1: Staging

------

This lab requires Web Security Dojo VM with an internet connection (NAT mode is recommended).

![Screenshot 2022-02-03 at 12.56.12](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 12.56.12.png)

### Part 2: OWASP Web Goat

------

Web Goat does not start automatically in Security Dojo. You’ll need to start it manually from command line. Open a terminal in Security Dojo and enter `sudo bash /home/dojo/targets/bin/webgoat-ng-Start.sh` to initialize Web Goat.

![Screenshot 2022-02-03 at 13.00.32](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 13.00.32.png)

In Firefox browse to http://webgoat.local:8081/WebGoat/ and login as guest, password guest. 

![Screenshot 2022-02-03 at 13.02.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 13.02.48.png)

Navigate to Injection Flaws and complete the following sections:

- String SQL Injection

![Screenshot 2022-02-03 at 13.27.06](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 13.27.06.png)

+ LAB: SQL Injection

  + Stage 1: String SQL Injection

  ![Screenshot 2022-02-03 at 13.02.48](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 13.02.48.png)
  + Stage 3: Numeric SQL Injection

![Screenshot 2022-02-03 at 14.21.35](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 14.21.35.png)

### Part 3: Portswigger

------

Access [Portswigger Academy](https://portswigger.net/web-security/all-labs) and complete at least three of the SQL labs.

#### Lab: SQL injection vulnerability allowing login bypass

![Screenshot 2022-02-03 at 14.47.43](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 14.47.43.png)

`x' or '1'='1` for the password field.

#### Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

When the user selects a category, the application carries out an SQL query like the following:

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

To solve the lab, perform an SQL injection attack that causes the application to display details of all products in any category, both released and unreleased.

With Burp  intercept and modify the request that sets the product category filter. Modify the `category` parameter, giving it the value `'+OR+1=1--`

![Screenshot 2022-02-03 at 14.58.22](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 14.58.22.png)

![Screenshot 2022-02-03 at 15.00.43](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 15.00.43.png)

#### Lab: SQL injection UNION attack, determining the number of columns returned by the query

This lab contains an SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other table.

The first step of such an attack is to determine the number of columns that are being returned by the query.

1. Modify the `category` parameter, giving it the value `'+UNION+SELECT+NULL--`. Observe that an error occurs.
2. Modify the `category` parameter to add an additional column containing a null value: `'+UNION+SELECT+NULL,NULL--`
3. Continue adding null values until the error disappears and the response includes additional content containing the null values.

![Screenshot 2022-02-03 at 15.15.09](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-39/Screenshot 2022-02-03 at 15.15.09.png)

### Part 4: Reporting

------

Answer the below questions in your own words:

- What is SQL injection?
  - An injection technique used to modify or retrive data from SQL data bases
- How is SQL injection detected?
  - Querying the database for common HTML tags
  - Examining webpages created from dynamic content for unexpected behavior
- How can a web app developer defend against SQL injection?
  - By propely sanitize all the data base queries