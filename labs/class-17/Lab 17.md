## Lab 17

### Part 1: VPC Creation

------

AWS provides you a “default VPC” whenever you launch an EC2 instance. In this first step of the lab, you’ll create and customize your own VPC.

#### Login to your AWS Management Console and click the Services dropdown. Add VPC and EC2 to favorites, you’ll need quick access to them throughout today’s lab.

![Screenshot 2021-12-29 at 12.37.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2012.37.57.png)

#### Navigate to VPC Management Console.

![Screenshot 2021-12-29 at 12.43.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2012.43.58.png)

#### Create a VPC named “class-17-vpc” with an IPv4 CIDR block of 10.0.0.0/16. Ensure that the tag “class-17-vpc” is created for this VPC object.

Go to **Your VPCs** and select **Create VPC**:

![Screenshot 2021-12-29 at 12.45.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2012.45.30.png)

FIll the form according to the lab instruction and click **Create VPC** at the bottom:

![Screenshot 2021-12-29 at 12.46.27](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2012.46.27.png)

![Screenshot 2021-12-29 at 12.49.39](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2012.49.39.png)

#### Create the following subnets and associate them with class-17-vpc:

#####  Class-17-public-subnet

###### Select an appropriate IPv4 CIDR block that is within the scope of the VPC network, but does not take up the whole network. This subnet should accommodate up to 250 hosts.

Go to **Subnets** and click **Create Subnets**, on the **VPC ID** dropdown menu select the newly created VPC **class-17-vpc**:

![Screenshot 2021-12-29 at 12.52.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2012.52.38.png)

###### What did you select and why? You may need to calculate subnets with online tooling to assist with making a determination here.

The CIDR block of 24 fits into the VPC block of 16

![Screenshot 2021-12-29 at 13.20.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2013.20.51.png)

##### Class-17-private-subnet

###### Once again, select an IPv4 CIDR block that is within the scope of the VPC network but does not overlap with class-17-public-subnet. This subnet should accommodate up to 250 hosts.

Go to **Subnets** and click **Create Subnets**, on the **VPC ID** dropdown menu select the newly created VPC **class-17-vpc**:

![Screenshot 2021-12-29 at 13.52.39](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2013.52.39.png)

![Screenshot 2021-12-29 at 13.57.31](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2013.57.31.png)

###### What did you select and why?

We need a different subnet from the previous one that fits in the VPC block of 16.

###### Did you leave room for additional subnets in the future to be added? How many could potentially be added?

Yes we did, with a subnetmask of 255.255.255.0/24 we can have up to 256 subnets each one with 254 hosts.

### Part 2: Security Group

------

#### In the VPC Management Console, you’ll need to select Security Groups and create a new security group with the following parameters:

Go to **Security Groups** and select **Create security group**:

##### Name: class-17-vpc-security-group

![Screenshot 2021-12-29 at 14.01.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.01.01.png)

##### Description: Allow selective ports

![Screenshot 2021-12-29 at 14.01.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.01.38.png)

##### VPC: class-17-vpc

![Screenshot 2021-12-29 at 14.02.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.02.09.png)

#### Create inbound rules that allow the following:

- All ICMP (IPv4) from anywhere
- All SSH from anywhere
- All RDP from anywhere
- All HTTP from anywhere
- All HTTPS from anywhere

![Screenshot 2021-12-29 at 14.07.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.07.30.png)

#### On the outbound, permit all traffic to anywhere.

+ Create an optional tag:
  + Key: Name
  + Value: class-17-vpc-security-group

![Screenshot 2021-12-29 at 14.08.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.08.56.png)

##### If successful, you’ll see “Security group (name) was created successfully.” If you ran into issues, troubleshoot until resolved.

#### Include a screenshot of your “Inbound Rules” table in your submission. It should have exactly ten entries.

![Screenshot 2021-12-29 at 14.18.04](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.18.04.png)

### Part 3: Internet Gateway

------

#### In the VPC Management Console, navigate to Internet gateways and create a new one named “class-17-vpc-igw”.

+ Apply a name tag.

![Screenshot 2021-12-29 at 14.32.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.32.55.png)

![Screenshot 2021-12-29 at 14.33.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.33.10.png)

#### While the internet gateway is created, it is not yet attached to your VPC. You can click the “Attach to a VPC” popup to do so.

- Select class-17-vpc.

- What is the AWS CLI command corresponding to this action?

  ![Screenshot 2021-12-29 at 14.35.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.35.26.png)

- You should get a success message and see the State changed to “Attached.

![Screenshot 2021-12-29 at 14.34.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.34.07.png)

![Screenshot 2021-12-29 at 14.34.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2014.34.29.png)

### Part 4: NAT Gateway

------

#### Deploy a NAT gateway between your private and public subnet that allows the Ubuntu Server in your private subnet to access the internet without exposing itself. Here’s some helpful documentation:

Go to **Virtual Private Cloud** > **NAT Gateways** and select **Create NAT gateway**.

Select the public subnet to be associated with this NAT gateway and select **Allocate Elastic IP** to assign an Elastic IP address to the NAT gateway. Click **Create NAT gateway** when you're done:

![Screenshot 2021-12-29 at 15.04.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.04.53.png)

![Screenshot 2021-12-29 at 15.05.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.05.32.png)

#### Update the route table associated with your private subnet.

Go to **VIRTUAL PRIVATE CLOUD** > **Subnets** and select the private subnet. At the bottom go to **Route table** and click on the **Route table:** link:

![Screenshot 2021-12-29 at 15.16.16](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.16.16.png)

At the bottom go to the **Routes** tab and click **Edit routes**:

![Screenshot 2021-12-29 at 15.17.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.17.44.png)

Select **Add route**. **Destination** should be `0.0.0.0/0` (all) and **Target** should be the newly create NAT gateway. Click **Save changes**:

![Screenshot 2021-12-29 at 15.25.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.25.43.png)

![Screenshot 2021-12-29 at 15.27.48](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.27.48.png)

### Part 5: Instance Deployment

------

#### Switch back to EC2 and launch the following instances:

##### Ubuntu Server 20.04 LTS (HVM), SSD Volume Type to class-17-public-subnet

![Screenshot 2021-12-29 at 15.33.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.33.19.png)

- In Step 3: Configure Instance Details, you can assign the instance to your new VPC and subnet under Network and Subnet dropdown menus.

![Screenshot 2021-12-29 at 15.34.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.34.33.png)

- Remember to specify class-17-vpc-security-group in Step 6.

![Screenshot 2021-12-29 at 15.35.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.35.09.png)

+ AWS should warn you with something like this:

![Screenshot 2021-12-29 at 15.35.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.35.51.png)

- Is this a concern, or does it fit with the goals of your cloud architecture?

It fits with the goals of the cloud architecture, we want this machine to be public accessilble.

![Screenshot 2021-12-29 at 15.37.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.37.58.png)

#### Ubuntu Server 20.04 LTS (HVM), SSD Volume Type to class-17-private-subnet

![Screenshot 2021-12-29 at 15.38.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.38.54.png)

- In Step 3: Configure Instance Details, you can assign the instance to your new VPC and subnet under Network and Subnet dropdown menus.

  ![Screenshot 2021-12-29 at 15.39.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.39.29.png)

  ![Screenshot 2021-12-29 at 15.39.56](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.39.56.png)

- AWS may warn you with the same prompt as before.

  ![Screenshot 2021-12-29 at 15.43.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.43.36.png)

- Is this a concern, or does it fit with the goals of your cloud architecture?

It is as this instance should be private and not accessible via internet.

### Part 6: Wrap Up

------

#### Shut down your two Ubuntu instances and NAT gateway to avoid incurring cloud charges.

![Screenshot 2021-12-29 at 15.45.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.45.26.png)

Make sure you delet **NAT gateways** as well:

![Screenshot 2021-12-29 at 15.46.18](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-17/Screenshot%202021-12-29%20at%2015.46.18.png)
