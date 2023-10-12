# Setup
## Getting Started with a Pentest Distro
Skipping summarizing this section. It mainly contains basic information over the process and choices on how to set up a VM.

## Staying Organized
### Folder Structure
A pretty individual topic in my opinion. Here is the given example for a structure:
```
rollentube@htb[/htb]$ tree Projects/

Projects/
└── Acme Company
    ├── EPT
    │   ├── evidence
    │   │   ├── credentials
    │   │   ├── data
    │   │   └── screenshots
    │   ├── logs
    │   ├── scans
    │   ├── scope
    │   └── tools
    └── IPT
        ├── evidence
        │   ├── credentials
        │   ├── data
        │   └── screenshots
        ├── logs
        ├── scans
        ├── scope
        └── tools
```

### Note Taking Tools
* Cherrytree
* Visual Studio Code
* Evernote
* Notion
* GitBook
* Sublime Text
* Notepad++	

### Other Tools and Tips
Maintain knowledge base with quick reference guides and cheat sheets (each HTB Academy Module has a cheat sheet!).

We should also maintain checklists, report templates and a vulnerability database with description, impact, advices and references.

## Connecting Using VPN
A virtual private network (VPN) allows us to connect to a private (internal) network and access hosts and resources as if we were directly connected to the target private network. It is a secured communications channel over shared public networks to connect to a private network (i.e., an employee remotely connecting to their company's corporate network from their home). VPNs provide a degree of privacy and security by encrypting communications over the channel to prevent eavesdropping and access to data traversing the channel.

* client-based VPN: use of client software. User is fully connected to the company network
* SSL VPN: uses the web browser as VPN client. Access is restricted to web-based applications

Use of openvpn:
```
openvpn user.ovpn
```

Show connected networks:
```
netstat -rn
```