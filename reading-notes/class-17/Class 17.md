## Class 17

### Reading: Virtual Private Cloud (VPC)

------

#### What is a virtual private cloud (VPC)?

A VPC is a public loud offering that lets an enterprise establish its own private cloud-like computing environment on shared public cloud infrasctucture. A VPC gives an enterprise the ability to define and controls a virutal netowrk that is logically isolated from all other public cloud tenants, creating a private, secure place on the public cloud.

*Having a VPC is like having your own private condominium-no one else has the key, and no one can enter the space without your permission*

A VPC's logical isolation is implemented using virtual network function and security features that give and enterprise customer granuualr control over which IP addresses or applications can access particular resources.

#### Features

They give customer many of the advantages of private clouds, while leveraging public cloud resources and savings. 

Key features of the VPC mode:

+ Agility: Control the size of your virtual network and deploy cloud resources whenever your business needs them. 

  Resources can be scaled in real-time.

+ Availability: Redundant resources and highly fault-tolerant availability zone architectures mean your applications and workloads are highly avaialble.

+ Security: VPC is a logically isolated network, your data and applications won't share space or mix with those of the cloud provider's other customers, You have full control over how resources and workload are accessed, and by whom.

+ Affordability: VPC customers can take advantage of the public cloud's cost-effectiveness, such as saving on hardware costs, labor times, and other resources.

#### Benefits

+ Flexible business growth: Virtual servers, storage and networking - can be deployed dynamically, VPC customers can eaily adapt to changes in business needs.
+ Satified custuers: The high availability of VPC environments enables reliable online experiences that buld cusomter loyalty and increase trustç
+ Reduced risk across the entire data lifecyle: VPCs enjoy high levels of security at the instance or subnet level, or both. This gives you peace o mind and further increases the trust of costumers.
+ More resources to channel towards business innovation: With reduced costs and fewer demands on your internal IT team, you can focus your efforts on achieving key businesss goals and exercising core competencies.

#### Architecture

In a VPC, you can deploy cloud resources into your own isolated virtual network. These cloud resource - also know as logical instances - fall into three categories:

- Compute: Virtual server instances (VISs, also know as virtual servers) are presented to the user as vitual CPUs (vCPUs) with a preetermined ammount of computing power, memory, etc.

- Storage: VPC customers are typicallly allocated a certain block storage quota per account, with the ability to purchase more. It is akin to purchasing additional hard drive space. Recommendations fot storage are based o the nature of your workload

- Networking: You can deploy virtual version of various networking functions into your virtual private cloud account to enable or restric access to its resources. These include public gateways, which are deployed so that all ot some areas of your VPC environment can be made available on the public-facing Internet.

  Load balancers, which distribute traffic across multiple VSIs to optimize availability and performance; and routers, which direct traffic and enable communication between network segments.

  Direct or dedicated likns enable rapid and secure communications between your on-premises enterprise IT environment or your private cloud and your VPC resources on public cloud.

#### Three-tier architecture in a VPC

The majority of today's applications are designed with a three-tier architecture comprised of the following interconnected tiers:

+ The web or presentation tier, which takes requests from web browsers and presents information created by, or store within, the other layers to end users.
+ The application tier, which houses the business logic and is where most processing takes place
+ The database tier, comprised of database servers that store the data processsed in the application tier.

To create a three-tier application architecture on a VPC, you assign each tier its own subnet, which will give it its own IP address range. Each layer is automatically assigned its unique ACL

#### Security

VPCs achieve high levels of security by creating virtualized replicas of the security features used to control access to resources housed in traditional data centers.

These security features enable customers to define virtual networks in logically isolated parts of the public cloud and control which IP addresses have access to which resources.

Two types of network access controls comprise the layers of VPC security:

+ Access controls lists (ACLs): An ACL is a list of rules that limit who can access a particular subnet within your VPC. A subnet is a portion or subdivision of your VPC; the ACL defines the set of IP addresses or application granted acccess to it.
+ Security group: Whitin a security group, you can create groups of resources and assign uniforma access rules to them. For example, if you have three application in three different subnets, and you want them all to be public Internet-facing, you can place them in the same security group. Security groups act like virtual firewalls, controlling the flow of traffic to your virutal servers, no matter which subnet they are in.

#### VPC vs. ...

##### VPC vs. virtual private network (VPN)

A virtual private network (VPN) makes a connection to the public Intenet as secure as a connection to a private network by creating and encrypted tunnel through which the information travels. You can deploy a VPN-as-a-Service (VPNaaS) on your VPC to establish a secure site-to-site communication channel between your VPC and your on-premises environment or other location.

##### VPC vs. private cloud

Private cloud and virtual private cloud are sometimes - and mistakenly - used interchangeably. A virtual private cloud is actually a public cloud offering. A private cloud is a single-tenant cloud environment owned, operated, and managed by the enterprise, and hosted most commonly on-premises or in a dedicated space or facility. By contrast, a VPC is hosted on multi-tenant architecture, but each customer's data and workloads are logically separate from those of all other tenants. The cloud provider is responsible for ensuring this logical isolation.

##### VPC vs. public cloud

A virtual private cloud is a single-tenant concept that gives you the opportunity to create a private space within the public cloud's architecture.