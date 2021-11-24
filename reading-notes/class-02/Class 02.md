## Class 02

### Readings: Cloud Security Principles and Frameworks

------

In the cloud there are things that AWS will do and things that the consumer will do. Supporting millions of customers on AWs requires a certain degree of flexibility in the services AWS offers. There are many different patterns, use cases, and requirements to satisfy.

#### The instance (or virtual machine) abstraction

The first abstraction introduced by AWS back in 2006. **Amazon Elastic Compute Cloud (Amazon EC2)**. The service that allows AWS customers to launch instances in the cloud. At this level, customers retain teh responsibility of the guest operating system and above (middleware, applications, etc.) and their lifecycle. AWS has the responsibility for managing the hardware and the hypervisor including their lifecycle.

At the same level of the stack theres is also **Amazon Lightsail**, the 'easiest way to get started with AWS for developers, small businesses, students, and other users who need a simple virtual private server (VPS) solution. Lightsail provides developers compute, storage, and netoworking capacity and capabilities to deploy and manage websites and web applications in the cloud'.

#### The container abstraction

With the rise of microservices, a new abstraction took the industry by storm in the last few years: **containers**. A container is a self-contained environment with soft boundaries that includes both your applicatio as well as the software dependencies to run it. Whereas an instance (or VM) virtualizes a piece of hardware so that you can run dedicated operating systems, a container technology virtualizes an operating system so that you can run separated applications with different (and often incompatible) software dependencies.

Modern containers-based solutions are usually implemented in two main logical pieces:

+ A containers **control plane** that is responsible for exposing the API and interfaces to define, deploy, and lfecycle containers. Also referred to as the container orchestration layer.
+ A containers **data plane** that is responsible for providing capacity so that those containers can actually run and connect to a network. From a practical perspective this is typically a Linux host or less often a Windows host where the contaners get started and wired to the network.

In 2014, Amazon launched a production-grade containers controlss plane called **Amazon Elastic Container Service (EC2**). A higly scalable, high performance containter management service that supports Docker.

In 2017, Amazon also announced the intention to release a new service called **Amazon Elastic Container Service for Kubernets (EKS)** based on Kubernets, a successful open source containers control plane technology

#### The function abstraction

At re:invent 2014, AWS introduced another abstraction layer. **AWS Lambda**. Lambda is an execution environment that allows an AWS customer to run a single function. Instead of having to manage and run a full-blown OS instance to run your code, or having to track all software dependencies in a user-built container to run your code, Lambda allows you to upload your code and let AWS figure out hwo to run it at sclae.

What makes lambda so special is its event -driven model. Not only can you invoke Lambda directly via the **Amazon API Gateway** but you can trigger a Lambda function upon an event in another AWS service.

You don't have to manage the infrastructure underneath the function you are running.

#### The bare metal abstraction

Also known as the "no abstraction"

In re:Invent 2017, AWS announced the Amazon EC2 bare metal instances.

#### The full container abstraction

**AWS Fargate** is a production-grade service that provides compute capacity to AWS containters control plane. Fargate is making the containers data plane fall into the "Provider space" responsabilitty.



Lecture