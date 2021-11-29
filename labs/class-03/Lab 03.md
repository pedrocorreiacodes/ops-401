## Lab 03

### Part 1: Review the CyHy Report

------

###### Read through the CyHy Report and identify potential risks:

The following are Vulnerabilities assessed as **Critical**:

+ **MikroTik RouterOS < 6.41.3 SMV Buffer Overflow**. It is affect by a remote SMB buffer overflow vulerability that can bel leverage by an unauthenticated, remote attacker to execurte arbitrary code.
+ **MikroTik RouterOS HTTP Server Arbitrary Write RCE (ChimayRed)**. An unauthenticated, remote attacker can write data to an arbiraty location within the web server process causing a denial of service condition or the execution of arbitrary code.
+ **Portable SDK for UPnP Devices (libupnp) < 1.6.18 Multiple Stack-based Bufer Overflows RCE**. An unauthenticated, remote attacker can exploit this, via a specially crafted SSDP request, to execute arbitrary code

### Part 2: Create the Risk Assessment Report

------

###### Using the provided Excel worksheet, populate the fields and submit the completed worksheet.

Find in this folder the `Risk Assessment Worksheet.xlsx`.

###### What are the biggest cyber risks to Initrobe?

Based on the **Risk Assessment Report (RAR)** the biggest cyber risks to Initrobe are:

+ MikroTik RouterOS < 6.41.3 SMB Buffer Overflow
+ MikroTik RouterOS HTTP Server Arbitrary Write RCE (ChimayRed)
+ Portable SDK for UPnP Devices (libupnp) < 1.6.18
+ Multiple Stack-based Buffer Overflows RCE
+  Data Center Flood Risk.

These risks are highly likely to occur and to have a serious negative impact on the company. These risks could be mitigated by upgrading to the most recent software version.

To mitigate the Data Center Flood risk we would need first of all the keep regular backups on all the data in a CSP. It would be highly advisable to secure the data center premises against flooding .

### Part 3: Quantitative Deterministic Risk Calculation

------

###### For the **worst** case scenario:

+ Determine the AV, EF, and ARO. Justify your reasoning:
  + EF = 30% AV = $8,867,766,60 ARO = 0.25
  + 30% of the data center will be compromised due to the flooding (EF). The Asset Value (AV) is  $8,867,766,60. It is estimated that the data center will flood at most once every four years.

+ Calculate the SLE. Explain and justify your method:
  + SLE is calculated by assuming total loss of the 30% of the Data Center. SLE = EF * AV
  + SLE = $2660329,98
+ Calculate the ALE. Explain and justify your method:
  + ALE = SLE * ARO. SLE is the value lost in the worst case scenario and ARO the Annualized Rate of Occurrence. 
  + ALE = $6650823.45

###### For the best case scenario:

+ Determine the AV, EF, and ARO. Justify your reasoning:
  + EF = 15% AV = $8,867,766,60 ARO = 0.1666666
  + 15% of the data center will be compromised due to the flooding (EF)
+ Calculate the SLE. Explain and justify your method:
  + SLE is calculated by assuming total loss of the 30% of the Data Center. SLE = EF * AV
  + SLE = $1330164,99
+ Calculate the ALE. Explain and justify your method.
  + ALE = SLE * ARO. SLE is the value lost in the worst case scenario and ARO the Annualized Rate of Occurrence. 
  + ALE = $21282639.84

###### For the most likely scenario:

+ Determine the AV, EF, and ARO. Justify your reasoning:
  + EF = 22.5% AV = $8,867,766,60 ARO = 0.2
  + 22.5% of the data center will be compromised due to the flooding (EF)
+ Calculate the SLE. Explain and justify your method:
  + SLE is calculated by assuming total loss of the 22.5% of the Data Center. SLE = EF * AV
  + SLE = $19952474,85
+ Calculate the ALE. Explain and justify your method:
  + ALE = SLE * ARO. SLE is the value lost in the worst case scenario and ARO the Annualized Rate of Occurrence. 
  + ALE = $3990494.97

###### Create a table in your Google Doc submission of the calculated values for all three scenarios. Convert and present the monetary figures in USD for all fields of the table, and include the conversion rate used:

| Value                      | Worst Case        | Most Likely       | Best Case         |
| -------------------------- | ----------------- | ----------------- | ----------------- |
| EF                         | 30%               | 22.5%             | 15%               |
| AV                         | $8,867,766,60     | $8,867,766,60     | $8,867,766,60     |
| ARO                        | 0.25              | 0.2               | 0.16              |
| SLE                        | $2660329,98       | $19952474,85      | $1330164,99       |
| ALE                        | $6650823.45       | $3990494.97       | $21282639.84      |
| BTC to USD conversion rate | 1 BTC = $58710,00 | 1 BTC = $58710,00 | 1 BTC = $58710,00 |