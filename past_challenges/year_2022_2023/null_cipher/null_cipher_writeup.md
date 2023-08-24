## Null Cipher

This is a problem from Code Quest 2022.  

It's a cipher that has a ciphertext that looks like random characters. To decrypt
the ciphertext, we read the ciphertext until we find a vowel, we then copy the
character that follows the vowel to the plaintext message.

This is a touch of stegenography in a programming challenge

## Hints

* Solutions should either read text from a file, or have the user cat the file
  and then pipe into their solution as input.
* The solution has to be careful not convert 2 consecutive vowels into plaintext

CT = baaddatal

Where the plaintext characters are ba **a** dda **t** a **l**
    
PT = atl

* Test the solutions on the sample input before trying the larger and more
  complext ciphertext containing the flag

## Sample Solution Code

```
#!/usr/bin/env python3            
                                                                               
import sys

if (len(sys.argv) != 2):
        print("Usage: {} filename.txt".format(sys.argv[0]))       
        print("  Use - instead of a filename to read from stdin")
        print("  First line is the number of lines in the data set")
        sys.exit(1)

if (sys.argv[1] == "-"):
        data = sys.stdin.read()
else:
        f = open(sys.argv[1], 'r')
        data = f.read()
        f.close()

inputlines = data.split('\n')
numLines = int(inputlines[0])

for singleLine in inputlines[1:1 + numLines]:
        outputNextChar = False
        outputLine = ""

        for singleChar in singleLine:
                if (outputNextChar):
                        # Previous char was a vowel
                        outputLine += singleChar
                        outputNextChar = False
                else:
                        # Check for vowels
                        justLower = singleChar.lower()
                        if ( (justLower == 'a') or (justLower == 'e') or
                             (justLower == 'i') or (justLower == 'o') or
                                 (justLower == 'u') ):
                                 outputNextChar = True

        # Finished processing line
        print(outputLine)
```

## Solution

```
$ ./solution.py ciphertext.txt 
sincewecanonlyuselowercasecharsforourtext
replacethebracetextwithrealbraceforflaginput
wildcatbraceiwishthiscipherhadspacesbrace
```

Reading the message indicates that the plaintext has some limitiations on
characters, to the student will have to convert to the proper flag format
before submitting:

```
wildcat{iwishthiscipherhadspaces}
```

