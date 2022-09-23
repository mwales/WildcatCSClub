### Coin Series
# (Wildcat Coin, Wildcat Coin Mining, Sad Face Coin Mining)
These challenges were largely based on cryptographic hashing (namely MD5) and a bit of programming.

# Wildcat Coin
For this challenge, you were given a .zip file with 999 .bin files each containing a possible flag, only one of which was valid.
The task was to find which file's triple MD5 hash contained the string "ca7c0de"

To solve this I made a python program:
`
import hashlib  # this library has the md5 hash function
import random
import string

for i in range(1, 999):    # for 1 - 999
  file = open("chal/file_+ str(i) + ".bin", "rb") # open that number's file as a bytes like object
  
  fileData = file.read()     
  hash1 = hashlib.md5(fileData).hexdigest().encode()
  hash2 = hashlib.md5(hash1).hexdigest().encode()
  hash3 = hashlib.md5(hash2).hexdigest().encode() # get the hash, convert it to text, then convert that string back to bytes - I bet theres a better way but this was simpler
  
  if "ca7c0de" in hash3: # if it has found the correct file then print the file number
    print(i)

`

Let it run and it as expected gives the number of the file - which you can open the file up and submit.

# Wildcat Coin Mining
For this challenge, we need to make/find two new valid coins - sadly the two we already got don't work.
To do this I just modified my program to keep checking the triple hash of random strings until it found a valid coin.

Now my program looks something like this:
`
def tripleHash(data):  # This is the same as the other code just much worse as it is all in one line
    return hashlib.md5(hashlib.md5(hashlib.md5(data.encode()).hexdigest().encode()).hexdigest().encode()).hexdigest()
letters = string.ascii_lowercase # this is my array of valid characters to be randomly chosen from
while True:
    coin = ''.join(random.choice(letters) for j in range(32)) # create a 32 character long string of letters from out letters list
    data = tripleHash(coin) # triple hash it

    if "ca7c0de" in data: # check if its valid and print
        print(coin)
`

After a few minutes of running you should get a few coins which can be uploaded with the command in the challenge

# Sad Face Coin Mining
This one is actually exactly the same as Wildcat Coin Mining except the required string is now "5adface".
We can actually use the same program too, just replace "ca7c0de" with the new string.
