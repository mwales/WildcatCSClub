# Command Injection

Vulnerability where user string data is provided to an API call, and unexpected
user data can cause the API to perform unexpected behavior.

The most typical example of this vulnerability is system call injection.  A C
program can execute external applications using the system call.  The example
code below intends to call the __cat__ shell command and provide it the name of
a file provided by the user.  But the user can use a semicolon, pipes, or 
other various shell syntax to call additional programs.

```
// Example Code from OWASP Foundation
// Command Injection
// https://owasp.org/www-community/attacks/Command_Injection
// Author: Weilin Zhong
// Contributor(s): Wichers, Amwestgate, Rezos, Clow808, KristenS, Jason Li, Andrew Smith, Jmanico, Tal Mel, kingthorin

#include <stdio.h>
#include <unistd.h>
#include <string.h> // added by me for a clean compile
#include <stdlib.h> // added by me for a clean compile

int main(int argc, char **argv) {
 char cat[] = "cat ";
 char *command;
 size_t commandLength;

 commandLength = strlen(cat) + strlen(argv[1]) + 1;
 command = (char *) malloc(commandLength);
 strncpy(command, cat, commandLength);
 strncat(command, argv[1], (commandLength - strlen(cat)) );

 system(command);
 return (0);
}
```

So a user could specify a filename that also asks for the kernel version.

```
./a.out "story.txt; uname -a"
$ ./a.out "story.txt; uname -a"
Once upon a time...
Linux Metroid 6.5.0-14-generic #14~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Mon Nov 20 18:15:30 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```

Or pop a shell...

```
$ ./a.out "--version && /bin/sh"
cat (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Torbjorn Granlund and Richard M. Stallman.
$ ls
a.out  readme.md  sample1.c  story.txt
```

Not to leave out any web developers, PHP can also host this vunlerability:

```
<?php
print("Please specify the name of the file to delete");
print("<p>");
$file=$_GET['filename'];
system("rm $file");
?>
```

Even when an applications attempts to sanitize the user input, it can sometimes
be difficult to sanitize against all possible ways to escape / exploit
safeguards and generate unexpected behaviors.  On a *nix system, here are some
methods to call a different command from within command.

* ;
* &&
* $(/bin/sh)
* \`/bin/sh\`  # backticks
* |            # pipe

If you sanitize against some of these, but miss a single one, your code still
will likely be vulnerable

# Real world example

A hilariously dumb version of this bug (or atleast similar enough) was on the
original HTC Dream / G1 (the original Google Andorid phone).  Everything you
typed with the keyboard would be passed to the shell (a shell running as root
no less...).  If you simply sent a text message "reboot", your phone would
reboot...

[Worst. Bug. Ever. (via Wayback Machine)](https://web.archive.org/web/20081201032420/http://blogs.zdnet.com/Burnette/?p=680)

The first Android jailbreak was to simply start telnetd, it would then start
the telnet daemon as root.

# Other examples of this type of bug

* Python's eval function
* Python's system function
* Java call cmd.exe to run a script on Windows systems
* SQL Database Queries


# Mitigations

If a program has to call an API that can interpret the user controlled data,
the application could sanitize the user input before calling the API.  This
can be very tricky, and it may be easy to miss things with your sanitization.

Another alternative would be to use APIs that are less vulnerable.  The C and
PHP version of system give the arguments to __/bin/sh__ interpreter, but the
Java version of system does not. The Java equivalent calls the program and
specifically passes additonal string data after the first space as arguments
to the application.

## References

* [Command Injection](https://owasp.org/www-community/attacks/Command_Injection), Weilin Zhong of OWASP Foundation
* [Worst. Bug. Ever.](http://blogs.zdnet.com/Burnette/?p=680), Ed Burnette of ZDNet.