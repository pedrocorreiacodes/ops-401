## Lab 11

### Part 1: Staging Splunk

------

#### Create a new Splunk account

##### Ensure you select the software version of Splunk **NOT** cloud.

![Screenshot 2021-12-13 at 20.41.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-13%20at%2020.41.30.png)

##### Select Linux as the software download platform with the **.deb** package file.

![Screenshot 2021-12-13 at 21.15.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-13%20at%2021.15.15.png)

#### Set up a new Ubuntu Server VM in VirtualBox.

#####  Allocate at least 60 GB for the virtual hard disk.

![Screenshot 2021-12-13 at 21.17.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-13%20at%2021.17.53.png)

![Screenshot 2021-12-13 at 21.19.15](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-13%20at%2021.19.15.png)

##### Allocate at least 4 GB for memory.

![Screenshot 2021-12-13 at 21.18.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-13%20at%2021.18.33.png)

##### Install to the virtual hard disk.

![Screenshot 2021-12-14 at 13.48.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2013.48.51.png)

##### Set the network adapter to Bridge Mode. You’ll want to access the web portal via your immediate web browser for the least latency.

![Screenshot 2021-12-14 at 14.20.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2014.20.09.png)

#### Launch the VM and identify its IP address.

![Screenshot 2021-12-14 at 14.40.40](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2014.40.40.png)

#### Transfer the .deb Splunk file on to your Ubuntu Server.

![Screenshot 2021-12-14 at 15.08.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2015.08.33.png)

![Screenshot 2021-12-14 at 15.23.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2015.23.59.png)

##### Install Splunk with this command `sudo dpkg -i FILE_NAME.deb`.

![Screenshot 2021-12-14 at 16.18.07](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2016.18.07.png)

##### Access the VM by opening a web browser to `http://ipaddress:8000` where `ipaddress` is replaced with the VM’s IP address.

After running `sudo find / -type f -name splunk`to find out where splunk is installed we can go to that directoy and run `sudo ./splunk start`to start the splunk service:

![Screenshot 2021-12-14 at 17.14.09](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.14.09.png)

Now we can access the web portal from the browser:

![Screenshot 2021-12-14 at 17.15.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.15.33.png)

And login with the credentials used when setting up Splunk from the CLI:

![Screenshot 2021-12-14 at 17.16.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.16.32.png)

##### Follow the directions to upload Splunk tutorial data to the default index.

Click **Add Data**:

![Screenshot 2021-12-14 at 17.20.25](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.20.25.png)

At the bottom of the window, click **Upload**:

![Screenshot 2021-12-14 at 17.21.06](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.21.06.png)

Under **Select Source**, click **Select File**:

![Screenshot 2021-12-14 at 17.21.41](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.21.41.png)

In the download directory, select the `tutorialdata.zip` file and click **Open** (you have to previously download the [tutorial data](http://docs.splunk.com/Documentation/Splunk/8.1.0/SearchTutorial/Aboutthetutorialdata). Click **Next** to continue to **Input Settings**:

![Screenshot 2021-12-14 at 17.28.39](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.28.39.png)

Select **Segment in path**. Type `1` for the segment number:

![Screenshot 2021-12-14 at 17.30.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.30.52.png)

Click **Review** and **Submit** to add the data:

![Screenshot 2021-12-14 at 17.31.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.31.37.png)

Now let's confirm by seeing the data on the Search app, click **Start Searching**. You might see a screen asking if you want to take a tour. You can take the tour or click **Skip**. The Search app opens and a search is automatically run on the tutorial data source.

![Screenshot 2021-12-14 at 17.33.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.33.13.png)

### Part 2: Incident and Analysis

------

Complete the official [Splunk Search Tutorial](https://docs.splunk.com/Documentation/Splunk/8.1.0/SearchTutorial/WelcometotheSearchTutorial). For each component of the lab tutorial, create notes in your submission including screenshots of successful execution of today’s tutorial.

#### Part 3: Using the Splunk Search App

In this part we explore the **Search Summary View** and **New Search view**:

![Screenshot 2021-12-14 at 17.41.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.41.42.png)

![Screenshot 2021-12-14 at 17.42.26](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.42.26.png)

And how to restrict, or filter,your search criteria using a time range. The easiest and most effective way to optimize searches:

![Screenshot 2021-12-14 at 17.44.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.44.50.png)

We can select preset time ranges:

![Screenshot 2021-12-14 at 17.46.14](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.46.14.png)

And custom time ranges

![Screenshot 2021-12-14 at 17.47.05](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.47.05.png)

##### Part 4: Searching the tutorial data

This section shows that we can create searches that retrieve events from the index.

![Screenshot 2021-12-14 at 17.49.31](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2017.49.31.png)

To retrieve events that mention errors or failures, you type the keywords in your search criteria. If you use multiple keywords, you must specify Boolean operators such as AND, OR, and NOT.

![Screenshot 2021-12-14 at 18.19.36](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2018.19.36.png)

Changing the display of the Events viewer to **List**:

![Screenshot 2021-12-14 at 18.26.38](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2018.26.38.png)

Searching with fields:

![Screenshot 2021-12-14 at 18.45.35](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2018.45.35.png)

Running targeted searches:

![Screenshot 2021-12-14 at 18.49.51](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2018.49.51.png)

Using the `top` command to organize the search results into a table.

![Screenshot 2021-12-14 at 19.00.06](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.00.06.png)

Viewing and formatting results on the Visualization tab:

![Screenshot 2021-12-14 at 19.04.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.04.44.png)

Searching with a subsearch:

![Screenshot 2021-12-14 at 19.08.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.08.57.png)

##### Part 5: Enriching events with lookups

Updloading the `Prices.csv.zip`file:

![Screenshot 2021-12-14 at 19.14.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.14.32.png)

Adding the field lookup definition:

![Screenshot 2021-12-14 at 19.17.40](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.17.40.png)

Making the lookup automatic:

![Screenshot 2021-12-14 at 19.23.35](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.23.35.png)

Displaying product names and prices:

![Screenshot 2021-12-14 at 19.30.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.30.52.png)

#### Part 6: Creating reports and charts

Creating and saving a report:

![Screenshot 2021-12-14 at 19.35.12](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.35.12.png)

Creating a basic chart:

![Screenshot 2021-12-14 at 19.40.54](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.40.54.png)

Creating a report from a custom chart:

![Screenshot 2021-12-14 at 19.42.50](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2019.42.50.png)

#### Part 7: Creating dashboards

*Dashboards are views that are made up of panels. The panels can contain modules such as search boxes, fields, charts, tables, and lists. Dashboard panels are usually connected to reports.*

Creating a new Dashboard:

![Screenshot 2021-12-14 at 20.00.22](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2020.00.22.png)

![Screenshot 2021-12-14 at 20.00.57](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-11/Screenshot%202021-12-14%20at%2020.00.57.png)

### Part 3: Reporting

------

#### Why would a security team benefit from SIEM implementation?

With a SIEM implementation a small security team can scale to protect massive enterprises. A SIEM collect logs and other data from sustems and security solutions an gather it all into a single centralized place.

The data collected by a SIEM comes from a number of different systems and can be in several different formats. In order to perform comparison and anylises a SIEM will aggregate and normalize the data.

SIEM solutions can also look for indications of cybersecurity threats in the data. Both by looking for predefined issue outlined in polices and for other potential indications of attack detecting using known patterns.

A SIEM solution can also detect a cybersecurity threat, it notifies an organization's security team through a SIEM alert and may take advantage of integration with ticketing and bug reporting systems or messaging application.

#### What is an index?

The repository for data. Indexes reside in flat files on the Indexer.

When Spunk indexes raw data it transforms the data into searchable events.

There are two types of indexes:

+ Event indexes: The default type of index. They can hold any data.
+ Metric indexes: Metric indexes hold only metric data.

#### What is a forwarder?

Forwarder provide data collection from different sources and deliver data to Splunk for indexing and analysis. The are several types of forwarder but the most common is the universal forwarder, a small footprint agent, installed directly on an endpoint.

#### How does a SIEM add value to an organization like Buttercup Games?

A SIEM solution acts like a central clearinghouse for all cybersecurity data within an organization's network. It's vital to perform several crucail security functions like Threat Detection and Analysis. Forensics and Threat Hunting Support and Regulartory Compliance since a SIEM solution can help demonstrate regulatory complicance because the data that they collect and store can demonstrate that required security controls and policis are in-place and enforced and that a company has not experienced any reportable security incidents.
