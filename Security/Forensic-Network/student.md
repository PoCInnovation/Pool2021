
# Introduction
In a CTF context, "Forensics" challenges can include file format analysis, steganography, memory dump analysis, or network packet capture analysis. Any challenge to examine and process a hidden piece of information out of static data files (as opposed to executable programs or remote servers) could be considered a Forensics challenge (unless it involves cryptography, in which case it probably belongs in the Crypto category).

Forensics is a broad CTF category that does not map well to any particular job role in the security industry, although some challenges model the kinds of tasks seen in Incident Response (IR). Even in IR work, computer forensics is usually the domain of law enforcement seeking evidentiary data and attribution, rather than the commercial incident responder who may just be interested in expelling an attacker and/or restoring system integrity.
# Useful tools

# Network
Network forensic can be defined as the investigation of  **network**  traffic patterns and data captured in transit between computing devices—can provide insight into the source and extent of an attack. It also can supplement investigations focused on information left behind on computer hard drives following an attack.

Identifying attack patterns requires a thorough understanding of common application and network protocols. For example:

-   Web protocols, such as http and https
-   File transfer protocols, such as Server Message Block (SMB) and Network File System (NFS)
-   Email protocols, such as Simple Mail Transfer Protocol (SMTP)
-   Network protocols, such as Ethernet, WiFi, and Transmission Control Protocol/Internet Protocol (TCP/IP)

The investigator must understand the normal form and behavior of these protocols to discern the anomalies associated with an attack.

During this part of the day we are going to use Wireshark.
Wireshark is a network analysis tool, also called sniffer, that will allow you to visualize all the data that transit on a device. It can also be used to back up all this data for later analysis via PCAP or PCAPNG file.

# Memory
Memory forensic refers to the analysis of a computer's memory dump. Basically a memory dump is a snapshot capture of the computer memory data.
A memory dump can contain valuable forensics data about the state of the system before an incident such as a crash or security compromise.

The analysis of a memory dump is a very good way to find if a malware is operating on the computer at the time of the snapshot.

https://www.synacktiv.com/publications/sharkyctf-ezdump-writeups-linux-forensics-introduction.html
https://forensixchange.com/posts/19_09_17_defcon_dfir_ctf/
https://defcon2019.ctfd.io/
https://drive.google.com/drive/folders/1JwK8duNnrh12fo9J_02oQCz8HlILKAdW

## Windows
