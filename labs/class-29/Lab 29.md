## Lab 29

### Part 1: Staging your Toolkit

------

#### You will need [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started) for today’s lab.

##### Download and install [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started)

![Screenshot 2022-01-11 at 16.08.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-29/Screenshot 2022-01-11 at 16.08.44.png)

![Screenshot 2022-01-11 at 16.09.17](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-29/Screenshot 2022-01-11 at 16.09.17.png)

### Part 2: Threat Modeling

------

#### Generate a threat model DFD using [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started)...

![Screenshot 2022-01-11 at 19.16.22](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-29/Screenshot 2022-01-11 at 19.16.22.png)

### Part 3: Communicate Findings

------

#### Contents

Application Name and Description
Revision History

1. Security Objectives
2. Application Overview
3. Application Decomposition
4. Threats
5. Vulnerabilities

#### Application Name and Description

The application is an Internet-facing Web application with a SQL Server back end.

#### Revision History

Pedro Correia		Created		01/01/22

1. #### Security Objectives

The application is an Internet-facing Web application with a SQL Server back end. The Web server is located in AWS. Business and data access logic resides on the Web server. The application enables Internet users to browse and purchase products from the company's product catalog.

##### Roles

Application roles are:

+ Internet users
+ Catalog administrators

#### Key Scenarios

Important application scenarios are:

+ Anonymous user accesses and views paystubs.
+ Anonymous user searches to locate a specific paystub.
+ Anonymous user logs in to authenticate prior to accessing paystubs or requesting time off.
+ Anonymous user creates a new account prior to accessing paystubs or requesting time off.
+ Authenticated user requests time off.

#### Technologies

The application uses the following technologies:

+ Web Server: Ubuntu Server 20.10
+ Database Server: Microsoft SQL Server 2019

#### Application Security Mechanisms

The most important application security mechanisms known at this time are:

+ Users are authenticated with Forms authentication.
+ Application is authenticated at the database by using Windows authentication.
+ Roles are used to authorize access to business logic.
+ Administration can be performed only by remotely logging on to the server computer using Team Viewer.

3. #### Application Decomposition

This section describes the trust boundaries, entry points, exit points, and data flows.

#### Trust Boundaries

Identified trust boundaries are:

+ The WAF.
+ The database server trusts calls from the Web application's identity.
+ The data access components trust the business components to pass fully validated data.
+ An entry point to catalog administration business component.

#### Data Flows

Data flows are:

+ An anonymous user browses Genisys. The details are retrieved from the database and returned to Genisys.
+ An anonymous user submits a search string. The home page accepts the search string and validates it by using a regular expression. The search string must be less than 50 characters in length and may include any combination of letters or numbers. The search string is passed to the data access component. The data access component calls a stored procedure and passes the search string as a single parameter.
+ The user logs on. The user submits a name and password through the logon form. The user name and password are handled by the logon page and passed to the membership business logic component. This component passes the data to the data access component, which verifies the credentials with the database to determine their validity.
+ An administrator logs on and accesses the SQL server. The administration component checks the user role at the business layer. 

#### Entry Points

Entry points are:

+ Port 80 for Web requests.
+ Port 443 for SSL.
+ All other ports are restricted by the firewall.
+ Port 80 and 5938 for System Administrators

#### Exit Points

The following threats could affect the application:

+ Brute force attacks occur against the Windows Server 2019.
+ Network eavesdropping occurs between the browser and Web server to capture client credentials.
+ An attacker captures an authentication cookie to spoof identity.
+ SQL injection occurs, enabling an attacker to exploit an input validation vulnerability to execute commands in the database and thereby access and/or modify data.
+ Cross-site scripting occurs when an attacker succeeds in injecting script code.
+ Cookie replay or capture occurs, allowing an attacker to spoof identity and access the application as another user.Information is disclosed and sensitive exception details are revealed to the client.
+ An attacker manages to take control of the Web server, gain unauthorized access to the database, and run commands against the database.
+ An attacker obtains the encryption keys used to encrypt sensitive data (including client credit card numbers) in the database.
+ An attacker or client obtains unauthorized access to Web server resources and static files.

5. #### Vulnerabilities

The application vulnerabilities are:

+ User password storage.
+ Lack of password complexity enforcement.
+ Lack of password retry logic.Missing or weak input validation at the server.
+ Failure to validate cookie input.
+ Failure to sanitize data read from a shared database.
+ Failure to encode output leading to potential cross-site scripting issues.
+ Exposing an administration function through the customer-facing Web application.
+ Exposing exception details to the client.