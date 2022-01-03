## Class 27

### Reading: PowerShell Empire Framework Is No Longer Maintained

------

The Empire post-exploitation framework used by hackers of all hats has been discontinued.

Empire was released in 2015 at he BSides Las Vegas conference to show how PowerShell could be used beyond the infection stage of an attack.

Its open-source nature and modular architecture allowed it to grow and fulfill the needs of offensive security teams, who saw in it an opportunity to test defenses by imitating attacks from real threat actors.

One of its major advantages is that it uses encrypted communication with the command and control server and made it difficult to detect its traffic, especiall in large networks.

And adversary can use Empire to control an agent planted on the compromised host and forward the attack. Further developmetn removed the necessity of powershell.exe on the infected machine.

Over time, numerous ecploit modules were added to the framework for various hacking needs, and a Python agent for Linux and macOS systems.

Empire was also embraced for malicious activities. Researchers saw it used y various threat groups, from nation-sate hackers to financially-driven ones.

The framework is very popular with malware operators due to being "lightweight and extensible for modular development"

Although discontinuing Empire is a blow to hackers on both side of the law, there are alternative frameworks available for red teams:

+ Apfell
+ Covenant
+ Silver
+ Faction