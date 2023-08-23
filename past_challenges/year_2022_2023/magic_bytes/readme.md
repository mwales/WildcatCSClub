Name: magic_numbers

Category:  forensics

Attachments:
* [chal.zip](chal.zip)

This challenge is a recreation of a true story...

In an effort to avoid accidentally butt-dialing people with my Samsung Galaxy
phone, I turned the pin code unlock feature on.  I didn't realize at the time
that there was a default enabled option, that after 10 incorrect pin tries,
the phone would erase itself.  Can you see where this might go wrong?

Well one day, while doing some yardwork in the heat, lots of sweating, the
phone was in my pocket getting really warm.  When I looked at it, it told
me it was erasing all of it's contents!  All my photos, mp3s, and memes!  I
ripped the battery out as fast as possible. Old Android phones would just
appear as mass storage devices / thumb drives when plugged it in to my PC.
I was too late, everything was gone!

I had to try something.  I dd-ed (https://en.wikipedia.org/wiki/Disk_cloning)
the contents of my phone's flash to a file and ran some forensic filesystem
recover software.  It recovered many of the files, but now the filenames are
long gone.

Your flag is in there.... somewhere....

Here is a hint though, most files have magic bytes (aka file signatures).  You
can dump out the file contents by executing the following:

```
hexdump -C filename 
```

This wikipedia page has a list of many known magic bytes:

https://en.wikipedia.org/wiki/List_of_file_signatures

There is a linux program named __file__ (yeah, that is a silly name, this is un-google-able), that has these magic bytes built into it
and it can probably help you. Put the correct extension on each file and open
all the files to find the flag. Try searching for "man file" to find out more information about it.

[Solution Writeup - SPOILERS](magic_bytes_writeup.md)

