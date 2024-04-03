# Pwn Game

Flag: wildcat{ ??? }

Category:  pwn

Points: 1200

## Attachments:

* [game](game)

## Description:

If your player can find the flag and escape the dungeon, the game will
print the flag for you! You can use WASD to move around.

You will need Binary Ninja for this challenge! Pay attention to the
category of this challenge

To access the challenge on the web:
```
nc ctf.mwales.net 45037
```

Note, you will probably need to install the i386 version of libc to run
this on 64-bit Ubuntu 22.04 based systems

```
sudo apt install libc6-i386
```

<details>
<summary>Click to reveal Hint #1</summary>
Try to identify a memory address / variable you want to change.  What memory
do we have access to when we are playing the game?
</details>

<details>
<summary>Click to reveal Hint #2 - cost 1 pt</summary>
Does the game have any checks to make sure your player stays in bounds?
</details>

<details>
<summary>Click to reveal Hint #3 - cost 1 pt</summary>
There are some secret input keys in the game!
</details>

<details>
<summary>Click to reveal Hint #4 - cost 1 pt</summary>
What map location would overflag with the player's flag variable?
</details>

And if you are really stuck...

[Partial Writeup](writeup/pwn_game_partial_writeup.md)
