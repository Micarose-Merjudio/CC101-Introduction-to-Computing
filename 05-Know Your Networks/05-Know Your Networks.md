# SORSOGON STATE UNIVERSITY
**COLLEGE OF INFORMATION AND COMMUNICATIONS TECHNOLOGY**  
Bulan Campus  
Zone 8, Bulan, Sorsogon  

**CC 101 - Introduction to Computing**  
*"Know Your Network Settings": Exploring Windows 11 Network Configuration Tools*

**Name:** MICA ROSE D. MERJUDIO  
**Block:** BSCS 1-1  
**Computer Unit Used:** LAPTOP, HUAWEI  
**Date:** OCTOBER 14, 2026  
**Instructor:** Prof. John Mark Gabrentina  
**School Year:** 2026-2027  

---

## I. Objectives
At the end of this activity, you should be able to:
* Locate network adapter information using Windows 11 Settings, the Control Panel, Command Prompt (CMD), and PowerShell.
* Use `ipconfig`, `getmac`, `hostname`, `ping`, `netstat`, `route print`, and `systeminfo` in CMD, and `Get-NetAdapter`, `Get-NetIPAddress`, and `Test-Connection` in PowerShell.
* Interpret a sample `ipconfig /all` output from a networked computer: identify its IP address, subnet mask, default gateway, and DNS servers, and classify the address as public or private.
* Relate each tool and finding to the layer of the OSI model where it works.
* Design a simple network and IP address plan for the computer laboratory.

---

## II. Materials Needed
* A computer running Windows 11 (a network or Internet connection is not required for this activity)
* This worksheet (printed copy, or the digital file to fill out and submit)
* Week 6 lecture notes, for reference on IP addresses, protocols, the OSI model, and network devices

---

## III. Background
A computer does not need to be connected to a network to have network settings. Every PC has one or more network adapters (NICs), each with a permanent MAC address, and Windows always runs the TCP/IP software, including the loopback address $127.0.0.1$ (IPv4) and $::1$ (IPv6) that the computer uses to talk to itself. Windows 11 lets you inspect these settings in four places: the Settings app, the classic Control Panel, Command Prompt (CMD), and PowerShell. In this activity, you will explore all four on your own unit, observe how Windows behaves when no network is available, and then analyze a sample configuration taken from a computer that is connected to a network.

---

## IV. Procedure
*Reminder: This is a viewing activity. Do not change, disable, or reset any network setting. Close every dialog with Cancel. Record values exactly as Windows shows them.*

### Part A - Windows 11 Settings
1. Press Windows + I to open Settings, then click Network & internet. Write down the connection status shown at the top of the page (for example, "Not connected").
2. Click Advanced network settings. Under Network adapters, note every adapter listed (for example, Ethernet, Wi-Fi, Bluetooth Network Connection) and whether each one is enabled or disconnected.
3. Scroll down and click Hardware and connection properties. For each adapter, record its Name, Description, Physical address (MAC), and Status in Table 1.

### Part B - Control Panel (Network Connections)
4. Press Windows + R, type `ncpa.cpl`, and press Enter. This opens the classic Network Connections window. A red X on an icon means the adapter has no network connection.
5. Right-click your Ethernet adapter and choose Properties. List the items checked under "This connection uses the following items" in Table 2.
6. Select Internet Protocol Version 4 $(\text{TCP/IPv4})$ and click Properties. Record whether the computer is set to Obtain an IP address automatically (DHCP) or Use the following IP address (static), and the same for DNS. Click Cancel, then Cancel again. Do not change anything.

### Part C - Command Prompt (CMD)
7. Press the Windows key, type `cmd`, and press Enter. Run each command below, one at a time, and record the results in Table 3.
   * `hostname`
   * `getmac /v`
   * `ipconfig /all`  
   *Tip: For a disconnected adapter, `ipconfig /all` shows "Media disconnected" and no IPv4 address, but it still shows the Description and Physical Address.*
8. Test the computer's own TCP/IP software using the loopback address. Record whether you got replies and the time. For `ping localhost`, note the address that replied.
   * `ping 127.0.0.1`
   * `ping localhost`
9. Now observe what happens when there is no network. Record the exact message each command displays.
   * `ping 8.8.8.8`
   * `nslookup google.com`
10. View the ports your computer is listening on and its routing table. In Table 3, record three LISTENING local addresses with their port numbers, and the Netmask shown for the Network Destination $127.0.0.0$.
    * `netstat -an | findstr LISTENING`
    * `route print -4`
11. Run the command below. It may take a few seconds. Scroll to Network Card(s) and record how many network cards are installed and the status of each.
    * `systeminfo`

### Part D - PowerShell
12. Right-click the Start button and choose Terminal (or press the Windows key, type PowerShell, and press Enter). Run each command below and record the results in Table 4.
    * `Get-NetAdapter`
    * `Get-NetIPAddress -AddressFamily IPv4 | Format-Table InterfaceAlias, IPAddress, PrefixLength`
    * `Test-Connection 127.0.0.1 -Count 4`
    * `Get-NetTCPConnection -State Listen | Select-Object -First 5 LocalAddress, LocalPort`  
    *Tip: PowerShell commands follow a Verb-Noun pattern (`Get-NetAdapter` = "get the network adapters"). Compare each result with the matching CMD command from Part C.*

### Part E - Analyze a Networked Computer
13. The output below was taken from a laboratory computer that is connected to a network. Study it, then complete Table 5.

```text
Sample Output 1. ipconfig /all (excerpt) from a networked PC

Host Name . . . . . . . . . . . . : CICT-LAB-PC07
Ethernet adapter Ethernet:
   Description . . . . . . . . . . : Realtek PCIe GbE Family Controller
   Physical Address. . . . . . . . : 3C-52-82-A1-7F-09
   DHCP Enabled. . . . . . . . . . : Yes
   Link-local IPv6 Address . . . . : fe80::8c2d:4a1f:93b2:61e5%12(Preferred)
   IPv4 Address. . . . . . . . . . : 192.168.10.37 (Preferred)
   Subnet Mask . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . : Wednesday, October 14, 2026 8:02:15 AM
   Lease Expires . . . . . . . . . : Thursday, October 15, 2026 8:02:15 AM
   Default Gateway . . . . . . . . : 192.168.10.1
   DHCP Server . . . . . . . . . . : 192.168.10.1
   DNS Servers . . . . . . . . . . : 192.168.10.1, 8.8.8.8
```

### Part F - Design a Network for Our Laboratory
14. Our laboratory does not yet have a network. Draw a simple star topology network for it. Include at least four PCs, one switch, one router (default gateway), one printer, and the ISP / Internet. Use lines to show connections.
15. Assign each device a private IPv4 address from the network $192.168.10.0/24$, using $192.168.10.1$ for the router. Label each device in your drawing and complete the IP Address Plan (Table 6).

### Part G - Optional / Bonus
16. In CMD, run `type C:\Windows\System32\drivers\etc\hosts` to view (not edit) the hosts file. In one or two sentences, explain what this file is for and how it relates to DNS.

---

## V. Data and Findings

### Table 1. Network Adapters in Settings (Part A)
**Connection status shown on the Network & internet page:** Connected

| Adapter Name | Description | Physical Address (MAC) | Status |
| --- | --- | --- | --- |
| Local Area Connection* 3 | Microsoft Wi-Fi Direct Virtual Adapter #3 | 8c:e9:ee:e4:23:1c | Not operational |
| Local Area Connection* 4 | Microsoft Wi-Fi Direct Virtual Adapter #4 | 8e:e9:ee:e4:23:1b | Not operational |
| Wi-Fi | Intel(R) Wi-Fi 6 AX201 160MHz | 8c:e9:ee:e4:23:1b | Operational |
| Bluetooth Network Connection | Bluetooth Device (Personal Area Network) | 8c:e9:ee:e4:23:1f | Not operational |

---

### Table 2. Adapter Properties (Part B)

| Items Checked Under "This connection uses the following items" |
| --- |
| Client for Microsoft Networks |
| File and Printer Sharing for Microsoft Networks |
| QoS Packet Scheduler |
| Internet Protocol Version 4 (TCP/IPv4) |
| Microsoft LLDP Protocol Driver |
| Internet Protocol Version 6 (TCP/IPv6) |
| Link-Layer Topology Discovery Responder |
| Link-Layer Topology Discovery Mapper I/O Driver |

| TCP/IPv4 Setting | Automatic or Static? |
| --- | --- |
| IP address | Automatic (DHCP) |
| DNS server address | Automatic (DHCP) |

---

### Table 3. Command Prompt Results (Part C)

| Command/Item | Your Findings | OSI Layer |
| --- | --- | --- |
| `hostname` | LAPTOP-DQ5P6J7T | Application Layer (Layer 7) |
| `getmac /v`: MAC address and Transport Name | Transport name: `\Device\Tcpip_{74AE0F10-A23D-4ABA-82ED-B4819BC226D7}`<br>Media disconnected<br>MAC address: *Didn't show* | Data Link Layer (Layer 2) |
| `ipconfig /all`: Media State of Ethernet | Media disconnected | Data Link Layer (Layer 2) |
| `ipconfig /all`: DHCP Enabled | Yes | Application Layer (Layer 7) |
| `ping 127.0.0.1`: replies and time | Pinging 127.0.0.1 with 32 bytes of data:<br>Reply from 127.0.0.1: bytes=32 time<1ms TTL=128<br>Reply from 127.0.0.1: bytes=32 time<1ms TTL=128<br>Reply from 127.0.0.1: bytes=32 time<1ms TTL=128<br>Reply from 127.0.0.1: bytes=32 time<1ms TTL=128<br><br>Ping statistics for 127.0.0.1:<br>Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),<br>Approximate round trip times in milli-seconds:<br>Minimum = 0ms, Maximum = 0ms, Average = 0ms | Network Layer (Layer 3) |
| `ping localhost`: address that replied | `::1` / `127.0.0.1` | Network Layer (Layer 3) |
| `ping 8.8.8.8`: exact message | Pinging 8.8.8.8 with 32 bytes of data:<br>Reply from 8.8.8.8: bytes=32 time=12ms TTL=116<br>Reply from 8.8.8.8: bytes=32 time=12ms TTL=116<br>Reply from 8.8.8.8: bytes=32 time=12ms TTL=116<br>Reply from 8.8.8.8: bytes=32 time=19ms TTL=116<br><br>Ping statistics for 8.8.8.8:<br>Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),<br>Approximate round trip times in milli-seconds:<br>Minimum = 12ms, Maximum = 19ms, Average = 13ms | Network Layer (Layer 3) |
| `nslookup google.com`: exact message | Server: Unknown<br>Address: fe80::1<br><br>Non-authoritative answer:<br>Name: google.com<br>Addresses:<br>2404:6800:4008:c1b::64<br>2404:6800:4008:c1b::8b<br>2404:6800:4008:c1b::71<br>2404:6800:4008:c1b::8a<br>74.125.24.113<br>74.125.24.101<br>74.125.24.139<br>74.125.24.100<br>74.125.24.138<br>74.125.24.102 | Application Layer (Layer 7) |
| `netstat -an`: three LISTENING addresses:ports | `0.0.0.0:135` LISTENING<br>`0.0.0.0:445` LISTENING<br>`0.0.0.0:5040` LISTENING | Transport Layer (Layer 4) |
| `route print -4`: Netmask for 127.0.0.0 | 255.0.0.0 | Network Layer (Layer 3) |
| `systeminfo`: number of NICs and status | Network Card(s): 2 NIC(s) Installed.<br>[01]: Intel(R) Wi-Fi 6 AX201 160MHz<br>Connection Name: Wi-Fi<br>DHCP Enabled: Yes<br>DHCP Server: 192.168.1.1<br>IP address(es): [01]: 192.168.1.60<br>[02]: fe80::deb:24c4:efc9:5655%9<br>[02]: Bluetooth Device (Personal Area Network)<br>Connection Name: Bluetooth Network Connection<br>Media status: Media disconnected | Network / Data Link Layer |

---

### Table 4. PowerShell Results (Part D)

| Command | What It Showed | Matches CMD? (Y/N) |
| --- | --- | --- |
| `Get-NetAdapter`: Name, Status, MacAddress, LinkSpeed | Name: Wi-Fi, InterfaceDescription: Intel(R) Wi-Fi 6 AX201 160MHz, Status: Up<br>Name: Bluetooth Network Connection, Status: Disconnected | Y |
| `Get-NetIPAddress`: IPv4 addresses and PrefixLength | IPv4 address: 192.168.1.60, PrefixLength: 24<br>(or APIPA: 169.254.166.217, PrefixLength: 16) | Y |
| `Test-Connection 127.0.0.1`: result | Destination: 127.0.0.1, IPv4Address: 127.0.0.1, Response time: <1ms | Y |
| `Get-NetTCPConnection -State Listen`: two LocalAddress:LocalPort pairs | `::1 : 49712`<br>`0.0.0.0 : 135` | Y |

---

### Table 5. Sample Output Analysis (Part E)

| Question | Your Answer |
| --- | --- |
| IPv4 address of PC07 | $192.168.10.37$ (Preferred) |
| Subnet mask (and its /prefix) | $255.255.255.0$ (Prefix: $/24$) |
| Default gateway, and what device it usually is | $192.168.10.1$; it is usually a router (or default gateway router). |
| DNS servers | $192.168.10.1$, $8.8.8.8$ |
| Was the address assigned by DHCP or set manually? How do you know? | Assigned by DHCP. We know this because DHCP Enabled is set to "Yes", and active "Lease Obtained" and "Lease Expires" timestamps are present. |
| Public or private? Which RFC 1918 range? | Private, belonging to the RFC 1918 range $192.168.0.0 - 192.168.255.255$ ($192.168.10.0/24$). |
| IPv4 address of PC07 in binary (four octets) | $11000000.10101000.00001010.00100101$ |
| MAC address, and the OSI layer where it is used. How long is the DHCP lease? | MAC Address: `3C-52-82-A1-7F-09`, used at the Data Link Layer (Layer 2).<br>DHCP Lease Length: 24 hours (1 day), from October 14, 2026, 8:02:15 AM to October 15, 2026, 8:02:15 AM. |
| If the DHCP server failed, what kind of address would PC07 assign itself? | An APIPA (Automatic Private IP Addressing) address, which falls under the $169.254.x.x$ link-local range. |

---

### Part F - Proposed Laboratory Network Diagram & IP Plan

```
                   INTERNET SERVICE PROVIDER (ISP)
                                 |
                                 |
                          [ ROUTER ] (192.168.10.1)
                                 |
                                 |
                        [ CENTER SWITCH ]
                   /     /             \     \
                  /     /               \     \
            [ PC 1 ]  [ PC 2 ]      [ PC 3 ]  [ PC 4 ]     [ PRINTER ]
          .10       .12           .18       .21          .22
```

#### Table 6. IP Address Plan (Part F)

| Device | IPv4 Address | Subnet Mask | Default Gateway |
| --- | --- | --- | --- |
| Router (gateway) | $192.168.10.1$ | $255.255.255.0$ | N/A |
| PC 1 | $192.168.10.10$ | $255.255.255.0$ | $192.168.10.1$ |
| PC 2 | $192.168.10.12$ | $255.255.255.0$ | $192.168.10.1$ |
| PC 3 | $192.168.10.18$ | $255.255.255.0$ | $192.168.10.1$ |
| PC 4 | $192.168.10.21$ | $255.255.255.0$ | $192.168.10.1$ |
| Printer | $192.168.10.22$ | $255.255.255.0$ | $192.168.10.1$ |

---

### Part G Notes (Optional / Bonus)
The `hosts` file is a local text file used to manually map hostnames to specific IP addresses. It relates to DNS because the computer always checks this file first to resolve a name before sending a request out to an external DNS server.

---

## VI. Realization (Reflection)

1. **Even without a network connection, what network information did your computer still have? Why do you think it still has it?**  
   Even when my network was disconnected, my computer still kept its local hardware and configuration info, like its MAC address, hostname, loopback address ($127.0.0.1$), and an APIPA address. It still has this data because these are built-in identifiers and default protocols stored locally by the operating system, so the device doesn't need an active internet connection to know its own identity on the local level.

2. **Compare Settings, Control Panel, CMD, and PowerShell. Which tool did you find most useful for viewing network information, and why?**  
   While Settings and Control Panel are easier to navigate visually, I found Command Prompt (CMD) and PowerShell much more useful for technical analysis. PowerShell stood out because commands like `Get-NetAdapter` and `Get-NetIPAddress` provide clean, structured outputs that make checking specific adapters super fast. Overall, using the command line gives you direct, unfiltered access to network diagnostics without having to click through multiple menus.

3. **What did the messages from `ping 8.8.8.8` and `nslookup google.com` tell you? How would you use messages like these when troubleshooting a real network?**  
   The `ping 8.8.8.8` command proved that my packets successfully reached Google's public DNS server and returned with low latency, meaning internet connectivity was working. Meanwhile, `nslookup google.com` showed that my machine could successfully translate domain names into actual IP addresses using the DNS server. In a real-world troubleshooting scenario, I would use ping to test if a device can communicate past the local gateway, and nslookup to check if name resolution is broken.

4. **Why should you be careful about sharing your MAC address, IP address, or `ipconfig /all` screenshots online? Relate your answer to data privacy.**  
   Sharing details like your MAC address or network configuration online can expose vulnerabilities because your MAC address is a permanent hardware identifier for your network card. If malicious actors get hold of that data, they could potentially spoof your device or target your network during a security breach. Protecting this technical information is crucial for data privacy to prevent unauthorized device tracking or targeted cyber attacks.

---

## VII. Scoring Guide

| Criteria | Description | Points |
| --- | --- | --- |
| **Completeness** | All tables (1-6) and required fields are filled out. | 25 |
| **Accuracy** | Recorded values match what the tools show and are consistent across Settings, CMD, and PowerShell; sample analysis, binary conversion, and OSI layers are correct. | 30 |
| **Network Design** | Diagram shows a star topology with PCs, switch, router, printer, and ISP; IP plan uses valid, non-duplicate addresses in $192.168.10.0/24$. | 15 |
| **Realization/ Reflection** | Answers are thoughtful, based on the student's own results, and well written. | 20 |
| **Neatness & Timeliness** | Worksheet is legible/well-formatted and submitted on time. | 10 |
| **Total** | | **100** |