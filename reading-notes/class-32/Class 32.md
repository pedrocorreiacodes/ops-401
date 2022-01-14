## Class 32

### Reading: What is Malware Analysis? Definition, Types, Stages, and Best Practices

------

Malware is defined as "a software designed to infiltrate or damage a computer system wihtout the owner's informed consent. Any software performing malicious actions, including information stealing, spying, etc., can be referred to as malware."

Malware analysis is defined as "The process of dissecting malware to understand its core components and source code, investigating its characteristics, functionality, origin, and impact to mitigate the threat and prevent future occurences."

+ **It breaks down the malware:** A big part of malware analysis is demystifying malware and cyberthreats to increase awareness.

  Malware, is only a software program written with the expressed pupose of causing harm. Understanding the code and how it works is integral to blocking malware entry or, at least, its spread across your ecosyste,-

+ **It investigates its characteristics**: Every software will leave a unique digital footprint, and malware is no different. How does a specifc malware variant or family approach data? How does it spread? What is its pace of replication and tactic for camouflage?

  Knowing the exact characteristics of maleare makes t easier to detect it.

+ **It unravels it functionality**: This is a critical element of malware analysis, and it is difficult to get right. Malware will typically wait in hiding unitl the right time to attack. This means its functionality will not become clear to the  user before it's too late. Malware analysis tries to determine the intended functinoality of the software by reviewing its code.

+ **It traces the malware's origin**: Malware canbe notoriously hard to trace, and hackers take advantage of this by holding data ransom for large amounts. Malware analysis tries to see beyond the anonumization of the coder and trace it back to its origin - a person, an IP, a geographic location, or even an organization, among others. This helps in the swift interventon of legal authorities during an attack.

+ **It tries to predict the impact**: By puttin the above threads of investigation together, it is possible to arrive at a probable impact profile. Its functionality, nature of target systems, the pace of growth, and preferred distribution channels indicate the worst-case scenario impact of malware. This enables companies to plan and deploy mitigation procedures.

#### Malware Analysis Process

##### Step 1: Catpure the malware

Before the actual analysis, you need access to a malicious piece of code in an uncompressed format. You can use a tool llike Honey DB to attract malware and capture it.

##### Step 2: Build a malware lab

A malware analysis lab is a safe environment where you can test different malware functonalities without any risk to nearby files.

Typically, malware labs rely on virtual machines to sandbox the entire exercise.

##### Step 3: Install your tools

You can use several tools to analyze malware, including open-source and paid options. You can use the Cuckoo Sandbox and other equivalent analysis enablers. The tools must be instlalled in the VMs

##### Step 4: Record the baseline

Before running the malware, assess the operating environment and document it as your baseline. The tools installed in the VMs will help there. Running the same tools after the malware is activated will indicate malware behavior and impact.

##### Step 5: Commence your investigation

There are several phases involved in the investigation step. Some require intense manual involvement, while others can gain from automation tools. Tkae the malware apart before initiating these phases to reveal its properties at every layer.

##### Step 6: Document the results

Depending on the tools you're using you will have detailed information on malware behaviour, tendencies and interaction patterns with its surrounding digital environment. Consolidate these results into an exhaustive document that forms the dliverable for your malware analysis exercise.

Malware analysis is at the heart of cybersecurity innovation today.

Analysts can work with governments, non-profit organization, research institutions, and corporates to develop the body of knowledge around malware.

#### Types of Malware Analysis

Broadly, there are two types of malware analysis - static and dynamic.

You could also classify malware analysis based on the effort it requiress, opting for either manual or automated analysis.

A complete analysis exercise will combine all of these types to study the malware in detail and test how it reacts to different approaches.

1. ##### Static malware analysis

   This type of analysis focus on the dynamic elements of malware, examining static properties like metadata, headers, embedded assets, etc. A quick static analysis often reveals enough information needed to create an idicator of compromise (IOC), a document recording the software's malicious nature. In case the results of static analysis are optimistic, the code is usually discarded like a piece of bad programming, not meriting further investigaton as malware.

2. ##### Dynamic malware analysis

   Dynamic analusis allows the malware to play itself out in a controlled environment while observing its behavior. VMs are critical when conducting dynamic analysis, as it is likely that the malware will cause irreparable damage ot its host environment.

   Seveal behavioral signals require your attention during dynamic malware analysis, including its interactions with network traffic, its targeting patterns toward the file system, and any changes to the registry.

   By baselining the host environment before and after dynamic analysis, you can lear more about the malware's behaioral tendencies. Thats why this type of analysis is also known as behavior analysis.

3. ##### Manual malware analysis

   In a manual analysis, an analyst may choose to break down the code manually, using tools like debuggers, decompilers, and decrypters. Manual analysis often reveals the strategic intent behind malicious software; because the analyst examines the core logic of the algorithm and tries to predict the logic behind elements that seem unnecessary at first appearance.

   Manual analysis is also known as code reversing since you are essentially beginning with the final software, moving backward into code, and then arrivng at the original logic.

4. ##### Automated malware analysis

   Automated analysis passes the malware through an automated workflow where its different behavioral and static properties are tested. This may not provide insights into the software's logic, but it is extremly useful for understanding its broader classification and to which malware family it might belong to.

   Automation can generate detailed reports and feeds data into an incident response system, bringing only the most necessary signals to a human analyst. Falcon Sandbox and the AI-powered SNDBOX are some of the tools that can help you do this.

Each type of malware analysis has its own purpose. It's advisable to execute all of them in conjunction to create a holistic picture of what the malicious app is capable of and how to prevent its entry into user systems. Particularly, the manual code reversal approach aids in getting to the very root of the problem - why the malware was created in the first  place.

#### Key Stages of Malware Analysis

You can break down malware analysis into three key stages. These coincide with the types of malware analysis listed above.

1. ##### Observing malware behavior

   At the initial stages, malware analysts run tools to execute short, manual exercises to force it to react. Once the malware react ot its surrounding environment it becomes easier to understand whether it is harmless or a potential threat.

   A popular tool used to observe malware behavior is Wireshar, a tool that simulates multiple network conditons and inspects malware behavior in the face of different protocols. Behavioral studies could be as simple as running antivirus in the virtual environment to check how the malware responds.

   Combining the benefits of automation and maual strategy, you can use behavioral analysis frameworks to create reusable analysis script that puts the malware through its paces in a live virtual environment.

   Combining the benefits of automation and manual strategy you can use behavioral analysis frameworks to create reusable analysis script that put the malware through its paces in a live virtual environment.

2. ##### Disassembling the code

   Disassembling the code involves both static analysis - where you look at the unchangeable elements of the malware code - as well as its inner logic. Code disassembly relies on manual efforts to a large extent, which is why it is recommended that malware analyts bring some knowledge in binary and assembly language. Typically, three types of tools can help at this stage:

   + A **disassembler** deconstructs the malware into its primitive binary form and reconstructs it into assembly language that's comprehensible for a human analyst.
   + A **debugger** conducts a code walkthrough and highlights unusual/suspicious-looking code elements where the malware analyst must investigate further.
   + A **decompiler** recreates the original source code of a program and can help identify a coder's digital fingerprint to trace its origin.

   The first two stages focus on the malware's surface identity and ambient behaviour, while the next stage combs through its potential impact.

3. ##### Examine the memory

   At this stage, we dive into the forensic artifacts left behind by the malware on your system's memory. The average malware is often 1MB or less in size, so it is difficult to observe its memory imprint in everyday computing environments. A malware analysis lab provides the conditions necessary to benchmark the pre-malware memory state, run it, and then extract artifact resulting from its functionalities.

   Memory analysis can be extremely difficult, as you are looking for the most minute of digital imprints left behind by an extremely light application designed for stealth.

   In other words, this stage reveals further information on behavior even after the malware has stopped running.

Acoss these three strages, our goal is to learn more about the malware, how it works, and how it would respond in different scenarios.

#### Top 6 Malware Analysis Best Practices for 2021

As cyber threats grow more sophisticated, ethical hackers and malware analysts need to evolve in tandem. The end-to-end analysis procedure can be complex, requiring industry knowledge, innovating thinking, and the right tools. However, it is possible to simplify it significantly through the following best practices:

1. Expand your malware sample size continuously.
2. Use automation to optimize your efforts.
3. Always use a secure environoment to run malware.
4. Only analyze malware whose remote infrastructure is running.
5. Capture and store VM image snapshots.
6. Do you research and select the best-fit malware analysis tools.