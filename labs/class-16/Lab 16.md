## Lab 16

### Part 1: Users and Groups

------

You’ll need an AWS account for this lab along with AWS CLI installed to your computer. Using your favorite shell, utilize AWS CLI to perform the below operations. Be sure to capture screenshots of each successful execution in your shell terminal.

Follow **[THIS](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fiam%2F%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fiam&forceMobileApp=0&code_challenge=ZNIA_tSrQ3QTjKJuH57cXOrraBJRmf14_RJdo44kwxg&code_challenge_method=SHA-256)** guide to connect via CLI to AWS:

![Screenshot 2021-12-28 at 16.47.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2016.47.32.png)

- Check S3 to see if you have an S3 bucket with data in it. If not, create a bucket and put a text file with a line of data in it for testing access later on in this lab.

![Screenshot 2021-12-28 at 16.48.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2016.48.09.png)

![Screenshot 2021-12-28 at 16.52.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2016.52.45.png)

![Screenshot 2021-12-28 at 17.33.22](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2017.33.22.png)

#### EC2-Admin

![Screenshot 2021-12-28 at 17.49.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2017.49.59.png)

##### Attach an Inline Policy that permits the group to view (Describe) information about Amazon EC2 and Start or Stop instances.

![Screenshot 2021-12-28 at 17.55.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2017.55.42.png)

![Screenshot 2021-12-28 at 17.55.34](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2017.55.34.png)

#### EC2-Support

![Screenshot 2021-12-28 at 17.59.31](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2017.59.31.png)

![Screenshot 2021-12-28 at 17.59.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2017.59.52.png)

#### S3-Support

![Screenshot 2021-12-28 at 18.02.14](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.02.14.png)

![Screenshot 2021-12-28 at 18.02.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.02.50.png)

#### Create the following users:

- **user-1**
- **user-2**
- **user-3**

Took some creative liberties here:

![Screenshot 2021-12-28 at 18.05.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.05.59.png)

#### Add users to their corresponding groups

![Screenshot 2021-12-28 at 18.10.24](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.10.24.png)

![Screenshot 2021-12-28 at 18.11.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.11.30.png)

![Screenshot 2021-12-28 at 18.11.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.11.57.png)

![Screenshot 2021-12-28 at 18.12.16](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.12.16.png)

### Part 2: Testing and Validation

------

#### Test and validate user permissions.

To test using the web portal got to **Identify and Access Management (IAM)**, **(Users)** and enable **Console password** for each user.

##### Sign in as each user using a new incognito (Chrome)/inPrivate (Firefox) window on your browser.

For the user in the **EC2-Admin** group:

![Screenshot 2021-12-28 at 19.14.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.14.29.png)

![Screenshot 2021-12-28 at 19.16.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.16.58.png)

![Screenshot 2021-12-28 at 19.17.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.17.20.png)

![Screenshot 2021-12-28 at 19.18.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.18.26.png)

For the user in the **EC2-Support** group:

![Screenshot 2021-12-28 at 19.20.20](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.20.20.png)

![Screenshot 2021-12-28 at 19.20.57](/Users/baphomet/Library/Application Support/typora-user-images/Screenshot 2021-12-28 at 19.20.57.png)

![Screenshot 2021-12-28 at 19.21.20](/Users/baphomet/Library/Application Support/typora-user-images/Screenshot 2021-12-28 at 19.21.20.png)

For the user in the **S3-Support** group:

![Screenshot 2021-12-28 at 18.42.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.42.59.png)

![Screenshot 2021-12-28 at 18.58.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2018.58.54.png)

![Screenshot 2021-12-28 at 18.58.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.00.00.png)

![Screenshot 2021-12-28 at 19.02.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-16/Screenshot%202021-12-28%20at%2019.02.29.png)

### Part 4: Reporting

------

#### How did your testing go?

Everything went as expected.

#### Did you catch any misconfiguration and need to alter users or groups?

No.

#### Why is proper IAM important on the cloud?

IAM ensures control over which users have access to which applications / services. 

Having authentication and authorization mechanisms in a single platform allows consistency when managing user acess. In the case of someone leaving the company, that person's access rights may be immediately revoked, offering protection agains privilege creep attacks.
