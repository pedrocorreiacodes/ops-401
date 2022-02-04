## Class 39

### Reading: Understanding SQL Injection, Identification and Prevention

------

SQL injection attacks are one of those situations whre the outcome can be widly disproportionate to the amount of effort that went into executing it.

#### Why SQL Injection Matters

Standardized query language (SQL) is, in one form or another, still the dominant method of inserting, filtering and retrieving informatino from a database. Loads of SQL queries will be coursing through your web applications on almost every page load.

Armed with literally nothing but a web browser, some basic SQL knowledge and an internet coonnection, an attacker can exploit flaws in your web application - extracting user data, discovering or resetting credentials and using it as a launch point for deeper assaults on your network.

In order to understand injection/vulnerabilities, we need to take a step back an review that baisc SQL knowledge first.

#### What is SQL?

It's not usually regarded this way, but SQL is a full programming language unto itself.

#### What's a Database Table?

In a database, lists are called tables, and they're the fundamental bulding block of how data is structured in a database. At its core, a table is simply a list of information. **Atributes** are the columns of a table.

#### What are the basic SQL Commands?

You use SQL commands to Creat, Read, Update and Delete (CRUD) the information inside of your tables. Most web applications and frameworks revolve around these same principles, bulding out forms to manipulate the underlying data which is stored in the database.

#### How To Select Data

Select statement have lots of options and can get really complex, but the most important thing to know about is filtering (adding condiions to get only the rows you really want in a table) - this is where the most common type of SQL injection attack occurs

#### Why is string concatenation the root of all evil?

Programmers refer to a sequence of non numeric characters as a "string.

What is known is that a string concatenation is a quick and easy way to build SQL statements.

`URL: /show_me_the_cheese?id=1`

The ID value of '1' gets passed into the web app and a SQL query is built by putting together the portion of the command you know you need to run along with the id vale that will chnge on every page url.

`sql_string = "SELECT * FROM products WHERE id = " + id`

After this, the sql_string variable will be:

`SELECT * FROM products WHERE id = 1`

The sql_string value then gets passed into the database library gets the chees in question and returns it so the web page can be displayed.

It's evil because it's too easy and doing string concatenation of SQL statements is the fastest road to having your site and applicaiton owned.

String concatenation doesn't care what pass into it. It doesn't know what an "id" is supposed to look like, so when a malicious trickster changes the "id" value in the URL from a 1 to:

`URL: /show_me_the_cheese?id=(UPDATE products SET price = 0.1 WHERE ID =1) `

The same web application code will be executed as before:

`sql_string = “SELECT * FROM products WHERE id = ” + id`

Except this time the sql_string will have a value of:

```
SELECT * FROM products WHERE id =
 (UPDATE products
 SET price = 0.1
 WHERE ID = 1)
```

#### How do Web Frameworks Prevent SQL Injection?

While web frameworks are typically thought of to be productivity enhancers, most incorporate best security practices for their programming language. Security (and in particular web security) is a complex topic and it's exceedingly difficult to cover all the angles that you'd need to on your own.

In general, web frameworks prevent SQL injection attacks by providing easy methods fo data querying so that developers aren't seduce into writing hidesoulsy vulnerable SQL string concatenation statements.

They perform two important taks:

First, they offer specific user input sanitization countermeasures to defeat common SQL Injection patterns: the framework will strip **NULL characters**, **line breaks**, **single quotes**, etc. that are often used to piggyback additional SQL commands into an intended query.

Second, they provide a syntax for declaring what a SQL statement is supposed to look like before actually trying to execute it. Depending on what framework you're using, the name may vary, but the intent is the same: make sure that the form of the SQL statement that you want to execute is correct prior to running it.

#### What's vulnerable to SQL injection attacks?

Traditionally SQL injection attacks (which have been around since the invention of the HTML tag) have been the domain of big web applications. 

Since the early days of the web a couple important developments have happened: one technological and one user focused.

The user development was simply that a billion people have now gotten online and while some still Google for "Facebook.com" - most people are more comfortable with browsers and general web concepts than any other generalized form of computing interface.

The technological advancement was the development of SQLite as an absolutely crackerjack, free portable database - suitable for use in things like mobile apps development, internet of things devices, networking equipment and any other geegaw that would previously have made use of a poorlyformatted text file as a storage mechanism.

Together, these two advancements are responsible for:

Everything having a web configuration interface backed by a database.

Everything being susceptible to SQL injecction attacks.

Which is why we now live in a world where:

+ Smart Home Hubs - Can be compromised. Their credentials overridden, people could spy on you from your own security system.
+ Network Equipment - Once cracked, network devices like routers and switches offer a tremendous foothold for lauching more in depth attacks deeper into a network.
+ Electric Sport Cars - Have to date mostly only had their accounts compromised, but it's not unthinkable that things like remotely disabling the car or other more dangerous features could be implemented.
+ Android Apps - Once compromised your private pictures and contacts are vulnerable.
+ iOS Apps - The interconnectedness of mobile apps and the APIs they depend upon offer a new entry point for many SQL injection attacks.

#### What can web servers do to help?

##### Apache

ModSecurity (which also works with NGINX and IIS) provides a de fault corset of rules that will filter basic SQL injection attacks.

##### Nginx

Naxsi, an open source web application firewall that acs as a 3rd party module to Ngnix blocking many of the tell tale characteristics of SQL Injection attacks.

For example, Naxi defaulst SQL Injection rules would prevent url parameters o `--`(the SQL Comment string often used to piggyback attacks).

##### Internet Information Server

IIS v7.0+ (so literally any version of IIS you should be using in production) have the ability to filter inbound http requests.

The official IIS blog has directions for adding first level HTTP filters:

##### In NoSQL Safe from SQL Injection?

NoSQL is the catch all term for a variety of storage technologies that can complement or replace traditional relational data base management systems (servers that store data that have tables that are related to one another and that you query with SQL). Sometimes reffered to as "Document Databases" or Key/Value stores they offer a simplified storage system (no need to define tables ahead of time) and at different storage points may be faster in data reads and writes.

It's interesting and useful to think about how broad NoSQL and Key/Value storage solutions like MongoDB, Redis, Memsql, Cassandra, etc. deal with attacks that are similar, if not strictly "SQL Injection" attacks.

In MongoDB, the only method to query data is via Binary JSON (BSON) request objects. You literally can't just pass in some slapped together string riddled with SQL injection statements.

But you can pass in executable Javascript as part of a BSON query object.

#### Defense in Depth Checklist for SQL Injection Attack?

Like anthing else computer security related, the only true protection is defense in depth from attacks, multiple layers of complementary defensive measures that together provide an overarching layer of protection:

The following checklist is intended to help you trace an application query execution path and to identify where you can add additional security layers:

##### Database

+ Sufficient and appropriate database user permissions set
+ Extraneous and unused database features disabled
+ Database loggin enabled
+ Database backup / restore procedure
+ Database connection filtering procedures enabled
+ Database drivers up to date

##### Application

+ Using filtering options
+ Using parameterization options
+ Using DB calls only when needed? Could you use a static site generator?)
+ Code lint/checks for potential SQL injection points
+ Manual check for SQL Injection prone points
+ Application logging

##### Web Server / Web Firewall

+ Use WAF SQL Injection pre-filters
+ Rate limit to prevent mass SQL Injection attempts
+ Alert on SQL injection pattern attempts