# Solution

This challenge data we have looks like:

```
0000000 064567 062154 060543 075564 061460 032164 057554 032461
0000020 073537 030463 062162 005175
0000030
```

Any sane person would normally display octal a single byte at a time (0-377 in
octal). But for some strange reason, we have 6 octal digits for each number.
You also need to recognize the first column is just the address / offset into
the file.

I think the simplest thing to do would be just convert it all to
hex.  Cyber Chef can do conversion of octal bytes easily, but not 16-bit octal
words.  There isn't that much data, so lets just suffer and do it by hand.

```
octal    hex
064567 = 6977
062154 = 646c
060543 = 6163
075564 = 7b74
061460 = 6330
032164 = 3474
057554 = 5f6c
032461 = 3531
073537 = 775f
030463 = 3133
062162 = 6472
005175 = 0a7d
```

Lets convert the first few from hex to ASCII.  You can see an ascii table easily
on Linux by typing the following command:

```
man ascii
```

```
69 77 64 6c 61 63 ...
i  w  d  l  a  c
```

The flag should be in the format wildcat{blah blah blah}.  It looks like each
pair of characters are flipped.  This is because of endianness.  Computers
sometimes represent numbers with the highest place on the left (like we write
decimal numbers in math class, big endian), or reversed where the number is
right to left (one byte at a time).

Flipping each pair of numbers, and then decode each byte reveals the flag...

```
77 69 6c 64 63 61 74 7b ....
w  i  l  d  c  a  t  {  ....
```

Truly awful.

## Scripted solution

### Reading in the data from the file

I would probably pre-process the octal dump file and convert it to just octal,
and get rid of all the address information.  That is easiest done with the cut
command:

```
$ cat chal.txt  | cut -d ' ' -f 2-
064567 062154 060543 075564 061460 032164 057554 032461
073537 030463 062162 005175
0000030
```

That command says use a single space character as a delimiter, and only give me
fields 2 and after (cut starts numbering the fields / columns with 1).  The last
row comes though because it doesn't have 2 fields, so lets just use the head
command to say we only want the first 2 rows

```
$ cat chal.txt  | cut -d ' ' -f 2- | head -n 2
064567 062154 060543 075564 061460 032164 057554 032461
073537 030463 062162 005175
$ cat chal.txt  | cut -d ' ' -f 2- | head -n 2 > chal2.txt
```

Now we could use python to read in each line, split each line into the different
parts, and then add each part to a single long list of octal strings.  I usually
send my challenge file into my solve script on stdin.

So the start of my python script would look like the following:
```
#!/usr/bin/env python3

import sys

chaltext = sys.stdin.read()

# Splits on any whitespace, so spaces and newlines.  Just what we want
chalparts = chaltext.split()

print(chalparts)
```

And I can run the first part and get some debug output by executing it in the
following manner:

```
$ cat chal2.txt | ./solve.py 
['064567', '062154', '060543', '075564', '061460', '032164', '057554', '032461', '073537', '030463', '062162', '005175']
```

### Converting octal to an integer

I almost wanted call this section "Converting octal to a base-10 integer", but
in reality, the only thing a computer ever understands is binary.  It simply
converts numbers to hex or base-10 for our convenience, internal to it's memory
and registers, everything is binary!

But anyways, how would we solve this via script?

The int() function that we use to convert base-10 strings into integers has an optional
arguement that we can use to specify alternative base number systems

We can simply convert by executing the following on each part:

```
int(octalStringVar, 8)
```

If we didn't have that easy way to convert the string to an integer, we could
do it manually.  Starting at the right-most digit of the string, and working
our way to the left, we could convert to an integer using the following math.  I'll
show you a base-10 example first, and then we will show what it looks like 
using octal base numbers.

```
# converting 248 to an integer using math
myNum = "248"
intVal = 0
intVal += int(myNum[2]) * 1
intVal += int(myNum[1]) * 10
intVal += int(myNum[0]) * 100
print(intVal)
248
```

Now using base 8 or octal

```
myNum = "064567"
intVal = 0
intVal += int(myNum[5]) * 1
intVal += int(myNum[4]) * 8
intVal += int(myNum[3]) * 64
intVal += int(myNum[2]) * 512
intVal += int(myNum[1]) * 4096
intVal += int(myNum[0]) * 32768
print(intVal)
26999
```

Anyways, now my script would look like the following, converting each octal
string into an integer

```
flag = ""
for singleOctalNum in chalparts:
    curNum = int(singleOctalNum, 8)
    print(hex(curNum))
```

### Separating each byte

This is really easy since we only have a 2 byte number.  There is a math way,
and a bitwise solution for this.  The math way is

```
    firstByte = curNum % 0x100
    secondByte = curNum // 0x100
```

The bitwise way is:

```
    firstByte = (curNum & 0xff)
    secondByte = (curNum & 0xff00) >> 8
```

### Converting each byte to ascii and assembling flag

In python chr(number) converts numbers to ASCII characters, and ord('a')
converts characters to ASCII index value.

Lets add each byte to the flag, and then print it out the flag:

```
    flag += chr(firstByte)
    flag += chr(secondByte)

print(flag)
```

Running...

```
$ cat chal.txt | cut -d ' ' -f 2- | head -n 2 | ./solve.py 
```


