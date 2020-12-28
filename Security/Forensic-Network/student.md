# Introduction

In a CTF context, "Forensics" challenges can include file format analysis, steganography, memory dump analysis, or network packet capture analysis. Any challenge to examine and process a hidden piece of information out of static data files (as opposed to executable programs or remote servers) could be considered a Forensics challenge (unless it involves cryptography, in which case it probably belongs in the Crypto category).

Forensics is a broad CTF category that does not map well to any particular job role in the security industry, although some challenges model the kinds of tasks seen in Incident Response (IR). Even in IR work, computer forensics is usually the domain of law enforcement seeking evidentiary data and attribution, rather than the commercial incident responder who may just be interested in expelling an attacker and/or restoring system integrity.

# [](https://github.com/PoCInnovation/Pool2021/blob/master/Security/Forensic-Network/student.md#network)Network

Network forensic can be defined as the investigation of  **network**  traffic patterns and data captured in transit between computing devices—can provide insight into the source and extent of an attack. It also can supplement investigations focused on information left behind on computer hard drives following an attack.

Identifying attack patterns requires a thorough understanding of common application and network protocols. For example:

-   Web protocols, such as http and https
-   File transfer protocols, such as Server Message Block (SMB) and Network File System (NFS)
-   Email protocols, such as Simple Mail Transfer Protocol (SMTP)
-   Network protocols, such as Ethernet, WiFi, and Transmission Control Protocol/Internet Protocol (TCP/IP)

The investigator must understand the normal form and behavior of these protocols to discern the anomalies associated with an attack.

During this part of the day we are going to use Wireshark. Wireshark is a network analysis tool, also called sniffer, that will allow you to visualize all the data that transit on a device. It can also be used to back up all this data for later analysis via PCAP or PCAPNG file.
## Basic HTTP
To solve this challenge, focus on trying to understand what request the user is doing and what response did he get from his request.

## Basic Header
This challenge is similar to the past one but this time we want you to find the username and the password of the user who made those requests.

## Real CTF Part 1
Here is the first part of a **real challenge** for you !
You will have to focus on filtering information, because this is a FAT file. Here is the context:

You are a sysadmin in a small business. Your boss suspects that two employees exchange flags on company time. However, even though he can see slack’s private messages between employees, he didn’t see any suspicious message, but he knows that they’re communicating!
Having recently installed a network tap on the main switch of your network, you see all the packets that go through. The first flag is in a discussion between the two employees and it is very easy to recognize.

Now good luck !
## Real CTF Part 2
You know, ASCII isn't the only character encoding on earth.
## Real CTF Part 3
In the conversation you found, they are talking about a certain file download via a specific protocol. Get the file and you will get the flag.
## Real CTF Part 4
I always though that TLS was impossible to break, can you prove me that I am wrong ?
## Real CTF Part 5
The employee hints about [PyRDP](https://github.com/GoSecure/pyrdp) (an RDP man-in-the-middle) and gives two CLIENT_RANDOM data. Can you dig this and find what they are trying to hide ?
## Real CTF Bonus Part

A computer did a brief attempt at performing a man-in-the-middle attack on the whole network. Find the mac address of the attacker as well as the packet number that prove such attack. 

`Flag format: macAddressLowercase-packetNumber`z

# [](https://github.com/PoCInnovation/Pool2021/blob/master/Security/Forensic-Network/student.md#memory)Memory

Memory forensic refers to the analysis of a computer's memory dump. Basically a memory dump is a snapshot capture of the computer memory data. A memory dump can contain valuable forensics data about the state of the system before an incident such as a crash or security compromise.

The analysis of a memory dump is a very good way to find if a malware is operating on the computer at the time of the snapshot.

For this part you are going to use [Volatility](https://github.com/volatilityfoundation/volatility), an open source memory forensic framework written in python. It is used to analyze crash dumps, raw dumps, VMware & VirtualBox dumps.

## Download the file
For this part we will use this [dump](lol) with volatily. The dump is 5GB so please install it in advance if your connection is low.

When you have the memory dump on your computer get the SHA1 hash of the dump and submit it as the flag. This challenge is only here to be sure that you have the good file, if the answer is bad please contact one of the staff member to get help.

## Profile
Volatility works by giving the framework a specified profile so it can retrieve information from the dump so the first thing that you want to do with Volatility is to identify what OS profile the dump is from.

The flag is the most appropriate profile for this dump.

## Take notes
What was the process ID of notepad.exe ?
## wscript can have children too
Name the child processes of wscript.exe.
## tcpip settings
What was the IP address of the machine at the time the RAM dump was created ?
## intel 
Based on the answer regarding to the infected PID, can you determine what the IP of the attacker was ?
##  i <3 windows dependencies
What process name is VCRUNTIME140.dll associated with ?
## mal-ware-are-you
What is the md5 hash value the potential malware on the system ?
##  lm-get bobs hash
What is the LM hash of bobs account ?
## vad the impaler
What protections does the VAD node at 0xfffffa800577ba10 have ?
## more vads?!
What protections did the VAD starting at 0x00000000033c0000 and ending at 0x00000000033dffff have ?
## vacation bible school
There was a VBS script run on the machine. What is the name of the script ? (submit without file extension)
## thx microsoft
An application was run at 2019-03-07 23:06:58 UTC, what is the name of the program ? (Include extension)
## lightbulb moment
What was written in notepad.exe in the time of the memory dump ?
## 8675309
What is the shortname of the file at file record 59045 ?
## whats-a-metasploit ?
This box was exploited and is running meterpreter. What PID was infected ?
