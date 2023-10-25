# Problem Solving
Those sections are pretty much Hack The Box related. So I will strongly summarize them.

## Common Pitfalls
While performing penetration tests or attacking HTB boxes/labs, we may make many common mistakes that will hamper our progress. In this section, we will discuss some of these common pitfalls and how to overcome them.

### VPN Issues
We may sometimes face issues related to VPN connections to the HTB labs network. First, we should ensure that we are indeed connected to the HTB network.

#### Still Connected to VPN
```
sudo openvpn ./htb.ovpn
```

#### Getting VPN Address
```
ip -4 a show tun0
```

#### Checking Routing Table
```
sudo netstat -rn
```

#### Pinging Gateway
`10.10.14.1` is the gateway for the network `10.10.14.0/23` from our `tun0` interface:
```
ping -c 4 10.10.14.1
```

#### Working on Two Devices
The HTB VPN cannot be connected to more than one device simultaneously.

#### Checking Region
If we feel a noticeable lag in our VPN connection, such as latency in pings or ssh connections, we should ensure that we are connected to the most appropriate region. HTB provides VPN servers worldwide, in Europe, USA, Australia, and Singapore.

#### VPN Troubleshooting
[HackTheBox Help page](https://help.hackthebox.eu/troubleshooting/v2-vpn-connection-troubleshooting)

### Burp Suite Proxy Issues
#### Not Disabling Proxy
To use Burp with our browser we have to change the proxy settings to the Burp proxy. If it's not needed anymore, we can turn them off. For example via the plugin `Foxy Proxy` this is pretty simple.

### Changing SSH Key and Password
In case we start facing some issues with connecting to SSH servers or connecting to our machine from a remote server, we may want to renew or change our SSH key and password to make sure they are not causing any issues. We can do this with the `ssh-keygen` command.

By default, SSH keys are stored in the .ssh folder within our home folder. If we wanted to create an ssh key in a different directory, we could enter an absolute path for the key when prompted.

## Getting Help
When we start working on boxes on Hack The Box, we may likely get stuck in certain areas and may need to ask other players for some little tips and hints, to be able to move forward on the box. Here are some areas in which we can get help.

### Forum
The [Hack The Box Forum](https://forum.hackthebox.eu/) is an excellent place for discussing live and retired Hack The Box boxes and challenges.

Each box has an official discussion thread, in which live discussions are had about all aspects of the box, without giving any spoilers or clear indications on how to exploit the box.

### Discord
We can join the Official HTB Discord server by clicking on this [link](https://discord.gg/hRXnCFA).

The Discord server also covers discussions about General Announcements, Boxes and Challenges, Academy Modules, HTB Labs, Hacking and Pentesting, and General Support.

### Asking Questions Effectively
1. What point of the box/challenge are we stuck at 'i.e., user/root'?
2. What steps have we taken so far to get to the point we are at?
3. What step are we failing at, and what have we done to resolve our issue?
4. Always try to be very specific on what we need help on, rather than asking for general help

### Answering Questions Effectively
1. Be as spoiler-free as possible, and do not get direct instructions on how to complete the current step or the entire box
2. Give minor hints or tips that can lead to the right direction for completion, and do not give entire suggestions for completion
3. Share resources that we found helpful
4. Share tips on points we were getting stuck on

### Getting Technical Help
* [official HTB FAQ](https://help.hackthebox.com/)
* [open ticket at HTB Support](https://help.hackthebox.com/en/)