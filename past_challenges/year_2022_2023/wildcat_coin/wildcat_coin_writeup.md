# Wildcat Coin

This challenge talks a bit about the hashing of a bitcoin works.  It invents
a coin type called a "Wildcat Coin" that had a triple md5-hash with the
hexadecimal value ca7c0de in it.

The challenge gives the user a whole bunch of random files, and they need to
determine which of the files is a valid "Wildcat Coin"

## Hints

* Create a script to create the triple hash, use the example coin to verify
  your script.
* If having problems with the script, print each intermediate hash out and
  compare to the example.  Be very wary of extra whitespace (many shell tools
  will add it without you knowing), it can easily corrupt hash value.

## Solution

I created a script that has an output much like regular old md5sum, but it's the
the triple hash calculation instead.

```
#!/bin/bash

hash3=$(md5sum $1 | head -c 32 | md5sum | head -c 32 | md5sum | cut -d " " -f 1)
echo "$hash3 $1"
```

Extract the files from the zip.  Use the find or xargs command to run the triple
hash script on each file, and grep for an output with ca7c0de in it.

```
$ find . -type f -exec ../../triple_hash.sh {} \; | grep ca7c0de
ef906b451f374655398252bfcca7c0de ./file_239.bin
```

The contents of the file have the flag...

```
$ cat ./file_239.bin
wildcat{crypto_landfill_millionaire}BLAKE2.6966
```

