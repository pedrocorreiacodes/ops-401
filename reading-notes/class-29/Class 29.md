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