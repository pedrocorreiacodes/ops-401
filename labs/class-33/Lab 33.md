## Lab 33

#### Part 2: Active Countermeasures Labs

------

##### Complete all five of the Active Countermeasures Threat Hunting Labs.

##### Take notes as you work through the AC lab segments. Document your experiences in your submission today.

###### Lab 01 Long Connections

Open your pcap in Wireshark. An load the `.pcap` file in the main window. Select the TCP tab and sort by clicking on the Duration column. Click it again to sort in decreasing order.

![Screenshot 2022-01-26 at 16.40.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2016.40.15.png)

We can also check for UDP connection by selecting the UDP tab:

![Screenshot 2022-01-26 at 16.41.03](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2016.41.03.png)

With Zee (running on a Kali machine):

![Screenshot 2022-01-26 at 18.04.08](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2018.04.08.png)

###### Lab 02 Beacons

The goal is to identify command & control (C2) sessions using regular connection between two IP addresses.

Apply the filter `ip.src==192.168.88.2 && ip.dst==165.227.88.15`. Inside the preferences, click the + button to add a new item and make it match the entry shown below with “Time Delta” for the title and “frame.time_delta_displayed” in the Fields column. You need to double-click inside the box to edit the values. ( This adds a new column that contains the difference in times between each packet and the previous one.)

![Screenshot 2022-01-26 at 18.55.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2018.55.50.png)

![Screenshot 2022-01-26 at 18.56.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2018.56.29.png)

This shows that the IP `192.168.88.2` was communicating with `165.227.88.15` consistently on a 1 second interval. Meaning that there's poossibly beaconing going on..

We can use the command line equivalent of Wireshark **Tshark** to process pcaps and pull out different fields using its protocols dissectors. This is useful if we want to use other tools to manipulate the data

`tshark -r sample.pcap -T fields -e ip.src -e ip.dst -e udp.dstport -e frame.time_delta_displayed 'ip.src==192.168.88.2 && ip.dst==165.227.88.15' | head -25`

We can use also the following command to output all the packet size and the time intervals to a csv file:

`tshark -r sample.pcap -T fields -E separator=, -e ip.len -e frame.time_delta_displayed 'ip.src==192.168.88.2 && ip.dst==165.227.88.15' > sample.csv`

![Screenshot 2022-01-26 at 19.06.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.06.58.png)

open the file in a spreadsheet program and calculate some basic statistic using the following formulas:

![Screenshot 2022-01-26 at 19.11.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.11.52.png)

![Screenshot 2022-01-26 at 19.10.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.10.57.png)

###### Lab 03 DNS

Levarage frequency analysis to identify systems using DNS for C2.

Many command & control (C2) channels communicate directly with an attacker-controlled system. This makes it easier to detect and track down. DNS based C2 is different as the communication utilizes the DNS infrastructure to communicate instead.

We can ask the recursive name server for a server's A record:

![Screenshot 2022-01-26 at 19.18.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.18.36.png)

This time an answer was provided because your local resolver made the recursive calls for you. If we try the first command again with the +norecurse flag we’ll see that the answer is now cached:

![Screenshot 2022-01-26 at 19.22.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.22.13.png)

Here we're inspecting Zeek's dns logs:

![Screenshot 2022-01-26 at 19.24.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.24.26.png)

We can use Tshark to pull DNS queries directly out of a PCAP file on our computer:

![Screenshot 2022-01-26 at 19.30.04](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.30.04.png)

###### Lab 04 Outliers

Identify systems with supeciciouly high or low metrics in different areas. These outliers can then be used to dig into further with other type of analysis

Advanced techniques look at how long connections are held open or how regular conections are being made between two IP addresses. Sometimes it is useful to simply see how many total connection were made. A higher number of coonnections made indicates that systems were communicating quite a bit and this type of analysis can be used to determine where to dig further.

We can use zeek with:

`cat conn.log | zeek-cut id.orig_h id.resp_h id.resp_p proto | awk 'BEGIN{ FS="\t" } { arr[$1 FS $2 FS $3 FS $4] += 1 } END{ for (key in arr) printf "%s%s%s\n", key, FS, arr[key] }' | sort -nrk 5 | head`

![Screenshot 2022-01-26 at 19.34.03](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-33/Screenshot%202022-01-26%20at%2019.34.03.png)

From the results we can see that `192.168.88.2` was communicating with `165.227.88.15` a large number of times. The dataset used is taken over a period of 24 hours so we can see that 108,856 connections divided by 86,400 seconds in a day means over 1 connection was sent every second on average. Furthermore, we know that these connections were made over UDP port 53, which is normally DNS. Typically, DNS results are cached in a number of places including:

- operating system’s local cache
- local or remote DNS recursive resolver
