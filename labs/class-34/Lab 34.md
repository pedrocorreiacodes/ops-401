## Lab 34

### Part 1: Staging

------

#### You will need FLARE VM for this lab.

![Screenshot 2022-01-27 at 16.51.58](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2016.51.58.png)

### Part 2: Investigating with Autopsy

------

#### Complete at least three different scenarios using Autopsy.

**Fat Volume Test Label #1**

1. Does the analysis tool display the volume label for the image? If so, what label does it give?

   ![Screenshot 2022-01-27 at 19.09.27](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.09.27.png)

2. In the file browsing mode of the tool, is the "LABEL2" entry shown?  Can you view its contents?  What is its MD5?

![Screenshot 2022-01-27 at 19.11.59](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.11.59.png)

3.  In the file browsing mode of the tool, is the "dir1/FILE2.DLL" entry shown?  Can you view its contents?  What is its MD5?

    ![Screenshot 2022-01-27 at 19.13.01](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.13.01.png)

![Screenshot 2022-01-27 at 19.13.47](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.13.47.png)

4.  If a keyword search is conducted for the ASCII string "over here", is it found?  At what sector/cluster address is it located?  Does the tool report which file it is allocated to?

![Screenshot 2022-01-27 at 19.15.53](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.15.53.png)

5.  Does the tool have a method of identifying all graphic files? If so, does it find the "dir1/FILE2.DLL" file?

![Screenshot 2022-01-27 at 19.19.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.19.19.png)

**FAT Undelete Image #1**

1.  Can you see the frag1.dat, frag2.dat, sing.dat, mult1.dat, and dir1 file and directory names in the root directory?

    ![Screenshot 2022-01-27 at 19.40.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.40.30.png)

2. Can you see the dir2 and mult2.dat names in the dir1 directory?

   ![Screenshot 2022-01-27 at 19.41.43](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.41.43.png)

3. Can you see the frag3.dat name in the dir1\dir2 directory?

![Screenshot 2022-01-27 at 19.42.29](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.42.29.png)

4. Can you recover the sing.dat file?  Does it have the correct MD5?

   ![Screenshot 2022-01-27 at 19.43.52](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.43.52.png)

![Screenshot 2022-01-27 at 19.44.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.44.13.png)

Same value:

![Screenshot 2022-01-27 at 19.46.42](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.46.42.png)

5. Can you recover the mult1.dat file?  Does it have the correct MD5?

It does have the correct MD5:

![Screenshot 2022-01-27 at 19.50.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.50.11.png)

6.  Can you recover the dir1\mult2.dat file?  Does it have the correct MD5?

    Yes.

    ![Screenshot 2022-01-27 at 19.53.00](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.53.00.png)

7. Can you recover the frag1.dat file?  Does it have the correct MD5?

   Yes:

   ![Screenshot 2022-01-27 at 19.54.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.54.37.png)

8. Can you recover the frag2.dat file?  Does it have the correct MD5?

Yes.

![Screenshot 2022-01-27 at 19.55.55](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.55.55.png)

9. Can you recover the dir1\dir2\frag3.dat file?  Does it have the correct MD5?

   Yes:

   ![Screenshot 2022-01-27 at 19.58.45](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2019.58.45.png)

**JPEG Search Test #1**

![Screenshot 2022-01-27 at 17.01.27](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2017.01.27.png)

Let's select **Add Data Source** and select the `.DD` file for this scenario.

![Screenshot 2022-01-27 at 17.04.17](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2017.04.17.png)

1.  What search procedure(s) were used to obtain the following
    results?

    The following apply to the results from running an automated search
    tool for JPEG pictures.  If more than one procedure was used to
    find the images, please note the procedure that was used to find
    each.  Note that this was not designed to test data carving tools.


2. Did the search results include the alloc\file1.jpg picture?  

Yes the picture was found in the **alloc** folder:

![Screenshot 2022-01-27 at 18.06.11](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.06.11.png)

​	3. Did the search results include the alloc\file2.dat picture?  If not, then is it documented that JPEGs are found using only the extension?

![Screenshot 2022-01-27 at 18.13.32](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.13.32.png)

4. Did the search results include the invalid\file3.jpg file?

![Screenshot 2022-01-27 at 18.14.27](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.14.27.png)

5. Did the search results include the invalid\file4.jpg file?

![Screenshot 2022-01-27 at 18.18.13](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.18.13.png)

6. Did the search results include the invalid\file5.rtf file?

![Screenshot 2022-01-27 at 18.18.44](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.18.44.png)

7. Did the search results include the deleted picture in MFT entry #32 (del1/file6.jpg)?  If not, then is it documented that only allocated JPEGs will be found?

![Screenshot 2022-01-27 at 18.20.23](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.20.23.png)

8. Did the search results include the deleted picture in MFT entry #31 (del2/file7.hmm)?  If this file was not found, but the file in step #7 was found, then is it documented that only JPEGs with a proper extension will be found?

![Screenshot 2022-01-27 at 18.24.33](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.24.33.png)

9. Did the search results include the picture inside of archive\file8.zip? If not, then is it documented that JPEG files will be found and that JPEG images that are embedded inside other file types will not?

![Screenshot 2022-01-27 at 18.25.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.25.30.png)

10. Did the search results include the picture inside of archive\file9.boo?  If not, then is it documented that JPEG files will be found and that JPEG images that are embedded inside other file types will not?

![Screenshot 2022-01-27 at 18.26.37](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.26.37.png)

11. Did the search results include the picture inside of archive\file10.tar.gz?  If not, then is it documented that JPEG files will be found and that JPEG images that are embedded inside other file types will not?

![Screenshot 2022-01-27 at 18.28.10](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.28.10.png)

12. Did the search results include the misc\file11.dat file? If not, then is it documented that JPEG files will be found and that JPEG images that are embedded inside other file types will not?

![Screenshot 2022-01-27 at 18.29.19](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.29.19.png)

13. Did the search results include the misc\file12.doc file?  If not, then is it documented that JPEG files will be found and that JPEG images that are embedded inside other file types will not?

![Screenshot 2022-01-27 at 18.30.30](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.30.30.png)

14. Did the search results include the misc\file13.dll? If not, then is it documented that pictures in alternate data streams will not be found?

![Screenshot 2022-01-27 at 18.31.46](https://github.com/pedrocorreiacodes/ops-401/blob/master/screenshots/class-34/Screenshot%202022-01-27%20at%2018.31.46.png)

### Part 3: Reporting

------

#### How can Autopsy accelerate your ability to find important data on a hard disk image?

Autopsy is a powerful tools. It allows to search by keywords, extract content and provides metadata for all the files such as MD5 hash value

#### Why might the Autopsy timeline view be relevant in an investigation?

Trough the timeline we can have an overview of the events that took place. What happend and when it happened. We can check when something as acessed, deleted and for how long.

#### How does Autopsy compare to manually searching a hard disk in something like Windows Explorer?

Through Autopsy we can serch for deleted files or hidden information in files such as images. 
