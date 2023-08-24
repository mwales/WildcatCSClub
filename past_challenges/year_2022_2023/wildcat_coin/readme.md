Name: Wildcat Coin

Category:  crypto

Attachments:
* [example_coin.bin](example_coin.bin)
* [chal.zip](chal.zip)

Message:

Many crypto currencies require a "proof of work" to mine a new crypto coin. The
proof of work usually involves computing a crytographic hash on a file, and
trying it over and over until the hash has a special / unique pattern. For
BitCoin the hash must have a long sequence of zeroes in it.

If you don't know what a cryptographic hash function is, you can read about
them here:  https://en.wikipedia.org/wiki/Cryptographic_hash_function

For my Wildcat Coin that I created I use triple MD5, and when a coin is triple
MD5 hashed, the hash has to contain ca7c0de in it somewhere.  Let me walk you
through an example.

```
$ hexdump -C example_coin.bin
00000000  77 69 6c 64 63 61 74 7b  67 72 61 64 65 5f 6e 61  |wildcat{grade_na|
00000010  6d 65 64 5f 65 6e 64 7d  32 38 32 30              |med_end}2820|
0000001c
$ md5sum exampple_coin.bin
a6fc28554b424713bb62ca082fbc3ceb  example_coin.bin
```

So a6fc28554b424713bb62ca082fbc3ceb is the first hash.  It's exactly 32 characters
long, I'm going to hash the 32 characters...

```
md5sum example_coin.bin | head -c 32 | md5sum
d8ba7e2f8e5eb1ecbb097e47829f8b80  -
```

The dash means there was no file, it computed the hash from stdin.  This would
be the hash for double MD5.  I got tired of typing all that out, so I created a
script that would compute the triple MD5 for me.

```
$ ./triple_hash.sh example_coin.bin 
8c050a4ebd0ca7c0deafa9c910636dd7 example_coin.bin

```

Also notice that the the special coin string appears in the triple hash.  I'll
underline it incase you missed it.

```
8c050a4ebd0ca7c0deafa9c910636dd7 example_coin.bin
           -------
```

I have a bunch of files in chal.zip, and only 1 of them is a Wildcat Coin.  Can
you tell me what the flag is in the file that is a valid Wildcat Coin?

<details>
<summary>Click to reveal Hint # 1</summary>
Make a script or a 1 line command that you can easily compute the triple hash
of a file.  Try your triple hash on the example file and make sure your triple
hash that you calculate is the same exact triple hash that explanation says it
should be.  Sometimes whitespace will change the value of a hash even through
2 files look the same.
</details>

<details>
<summary>Click to reveal Hint # 2</summary>
There are so many files to sort through!  Make a script that checks each file,
or use the find command to run the triple hash on each file.  Use <b>grep</b>
to find the magic string in the output
</details>

[ Solution Write-up - CONTAINS SPOILERS](wildcat_coin_writeup.md)