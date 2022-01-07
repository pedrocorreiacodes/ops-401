## Class 29

### Reading: Threat Modeling

------

Threta modeling works to identify, communicate, and understand threats and mitigations within the context of protecting somehting of value

**A threat module is a structed representation of all the information that affects the security of an application.** It is a view of the application and its environment through the lens of security.

Threat modeling can be applied to a wide range of things, including software, applications, systems, networks, distributed systems, Internet of Things (IoT) devices, and business processes.

A threat model typically includes:

+ Description of the subject to be modeled
+ Assumptions that can be checked or challenged in the future as the threat landscape changes
+ Potential threats to the system
+ Actons that can be taken to mitigate each threat
+ A way of validating the model and threats, and verification of success of actions taken

Threat modeling is a process for capturing, organizing, and analyzing all of this information. Applied to software, it enables informed decision-making about application security risks. In addition to producing a model, typical threat modeling efforts also produce a prioritized list of security improvements to the concept, requirements, design, or implementation of an application.

#### Objectives of Threat Modeling

Threat modeling is a family of activities for improving security by identifying threats, and then defining countermeasures to prevent, or mitigate the effects of, threat to the system. A threat is a potential or actual undesirable event that may be malicious or or incidental. Threat modeling is a planned activity for identifying and assessing application threat and vulnerabilities.

#### Threat Modeling Across the LifeCycle

Threat modeling is best applied continuously throughout a software development project. The process is essentially the same at diffent levels of abstraction, although the information gets more and more granluar throughout the lifecycle. Ideally, a high-level threat model should be defined early on in the concept or planning phase, and then refined throughout the lifecyle. As more details are added to the system, new attack vectors are created and exposed. The ongoing threat modeling process should examine, diagnose, and address these threats.

#### Threat Modeling: Four Quetion Framework

A possible threat exists when the combine likelihood of the threat and impact it would have on the organization create a signficant risk. The four question framework that can help organize threat modeling:

+ What are we working on?
+ What can go wrong?
+ What are we going to do about it?
+ Did we do a good job?

Attempting to evaluate all the possible combinations of threat agent, attack, vulnerability, and impact is often a waste of time and effort. It is helpful to refine the search space in order to determine which possible threats to focus on.

+ Assess Scope - What are we working on? This might be as small as a sprint, or as large as a whole system.
+ Identify what can go wrong - This can be as simple as a brainstorm, or as structured as using STRIDE, Kill Chains, or Attack Trees.
+ Identify countermeasures or manage risk - Decide what you're going to do about each threat. That might be to implement a mitigation, or to apply the accept/transfer/eliminate approaches of risk managemt.
+ Assess your work - Did you do a good enough job for the system at hand?

#### Benefits

Done right, threat modeling provides a clear "line o sight" across a project that justifies scurity efforts. The threat model allows security decision to be made rationally, with all the information on the table.

The threat modeling process naturally produces an assurance argument that can be used to explain and defend the security of an application. An assurance argument starts with a few high level claims, and justifies them with either subclaims or evidence.

### Reading: A Begginers Guide To The Stride Security Threat Model

------

One common threat modeling approach is the STRIDE framework, which has six areas of focus:

+ Spoofing
+ Tampering
+ Repudiation
+ Information Disclosure
+ Denial of Service
+ Elevation of Privilege

Authored in 1999 by two Microsoft security researchers, STRIDE remais a useful approach to surface potential issues.

#### Spoofing

When you provide access to your systems data, you ned to authenticate every request. The security of your systems depends upon trust in the other party's identity. A threat to this trust is spoofing - when someone claims to be a person or system they are not.

There are many types of spoofing, form the teenager's fake ID to more serious infiltration of technology systems.

A major are of concern is network security, as much of our connectd deviced are dependent upon trusting the identity of other devices. In these systems, passwords, keys, tokens, and signatures are among the methods used to authenticate requests. The level of vulnerability varies based on the method.

Common authentication methods for systems and what would be required to spoof a request:

+ Single key: many APIs use a single API Key to authenticate request to their services. The value is static, though it can typically be deleted and regenerated in a user interface. Anyone who obtains the key would have access to the systems that trust it indefinitely.
+ Access token: similar to the single key, and access token is one value that authenticates a request. However, the access is usually limited in some way, often only usable for a short period. Anyone with an access token would only have minimal usage before needing additional credentials to generate another token.
+ Signatures: in contrast to the other two methods, signature-based authenticaton uses encryption, which requires private keys. Each request is signed using a shared secret that you can verify. To spoof a signature, the attacker would need access to the sender's private key.

The important thing to consider is what mechanism you're using to communicate identity and how you know the identity can be trusted. Look to common methods and conventions, such as open source libraries, to ensure your systems are secure and not vulnerable to spoofing attacks.

#### Tampering

Data is especially susceptible to threats of tampering, but physical machines or hardware may also be vulnerable.

There are methods to both prevent and discover tampering with networked systems. Firewalls and partitioned storage are among the tecniques you might empoy to ensure your data cannot be overwritten. Log files and notifications are common methods to detect tampered data.

Often, data tampering coincides with other potential threats. Data may be altered to spoof accesss, or data tampering could be caused by artificially-elevated privileges. Further, data tampering may cover the tracks of other vulnerabilities, such as overwriting log files that would show how the system was accessed.

#### Repudiation

You can't prevent attempted security threats, but you can implement auditing to catch and trace these activities. Done correctly, you can be certain that these nefarious efforts can be connected to the source of the vulnerablity.

Repudiation threats take aim at your auditing and tracing, ensuring that bad behavior cannot be proven.

All events with security importance should be logged.

Secure systems should build in non-repudiation mechanisms, such that the data source and the data itself can be trusted. For this reason, repudiation is intertwined with other elements of the SRIDE framework. For example tampered logs or a spoofed account both could lead to the user denying wrondoing.

#### IInformation Disclosure

Underlying the security threats mentioned so far is data exposure. Any system that stores or access private information may accidentally disclose it. There are any number of methods that can be used to access private data. These disclosures can impact a single user, multiple people, or be specific to a business itself.

Along with threats like spoofing, disclosures can be cause by backups and other files left in accessible locations, which might include servers, laptops, or external drives. In other circumstances, private data can be inadvertently exposed due to buggy code or attacks such as buffer overflows.

#### Denial Of Service

Another security threat from the technical news, a denial of service makes a system unreachable by exploiting resources so they can't be used for legitimate purposes. In networking, this can mean overloading a system with incoming requests, making it impossible for users to connect.

You should consider all areas of your systems that might by subject to a denial of service threat. For example, storage and processing may be areas of concern. A denial of service's impact may increase when combined with other security threats, which might give the attacker access to additional resources.

#### Elevation Of Privilege

The final are of the STRIDE framework could be the most threatening. Where spoofing is focused on authentication, elevation of privilege is related to authorization. In other words, the attacker not only claimed to be a valid user, but one with an expanded role.

A sophisticated elevation of privilege attack may use all of the other areas of STRIDE for an especially outsized impact.

With admin access, the attacker may be able to tamper with systems outside of the typical interfaces. The lack of audit trail could cause both repudiation and information disclosure without any trace. Of course, as mentioned in the previous section, more privileges likely translate to great resources for a denial of service.

