# Password Checker Pt 1

Flag: wildcat{???}

Category:  pwn

Points: 500

## Attachments:

* [a.out](a.out)

## Description:

This program is running on my digital ocean droplet protecting my flags.
I password protected my flag so not everyone can see it.  I even used
a cryptographic hash so you can't easily figure out my password.

You will need Binary Ninja for this challenge!

To access the challenge on the web:
```
nc ctf.mwales.net 45036
```

<details>
<summary>Click to reveal Hint #1</summary>
There are 2 major vulnerabilities that can help you win this challenge.
Can you figure out both of them?
</details>

<details>
<summary>Click to reveal Hint #2 - cost 1 pt</summary>
One of the bugs is system injection
</details>

<details>
<summary>Click to reveal Hint #3 - cost 1 pt</summary>
The other bug is a stack buffer overflow.  But you won't have to control
the instruction pointer or anything too serious if you reverse out all of
the code in main.
</details>

# Password Checker Pt 2

Flag: wildcat{???}

Category: cracking

Points: 750

## Description:

Instead of telling me the flag, what is the password that unlocks it?

When you get the password, convert it to a flag:
wildcat{cracked_password}

You don't need to really access the web for this challenge, you can make
a dummy flag.txt in your local directory and solve this challenge.

<details>
<summary>Click to reveal Hint #1</summary>
You are going to need to brute force crack the hash in the binary.  But
fortunately, since it's md5, it shouldn't be too hard.  Craft your own
password and hash pair and make sure you can crack a simple password.
</details>

<details>
<summary>Click to reveal Hint #2 - cost 1 pt</summary>
John and Hashcat are the 2 goto crackers on Linux.  Your going to probably
need jumbo john, and that doesn't come with ubuntu, so it might be a good
time to try hashcat.  Or do some googling and see if there is an even better
and faster way.
</details>

# Password Checker Pt 3

Flag: wildcat{???}

Category:  pwn

Points: 1000

## Description:

For this challenge, find the 2nd hidden flag in the docker container!

<details>
<summary>Click to reveal Hint #1</summary>
It's not obvious what the 2nd flag will be named or how to get it.  Maybe
try getting a shell on the server!
</details>

<details>
<summary>Click to reveal Hint #2 - cost 1 pt</summary>
If you get a shell using the system injection, it may be difficult to see
the output since everything is sent to md5sum.  Can you prevent md5sum
from running and get some output?
</details>

<details>
<summary>Click to reveal Hint #3 - cost 1 pt</summary>
If you figured out how to get output, you will probably notice that you only
get 1 word of output.  What programs would convert arbitrary text and stuff
into a single long string of characters?
</details>

# Partial Writeup

[Partial Writeup for all 3 challenges - SPOILERS](partial_writeup/partial_writeup_password_check.md)
