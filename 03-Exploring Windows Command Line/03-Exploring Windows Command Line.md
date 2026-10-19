# CC 101 Laboratory Activity: Exploring the Windows Command Line

**Republic of the Philippines**  
**Sorsogon State University**  
**COLLEGE OF INFORMATION AND COMMUNICATIONS TECHNOLOGY**  
Bulan Campus | Zone 8, Bulan, Sorsogon  
Tel. No.: 056 311-0103; Email Address: cict@sorsu.edu.ph  

---

## Student Details
* **Student Name:** Mica Rose D. Merjudio
* **Student ID:** 26118302
* **Course & Section:** BSCS 1-1
* **Date:** 09/23/26
* **Instructor:** Prof. John Mark Gabrentina

---

## Activity Details

| Item | Details |
| :--- | :--- |
| **Course** | CC 101 Introduction to Computing (BSCS 1st Year) |
| **Course Outcome** | CO2: Identify the functions and relationships of major hardware and software components |
| **Output** | Command Line Exploration Documentation (PDF) |
| **Estimated Time** | 2 to $2\frac{1}{2}$ hours |
| **Reference** | CC 101 Lecture Notes: Exploring the Windows Command Line |

---

## Instructions

Follow every step in order, take the screenshots marked `[Screenshot]`, and answer the questions marked `[Answer]` in your documentation.

### Before You Start
* You need a Windows 10 or 11 computer. No administrator rights are needed.
* To take a screenshot, press `Windows + Shift + S`, drag over the terminal window, then paste it (`Ctrl + V`) into your documentation.
* Replace the sample values (*Juan Dela Cruz, BSCS 1-1*) with your own details.
* Type every command yourself. Do not copy and paste; typing is how you learn.

---

## Part A: Open the Two Shells

1. Press `Windows + R`, type `cmd`, and press Enter. Type `cls` and press Enter.
2. Type `echo Mica Rose Merjudio, BSCS 1-1` and press Enter.  
   `[Screenshot] Figure A1`

```cmd
Microsoft Windows [Version 10.0.26200.9457]
(c) Microsoft Corporation. All rights reserved.

C:\Users\merju>echo Mica Rose Merjudio, BSCS 1-1
Mica Rose Merjudio, BSCS 1-1

C:\Users\merju>
```

3. Press `Windows + R`, type `powershell`, and press Enter. Type the same echo command, but put the text in quotation marks: `echo "Mica Rose Merjudio, BSCS 1-1"`. PowerShell treats the comma as a list separator without them.  
   `[Screenshot] Figure A2`

```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\merju> echo "Mica Rose Merjudio, BSCS 1-1"
Mica Rose Merjudio, BSCS 1-1
PS C:\Users\merju>
```

### Questions & Answers

* **[Answer] A-Q1. Compare the two prompts. What is different, and what does each part of the Command Prompt prompt mean?**  
  > The main difference between the two prompts is that PowerShell includes the prefix `PS` at the beginning (e.g., `PS C:\Users\merju>`), whereas Command Prompt shows only the directory path (e.g., `C:\Users\merju>`), where `C:` represents the current drive letter, `\Users\merju` indicates the active folder path, and the `>` symbol signifies that the system is ready for user input.

---

## Part B: Inspect Your System (Command Prompt)

*Use the Command Prompt window for Parts B to D.*

1. Run these commands one at a time: `whoami`, then `hostname`, then `ver`.  
   `[Screenshot] Figure B1`

```cmd
C:\Users\merju>whoami
laptop-dq5p6j7t\merju

C:\Users\merju>hostname
LAPTOP-DQ5P6J7T

C:\Users\merju>ver
Microsoft Windows [Version 10.0.26200.9457]

C:\Users\merju>
```

2. Run the command below. It may take 10 to 30 seconds.  
   `[Screenshot] Figure B2`

```cmd
C:\Users\merju>systeminfo | findstr /B/C:"OS Name" /C:"OS Version" /C:"System Type" /C:"Total Physical Memory"
OS Name:                   Microsoft Windows 11 Home Single Language
OS Version:                10.0.26200 N/A Build 26200
System Type:               x64-based PC
Total Physical Memory:     7,916 MB
```

3. Run `ipconfig`. Find the adapter that shows an IPv4 Address.  
   `[Screenshot] Figure B3`

```cmd
C:\Users\merju>ipconfig

Windows IP Configuration

Wireless LAN adapter Local Area Connection* 3:
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Local Area Connection* 4:
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:
   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::deb:24c4:efc0:5655%9
   IPv4 Address. . . . . . . . . . . : 192.168.1.60
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::1%9
                                       192.168.1.1

Ethernet adapter Bluetooth Network Connection:
   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
```

### Questions & Answers

* **[Answer] B-Q1. Complete this table in your documentation using your results:**

| Item | Your result |
| :--- | :--- |
| **Logged-in account (whoami)** | `laptop-dq5p6j7t\merju` |
| **Computer name (hostname)** | `LAPTOP-DQ5P6J7T` |
| **OS name** | `Microsoft Windows 11 Home Single Language` |
| **OS version** | `10.0.26200 N/A Build 26200` |
| **System type (x64 or ARM)** | `x64-based PC` |
| **Total physical memory (RAM)** | `7,916 MB` |
| **IPv4 address** | `192.168.1.60` |

* **[Answer] B-Q2. The `|` symbol in step 2 is called a pipe. Run `systeminfo` alone and compare. In your own words, what did `| findstr` do?**  
  > Running `systeminfo` by itself displays a very long list containing all hardware and software details about the computer. The `|` symbol acts as a pipe that takes this huge output and sends it directly into the `findstr` tool. The `findstr` command then filters through every single line of text to search for specific keyword matches. As a result, it only prints the exact requested details on the screen while hiding the rest of the unneeded information.

---

## Part C: Build a Folder Structure

1. Go to your user folder and create the lab folders:

```cmd
C:\Users\merju>cd "Mica Rose Merjudio, BSCS 1-1"
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1>mkdir CC101-Lab
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1>cd CC101-Lab
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>mkdir Notes Projects Screenshots
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>
```

2. Create a text file about yourself:  
   `[Screenshot] Figure C1`

```cmd
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>echo Name: Mica Rose Merjudio > profile.txt
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>echo Section: BSCS 1-1 >> profile.txt
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>echo Favorite app: YouTube >> profile.txt
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>type profile.txt
Name: Mica Rose Merjudio
Section: BSCS 1-1
Favorite app: YouTube
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>
```

3. Run `tree /F` to display your folder structure.  
   `[Screenshot] Figure C2`

```cmd
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>tree /F
Folder PATH listing for volume Windows
Volume serial number is 0E59-66A1
C:.
│   profile.txt
│
├───Notes
├───Projects
└───Screenshots
```

4. Open File Explorer, go to `C:\Users\(your account)\CC101-Lab`, and open `profile.txt` in Notepad.  
   `[Screenshot] Figure C3 (File Explorer and Notepad side by side)`

### Questions & Answers

* **[Answer] C-Q1. What would happen if you used `>` instead of `>>` in the second echo line? Test it on a new file (`test.txt`) and explain.**  
  > The `>` symbol is a redirection operator that completely overwrites any existing content inside a file. If you use `>` on the second line instead of `>>`, it will wipe out the first line containing your name. Testing this on `test.txt` shows that only the most recently typed line remains in the document. On the other hand, using `>>` properly appends new lines to the end of the file without deleting previous data.

---

## Part D: Copy, Rename, and Delete Files

1. Execute file operation commands:  
   `[Screenshot] Figure D1 (from copy to the first dir)`

```cmd
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>copy profile.txt Notes\profile-copy.txt
        1 file(s) copied.

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>cd Notes

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes>ren profile-copy.txt about-me.txt

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes>echo This file will be deleted > temp.txt

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes>dir
 Volume in drive C is Windows
 Volume Serial Number is 0E59-66A1

 Directory of C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes

23/09/2026  05:52 PM    <DIR>          .
23/09/2026  05:47 PM    <DIR>          ..
23/09/2026  05:48 PM                71 about-me.txt
23/09/2026  05:52 PM                28 temp.txt
               2 File(s)             99 bytes
               2 Dir(s)  67,310,940,160 bytes free
```

2. Delete temporary file and inspect directory tree:  
   `[Screenshot] Figure D2 (from del to tree /F)`

```cmd
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes>del temp.txt

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes>dir
 Volume in drive C is Windows
 Volume Serial Number is 0E59-66A1

 Directory of C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes

23/09/2026  05:52 PM    <DIR>          .
23/09/2026  05:47 PM    <DIR>          ..
23/09/2026  05:48 PM                71 about-me.txt
               1 File(s)             71 bytes
               2 Dir(s)  67,310,858,248 bytes free

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab\Notes>cd ..

C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>tree /F
Folder PATH listing for volume Windows
Volume serial number is 0E59-66A1
C:.
│   profile.txt
│
├───Notes
│       about-me.txt
│
├───Projects
└───Screenshots
```

### Questions & Answers

* **[Answer] D-Q1. After `del temp.txt`, check your Recycle Bin. Is `temp.txt` there? What does this tell you about deleting files from the command line?**  
  > Checking the Recycle Bin after running `del temp.txt` reveals that the deleted file is nowhere to be found. This happens because the command line removes files directly from the storage drive instead of sending them to a temporary trash location. Graphical user interfaces protect users by holding deleted items in the Recycle Bin for easy recovery. Therefore, deleting files via Command Prompt is permanent and requires extra caution before executing the command.

---

## Part E: Explore PowerShell

*Switch to the PowerShell window.*

1. Go to your lab folder and list and read its files:  
   `[Screenshot] Figure E1`

```powershell
PS C:\Users\merju> cd $HOME\CC101-Lab
PS C:\Users\merju\CC101-Lab> Get-ChildItem

    Directory: C:\Users\merju\CC101-Lab

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       23/09/2026   6:00 PM                Notes
d-----       23/09/2026   6:00 PM                Projects
d-----       23/09/2026   6:00 PM                Screenshots
-a----       23/09/2026   6:02 PM            138 profile.txt

PS C:\Users\merju\CC101-Lab> Get-Content profile.txt
Name: Mica Rose Merjudio
Section: BSCS 1-1
Favorite app: YouTube

PS C:\Users\merju\CC101-Lab> $PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.26100.9444
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.26100.9444
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

2. Run `Get-Help Get-ChildItem`.  
   `[Screenshot] Figure E2`

```powershell
PS C:\Users\merju\CC101-Lab> Get-Help Get-ChildItem
NAME
    Get-ChildItem

SYNTAX
    Get-ChildItem [[-Path] <string[]>] [[-Filter] <string>] 
    [-Include <string[]>] [-Exclude <string[]>] [-Recurse] [-Depth 
    <uint32>] [-Force] [-Name] [-UseTransaction] [-Attributes 
    {ReadOnly | Hidden | System | Directory | Archive | Device | 
    Normal | Temporary | SparseFile | ReparsePoint | Compressed | 
    Offline | NotContentIndexed | Encrypted | IntegrityStream | 
    NoScrubData}] [-FollowSymlink] [-Directory] [-File] [-Hidden] 
    [-ReadOnly] [-System] [<CommonParameters>]

    Get-ChildItem [[-Filter] <string>] -LiteralPath <string[]> 
    [-Include <string[]>] [-Exclude <string[]>] [-Recurse] [-Depth 
    <uint32>] [-Force] [-Name] [-UseTransaction] [-Attributes 
    {ReadOnly | Hidden | System | Directory | Archive | Device | 
    Normal | Temporary | SparseFile | ReparsePoint | Compressed | 
    Offline | NotContentIndexed | Encrypted | IntegrityStream | 
    NoScrubData}] [-FollowSymlink] [-Directory] [-File] [-Hidden] 
    [-ReadOnly] [-System] [<CommonParameters>]

ALIASES
    gci
    ls
    dir

REMARKS
    Get-Help cannot find the Help files for this cmdlet on this 
    computer. It is displaying only partial help.
    -- To download and install Help files for the module that 
       includes this cmdlet, use Update-Help.
    -- To view the Help topic for this cmdlet online, type:
       "Get-Help Get-ChildItem -Online" or
       go to https://go.microsoft.com/fwlink/?LinkID=113308.
```

3. Base Conversion using last 3 digits of Student ID (`302`):  
   `[Screenshot] Figure E3`

```powershell
PS C:\Users\merju\CC101-Lab> [Convert]::ToString(302, 2)
100101110

PS C:\Users\merju\CC101-Lab> [Convert]::ToString(302, 8)
456

PS C:\Users\merju\CC101-Lab> '{0:X}' -f 302
12E
```

### Questions & Answers

* **[Answer] E-Q1. Write your number in decimal, binary, octal, and hexadecimal.**  
  > * **Decimal:** `302`  
  > * **Binary:** `100101110`  
  > * **Octal:** `456`  
  > * **Hexadecimal:** `12E`  

---

## Part F: Discover a New Command

1. In Command Prompt, read command help with `vol /?`:  
   `[Screenshot] Figure F1`

```cmd
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>vol /?
Displays the disk volume label and serial number, if they exist.

VOL [drive:]
```

2. Execute the command `vol`:  
   `[Screenshot] Figure F2`

```cmd
C:\Users\merju\Mica Rose Merjudio, BSCS 1-1\CC101-Lab>vol
 Volume in drive C is Windows
 Volume Serial Number is 0E59-66A1
```

### Questions & Answers

* **[Answer] F-Q1. What does your chosen command do, and when would it be useful?**  
  > The `vol` command is a built-in tool used to display the volume label and serial number of a disk drive. Running this command instantly shows the identity of the current working partition without needing extra settings. It is especially useful when managing multiple storage devices or troubleshooting drive connections. System administrators often use it to quickly verify disk information before executing drive-related scripts.

---

## Part G: Reflection

* **[Answer] G-Q1. Which task in this activity was faster in the CLI than in the GUI? Which was easier in the GUI? Explain why.**  
  > Creating several folders at once using `mkdir` and running base conversions in PowerShell were much faster in the CLI than in the GUI. On the other hand, viewing the folder tree and opening text files side by side was much easier using the GUI. The CLI saves a lot of time because it executes precise text commands instantly without needing repetitive mouse clicks. Meanwhile, the GUI is more convenient for visual tasks because it displays files and options clearly on the screen.

* **[Answer] G-Q2. What error did you encounter (if any), what caused it, and how did you fix it?**  
  > An error occurred earlier when running commands with folder paths that contained spaces without proper quotes. The terminal got confused and treated the spaces as separate arguments instead of one continuous path. This issue was fixed by placing double quotation marks around the entire folder path so PowerShell could read it correctly. This experience showed how important exact syntax and proper formatting are when typing commands in the terminal.

* **[Answer] G-Q3. Give one real-world job or situation in computing where knowing the command line would be important.**  
  > System administrators and IT support professionals rely heavily on the command line when managing network servers remotely. Many cloud servers operate without a graphical interface, making terminal commands the only way to interact with them. Using the CLI allows these professionals to run automated scripts, deploy software updates, and fix system issues quickly across many machines. Learning these commands is essential for anyone who wants to work in cybersecurity, network management, or software development.

---

## Commands Learned Table

| Command | Shell | What it does |
| :--- | :--- | :--- |
| `cls` | Command Prompt | Clears the terminal screen. |
| `echo` | Command Prompt / PowerShell | Prints text to the screen or redirects it to a file. |
| `whoami` | Command Prompt | Displays the currently logged-in user account. |
| `hostname` | Command Prompt | Shows the host name of the computer. |
| `ver` | Command Prompt | Displays the version of the operating system. |
| `systeminfo` | Command Prompt | Displays detailed configuration information about the computer and OS. |
| `findstr` | Command Prompt | Searches for specific strings of text in files or command outputs. |
| `ipconfig` | Command Prompt | Displays all current TCP/IP network configuration values. |
| `cd` | Command Prompt / PowerShell | Changes the current working directory. |
| `mkdir` | Command Prompt / PowerShell | Creates a new directory/folder. |
| `type` | Command Prompt | Displays the contents of a text file. |
| `tree /F` | Command Prompt | Graphically displays the directory structure of a path, including files. |
| `copy` | Command Prompt | Copies one or more files to another location. |
| `ren` | Command Prompt | Renames a file or directory. |
| `del` | Command Prompt | Deletes one or more files permanently. |
| `Get-ChildItem` | PowerShell | Gets the items and child items in one or more specified locations (similar to `dir`). |
| `Get-Content` | PowerShell | Reads and displays the content of the file specified. |
| `$PSVersionTable` | PowerShell | Displays information about the current PowerShell version. |
| `Get-Help` | PowerShell | Displays help and documentation for PowerShell commands. |
| `vol` | Command Prompt | Displays the disk volume label and serial number. |