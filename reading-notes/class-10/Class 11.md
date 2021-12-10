## Class 11

### Lecture

------

#### Incident Response 

Lifecycle of a blue team analyst:

Preparation -> Identification -> Containment -> Eradication -> Recovery -> Post-incident Activity

#### Cyber Incident Response Team

+ Reporting, categorizing, and prioritizing (triage)
+ CIRT/CERT/CSIRT/SOC
+ Management/decision-making authority
+ Incident analysts
+ 24/7 availability
+ Roles beyond technical response
  + Legal
  + Human Resources (HR)
  + Marketing

#### Incident Identification

+ Precursor and detection channels
  + Security mechanisms (IDS, log analysis, alert)
  + Manual inspections
  + Notification procedures
  + Public reporting
  + Confidential reporting/whistleblowing
+ First responder
  + Member of CIRT taking charge of a reported incident
+ Analysis and incident identification
  + Classify and prioritize
  + Downgrade low priority alerts to log-only

#### Security and Information Event Management

+ Correlation
  + Static rules and logical expressions
  + Threat intelligence feeds
  + AI-assited analysis
+ Retention
  + Preserve evidence of attack
  + Facilitate threat hunting and retrospective incident identification

#### Loggin Platforms

+ Syslog
  + Loggin format, protocol, and server (daemon) software
  + PRI - facility and severity
  + Timestamp
  + Host
  + Message part
+ Rsyslog and syslog-ng
+ journalctl
  + Binary logging
+ Nxlog
  + Log normalization tool

#### About Syslog

+ Syslog is a Message Logging Standard for data about status, events, diagnostic, etc.
  + Uses UDP ports 514 and 601
  + Severity levels
    + Level 0 = Emergency
    + Level 5 = Warning
    + Level 6 = Informational
    + Level 7 = Debugging
+ Syslog servers collect and archive syslog data

#### Network, OS, and Security Log Files

+ System ans security logs
  + Application
  + Security/audit
  + System
  + Setup
  + Forwarded events
+ Network logs
  + Traffic and access data from network appliances
+ Authentication logs
  + Security log or RADIUS/TACACS+ application logs
+ Vulnerability scan output

#### The Problem... 

+ Windows event loggin isn't greatest for detecting security problems
  + Must correlate multiple different logs
  + Example: What is the parent process?
+ Executive questions to ask:
  + What are we logging?
  + What level of detail?
  + Why are we capturing logs this way?
  + How are we parsing them?

#### Solution: Sysmon

+ System Monitor (Sysmon) in an installable software from Microsoft Sysinternals that enhances event logging capabilitties
  +  Runs as a background service
  + Gathers detailed information about process creations, network connections, and changes to file creation time
  + Widely used by security teams to improve log data quality on Windoes endpoints
  + Requires a configuration file to get started
    + http://github.com/SwiftOnSecurity/sysmon-config

#### Sysmon Config File

+ Envet IDs indicate what type of Sysmon log is generated.
  +  EVENT ID 1: PROCESS CREATION
  + EVENT ID 2: PROCESS CHANGED A FILE CREATION TIME
  + EVENT ID  3: NETWORK CONNECTIONS
  + EVENT ID 4, 5: SYSMON SERVICE CHANGES
  + EVENT ID 6: DRIVER LOADED
  + EVENT ID 7: IMAGE LOADED

#### Reverse TCP Attack

Reverse TCP is an attack whereby the attacker is a TCP server issuing commands to the client.

+ This is backwards from a normal shell which is a forward TCP connectinon.
+ In a normal shell, the client issues commands to the server.

*The way to stop it is through logging*

#### Linux Data Streams

+ Linux data streams utilize Standard Input/Output (STDIO) for program input and output
  + **STDIN (file handle 0)** is standard input
    + Typically from the keyboard
    + Can be redirected from any file
  + **STDOUT (file handle 1)** is standard output
    + Sends the data stream to the display by default
    + Redirectable to a file or to pipe it to another program
  + **STDERR (file handle 2)** is a standard error
    + By default seen on the display

#### SOC Concepts

+ Security Operations Center (SOC) is a central team that monitors security infrastructure across the organization.
+ What does a SOC do?
  + Report on efficacy of security controls
  + Risk management
  + Incident response
  + Threat intelligence
+ A **security incident** is an event involving the breach of a system's security policy in order to affect its integrity or availability and/or the anauthotized access or attempted access to it
+ **Inciden Response (IR)** is the process by which and organization handles a data breach or cyberattack, including remediation
+ **Threat hunters**, however, do not perform the full IR lifecycle and instead focus on identification and detection
+ Data collection can and should be automated. What levels of data collection automation are there?
  + SQRRL automation maturity model attempts to assess a company's automation maturity

#### SOC Tool Categories

+ Security automation
  + Security automation and orchestration (SOAR) solutions coordinate, execute and automate taks, facilitator faster response to cybersecurity attacks
+ Example SOAR products:
  + Exabeam Incident Responder
  + Splunk Phantom
+ Robotic proces automation (RPA) is software that reduces the number of repetitive taks necessary to operate a computer by "robotically" imitating those actions.
  + Example use cases
    + Application invetory tracking
    + Data loss detection
    + Threat exposure
  + Example RPA product
    + CyberArk RPA
  + Alternatively, SOCs use custom-developed software and code that automate processes and perform analysis
+ Log Aggregation
  + **Security Information and Event Management (SIEM)** is a software that aggregates and analyzes activity from many different resrouce in your IT infrastructure
  + Examples
    + Splunk (commercial)
    + Elastic/ELK Stack (open source)
  + Performs
    + Event and log collection
    + Layered centric views or heterogeneous
    + Normalization
    + Correlation
    + Adaptability (scalable)
    + Reporting and alerting

#### Splunk Concepts

+ Splunk Enterprise is a SIEM software product that enables you to search, analyze, and visualize the data gathered from the components of your IT infrastructure or business.
+ Another major SIEM in this industry is *Elastic/ELK Stack*
+ **Search Processing Language (SPL)** is the query language designed by Splunk for use with Splunk software
+ SPL ecompasses all the search commands and their functions, arguments, and clauses
  + Syntax originally based on the Unix pipeline and SQL
  + SPL scope:
    + data searching
    + filtering
    + modification
    + manipulation
    + insertion
+ Stages of the SIEM data pipeline in Splunk
  + Stage1: Data input
    + Data accessed from the source and turned into 64k blocks
  + Stage2: Data storage
    + In the parsing phase, the Splunk software examines, analyzes and transforms the data.
    + In the indexing phase, the Splunk software writes parsed events to he index queue. The main benefit of using this is to make sure the data is easily available for anyone at the time of the search
    + Individual indexes are created as objects in Splunk, and you deine what scope of data gets monitored and goes into each index.



#### Splunk Architecture

+ An index is a repository of data.

  Indezes reside in flat files on the indexer, which transforms raw data into searchable events.

+ In a distributed search environment, a search head is a Splunk Enterprise instance that hands search management functions, directing search requests to a set of search peers and then mergin the results back to the user.

+ Forwarders provide reliable, secure data collection from various sources and deliver the data to Splunk Enterprise or Splunk Cloud for indexing and analysis.

+ Universal forwarders

  + Forward data from remote systems securely in real time
  + Have minimal resource overhead and impact on endpoint performance
  + Support thousands of machine data formats
  + Provide many features such as SSL, compression and buffering
  + What data sources does Splunk support?
    + Many. Includes old-fashioned syslog.
  + What data sources will Splunk typically be setup with?
    + Enterprise with multiple Windows Servers will forward their logs to Splunk
  + What ingestion techniques does Splunk support?
    + Syslog via Susmon
    + Splunk Universal Data Forwarder
  + What are some common challenges/problems encoutered with ingesting logs from many sources?
    + Incosistent time/date formatting
    + Syntax issues

