## Class 03

## Readings: Cyber Risk Analysis

------

Risk is a crucial element in all our lives. In every action we plan to take in our personal and profissional lives, we need to analyze the risks associated with it.

Risk management involves comprehensive understanding, analysis and risk mitigating techniques to ascertain that organizations achieve their information security objective. Risk is fundamentally inherent in every aspect of information security decisions and this risk management concepts help aid each decision to be effective in nature.

Major components of Security and Risk Management crucial for CISSP:

+ Information security within the organization /Security Mode
+ The triad of information security - Condifentiality, Integrity and Availability
+ Security governance principles
+ Business continuity requirements
+ Policies, standards, procedures, and guidelines
+ Risk management concepts
+ Threat modeling

#### Goals of a security model

------

The two primary objectives of information security within the organization from a risk management perpective include:

+ Have controls in place to support the mission of the organization

+ All the decisions should be based on risk tolerance of organization, cost and benefit

+ Strategy leads to Tactics; Tactics lead to Operations

+ Operational Goals:

  + Patching computers as needed
  + Updating anti-virus signatures
  + Maintaining the overall network on a daily basis

+ Tactical goals:

  + Moving computers into domains
  + Installing firewalls
  + Segregating the network by creating a demilitarized zone

+ Strategy goals:

  + Having all domains centrally administered and implementing VPNs and RADIUS servers to provide a highly secure environment that provides a good amount of assurance to the management and employees.

+ A security model has different layers, but it also has different types of goals to accomplish in different time frames:

  + Daily goals or operational goals:
    + Focus on productivity and task-oriented activities to ensure the company's functionality in a smooth and predictable manner.
  + Mid-term goals, or tactical goals:
    +  Could mean integrating all workstations and resources in one domain so more central control can be achieved.
  + Long-term goals or strategic goals:
    + May involve moving all the branches from dedicated communication lines to frame relay, implementing IPSec virtual private networks (VPNs) for all remote users instead of dial-up
    + Integrating wireless technology with the comprehensive security solutions and controls existing within th environment 

  This technique and approach to strategy is called the **planning horizon**. A company cannot usually implement all changes at once, and some changes are larger than others. If an organization whose network is currently decentralized, and works in workgroups without any domain trust, wants to implement its own certificate authority (CA) and public key infrastructure (PKI) enterpris wide, this cannot happen in a week's time. The operational goals are to keep production running smooth and mae small steps towards readying the environment for a domain structure. the tactical goals would be to put all workstations and resources into a domain structure and centralize access controls and authentication.

  The strategic goals is to have all workstations, servers, and devices within the enterprise use the public key infrastructure to deliever authentication, encryption, and additional secure communication channels.

Generally, security works best if it's Operational, Tactical, and Strategic goals are defined and work to support each other.

### Security fundamentals

------

Confidentiality, integrity and availability (the CIA triad) is a typical security framework intended to guide policies for information security within an organization.

**Confidentiality: Prevent unauthorized disclosure**: Confidentiality of information refers to protecting the information from disclosure to anauthorized parties.

Key areas for maintaining confidentiality:

+ **Social Engineering**: Trainiing and awareness, defining Separation of Duties at the tactical level, enforcing policies and conducting Vulnerability Assessments
+ **Media Reuse**: Proper Sanitization Strategies
+ **Eavesdropping**: Use of encryption and keping sensitive information off the network with adequate access controls 

**Integrity: Detect modification of information**: The integrity of information denote protecting the sensitive information from being modified by unauthorizes parties.

Key areas for maitaining confidentiality:

+ **Encryption**: Integrity based algorithms
+ **Intentional or Malicious Modification**
  + Message Digest (Hash)
  + MAC
  + Digital Signatures

**Availability: Provide timely and reliable access to resources**: Availability of information signifies ensuring that all the required or intented parties are able to access the information when need.

Key areas for maintaining availability:

+ Prevent single point of failure
+ Comprehensive fault tolerance (Data, Hard Drives, Servers, Network Links, etc.)

#### Best practices to support CIA

------

+ Separation of Duties: Prevents any one person from becoming too powerful within and organization. This policy also provides singleness of focus. Separation of Duties is a preventative control.
+ Mandatory Vacations: Prevents an operator form having exclusive use of a system. Periodically, that individual is forced to take a vacation and relegate control of the system to someone else. This policy is a detective control.
+ Job rotation: Similar in purpose to mandatory vacation, but with the added benefit of cross-training employees.
+ Least privilege: Allowing users to have only the required access to do their job.
+ Need to know: In addition to clearance, users must also have "need to know" to access classifed data.
+ Dual control: Requiring more than one user to perform a task.

#### Risk - Key points to be aware of 

------

+ Every decision starts with looking at risk.
+ Determine the value of your assets.
+ Evaluate and identify cost effective solutions to reduce risk to an acceptable levels (rarely ca we elimitate risk).
+ Keep in mind that safeguards are proactive and countermeasures are reactive

**The following definitions are crucial for risk management:**

+ Asset: Anything of value to the company
+ Vulnerability: A weakness; the absence of a safeguard
+ Threat: Things that could pose a risk to all or parts of an asset
+ Exploit: an instance of compromise
+ Risk: The probability of a threat materializing
+ Controls: Physical, Administrative and Technical Protections
  + Safeguards
  + Countermeasures 
+ Multiple scenario-based use cases are evaluatedin CISSP, based on the following sources of risk:
  + Weak, unpatched or non-existence anti-virus software
  + Disgruntled employess posing internal threat
  + Poor physical security controls
  + Weak access controls
  + Lack of change management
  + Lack of ofrmal processes for hardening systems
  + Poorly trained users and lack of awareness.
+ Lifecycle of Risk Management
  + Risk Assessment
    + Categorize, Classify and Valuate Assets
    + Know/Idenitfy Threats and Vulnerabilities
  + Risk Analysis
    + Qualitative
    + Quantitative
  + Risk Mitigation/Response
    + Reduce/Avoid
    + Transfer
    + Accept/Reject

#### Mitigating Risk

------

* Three acceptable risk responses:
  * Reduce
  * Transfer
  * Accept
* Continue to monitor for risks
* How we decide to mitigate business risks become the basis for Security Governance and Policy



**Risk** is the likelihood and impact (or consequence) or a threat actor exploiting a vulnerability.

+ Core mission of cybersecurity professionals is to manage and mitigate risk for the employer or client. (Save company money).
  + **People**
  + **Process**
  + **Technology**
+ A **vulnerability** is a weakness that could be triggered accidentally or exploited intentionally to cause a security breach.
  + A **zero-day** cyber attack attempts to exploit a vulnerability nobody know about.

+ A **threat** is the potential for someone or something to exploit a vulnerability and breach security. A threat may be interntional or unintentional.

#### Risk Management Lifecycle (ISC2)

------

What is **risk management lifecycle (ISC2)**? 

+ Risk Assessment
+ Categorize, Classify and Value Assets
+ Know/Identify Threats and Vulnerabilities

Risk Analysis:

+ Qualititative
+ Quantitative

Risk Response

+ Reduce
+ Avoid
+ Transfer
+ Accept/Reject

#### Quantitative Risk Analysis

------

CompTIA SEC+ Example 1:

+ Vulnerability + Threat = Risk

CompTIA Sec+ Ecample 2:

+ Risk = Impact * Likelihood

This involves assigning monetary values to trisk components.

**Asset Value (AV)** - How much is the asset worth?

**Exposure factor (EF)** - Percentage of Asset Value lost?

**Single Loss Expectancy (SLE)**:

+ What does it cost if it happens once*
+ SLE = AV x EF

**Annual Rate of Occurence (ARO)** is how often wil happen per year.

**Annualized Loss Expectancy (ALE)** is what it costs per year if we do nothing:

+ ALE = SLE x ARO

**Total Cost of Ownership (TCO)** is the mititgation cost: upfront + ongoing cost (Normally Operational)



#### Qualitatively Risk Analysis

------

+ Softer approach, does not use data quantification

+ Rating system is used instead
+ Requires judgment, best practicesm intuition, and experience
+ Methods
+ Brainstorming
+ Delphi technique
  + Questionnaires
+ Storyboard
+ Focus groups
+ Surveys
+ Questionnairs
+ Checklists
+ One on one meetings

#### Risk management options 

------

+ Risk acceptance
  + Level of risk is known and accepted
+ Risk avoidance
  + Remove opportunity for risk to cause loss
+ Risk mitigation
  + Utilize security controls to reduce risk to acceptable levels
+ Risk transference
  + Pay an external party to accept the financial impact of a given risk

Can risk be elminated?

Cyber risk can't be fully eliminated, but it can be significantly mitigated.

**Residual risk** consists of the risk remaining after security controls have been put in place as means of risk mitigation.

**NIST Risk Management Framework (RMF)** is a voluntary guidance, based on existing standards, guidelines, and practices for organizations to better manage and reduce cybersecurity risk.

#### Cyber Hygiene

------

Following best practises.

Security policy -> Technical Controls -> Audit to make sure they're in place.

Includes practices and precautions that facilitate keeping sensitive data organized, safe and secure from exflitration and attack.

Regularly evaluate for cyber hygiene, perform vulnerability scans and assessments, and thereby generate risk assessments which facilitate better organizatonal decision making.