# Basic Tools
## Using SSH
Secure Shell (SSH, port 22) is a network protocol that allows you to connect encrypted to a remote system. It uses password or public-key authentication.

The OpenSSH client can be used as followed:
```
ssh Bob@10.10.10.10
```

## Using Netcat
Netcat is a network utility for interacting with TCP/UDP ports.

Example to interact with port 22 (ssh):
```
netcat 10.10.10.10 22
```

Connecting to a port and get information of the service via the shown banner is called Banner Grabbing.

An alternative is `socat`. Additional it can forward ports, connect to serial devices or can be upgraded to a fully TTY.

## Using Tmux
Tmux is a terminal multiplexer. It gives more features to the terminal and allows for example to create multiple windows and jump through them or to split view multiple terminals.

The basic commands are:
```
[CTRL + B] + C      Create new window
[CTRL + B] + 0-9    Switch to window nr. 0-9
[CTRL + B] + %      Create new window in vertical split
[CTRL + B] + "      Create new window in horizontal split
[CTRL + B] + Arrow  Switch to windows
```
Cheat-Sheet: https://tmuxcheatsheet.com/

## Using Vim
Vim is text editor for the command line, that can be used entirely on the keyboard and has several hotkeys.
```
vim /etc/hosts
```

Basic commands:
```
i   Enter insert mode
:   Enter command mode
x	Cut character
dw	Cut word
dd	Cut full line
yw	Copy word
yy	Copy full line
p	Paste
```

Basic commands in command mode:
```
:1	Go to line number 1.
:w	Write the file, save
:q	Quit
:q!	Quit without saving
:wq	Write and quit
```

Cheat-Sheet: https://vimsheet.com/

## Optional Exercises
Challenge your understanding of the Module content and answer the optional question(s) below. These are considered supplementary content and are not required to complete the Module. You can reveal the answer at any time to check your work.

```
Target: 94.237.53.115:56436 
Time Left: 87 minutes
```

Apply what you learned in this section to grab the banner of the above server and submit it as the answer.

### Solution
```
> SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1
```

Banner Grabbing with Netcat:
```
$ nc 94.237.53.115 56436
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1
^C$
```