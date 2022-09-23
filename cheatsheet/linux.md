# Common Linux Commands

| Command                      | Meaning     | What it does
|------------------------------|-------------|----------------
| ls                           | listing      | List files in directory
| cd dirname                   | change dir   | Change directory to dirname
| cd ..                        |              | Go back one directory (the parent directory)
| pwd                          | present working dir | Shows you what directory are you in
| cat filename                 | concatenate  | Print the contents of the file to the screen (don't do this with binary files, zips, etc)
| cat file1 file2 file3        |              | Prints all the files back to back like they were a single file, they are concatenated together
| less filename                | less         | Print the contents of a file, but you can PgDown/PgUp to read a large file
| gedit filename               | Gnome Edit   | Open text editor gedit (easy to use) to edit file (only good for ASCII / text files)
| nano filename                | Small Editor | Text editor, command line (not a GUI), easy to use
| vi filename                  | Visual Edit  | Text editor. NOT EASY TO USE! If something tells you to use vi, try using gedit or nano instead!
| rm filename                  | Remove       | Remove a file
| mv filenameold fnnew         | Move         | Moves / Renames a file from old name to new name (there is no rename command in Linux)
| cp src dest                  | Copy         | Copies a file from source location to destination location
| whoami                       | Who am I     | Tells you what username is currenty on system
| history                      | History      | Lists previous commands run
| touch filename               | Touch        | Creates an empty file with the given name
| man command                  | Manual       | Shows manual page about the command, shows you the options, similar commands
| man -k topic                 |              | Searches for man pages pertaining to topic (see below)
| reset                        | Reset        | If you terminal is acting weird, try reset to fix it
| exit                         | Exit         | Exit shell (logout of server)
| head [filename]              | Head         | List the first few lines of a file (or stdin)
| sort [filename]              | Sort         | Sorts file (or stdin) line by line
| uniq [filename]              | Unique       | Removes CONSECUTIVE redundant lines from a file
| wc [filename]                | Word Count   | Counts number of words in a file (or stdin)
| tail [filename]              | Tail         | List the last few lines of a file (or stdin)
| tee filename                 | Tee (pipe)   | Writes the standard output piped into command into a file, while displaying the output
| file                         | File         | Tells you what type of file something is (based on file signatures, can be tricked)
| df                           | Disk free    | Lists disc drives mounted, and how much free space
| du                           | Disk usage   | Lists how much space is being used by files
| watch [command]              | Watch        | Run (watch) a command over and over (every 2s)
| !!                           | last cmd     | Run last command again
| ~                            | Home         | Home directory (/home/username)

# Process Management

| Command                      | Meaning     | What it does
|------------------------------|-------------|----------------
| kill [-9] pid                | Kill         | Kills a running process (-9 is KILL signal, which is sometimes required)
| killall processname          | Kill All     | Kills all processes with the given name ex: killall chrome\
| top                          | Top          | Lists processes running (interactive)
| htop                         | H Top        | Fancier version of top (bar graphs, easy sorting)
| ps [aux]                     | Process List | Dumps list of running processes

# Files / permissions

| ll                           | long list    | List file, file length, and file permissions (ls -l)
| sudo command                 | Superuser do | Runs the command as root user (administration commands).  Requires sudo permissions
| chmod permissions filename   | Channge mode | Changes read (+r), write (+w), execute (+x), or sticky bits (+s) for a file.  a=all, u=user, g=group, o=other
| chown user:group filename    | Change owner | Changes who owns a file

```
ls -l                         # Lists type of file, rwx for user, rwx for group, rwx for other, owner, group, length, etc
chmod a+rx filenames          # All user can read / execute
                              # Dirs need execute permission to cd into
chmod 744 filename            # Set permission with octal (for rwx bits)
```

# Searching / investigation

| Command                      | Meaning     | What it does
|------------------------------|-------------|----------------
| grep                         | Global Regex | Finds lines containing a given string and outputs them
| find                         | Find         | Find files.  Has insane amount of options
| binwalk                      | Bin Walk     | Looks all through a file to find file signatures / hidden files.  Many false positives!
| lsof                         | ls open files| List open files on the system
| exif                         |              | Allows reading and writing of EXIF metadata
| strings                      | Text Strings | Finds chains of human readable characters within a file 
| hexdump                      | Hex Dump     | Presents a three column ifnterface displaying line numbers, raw hex data and ASCII.
| xxd                          |              | Creates a hex dump or can create a file from a hex dump
| file                         | filename     | Will try to tell you what type of file something is

## Compression Tools
| Command           | Compress                 | Extract                    | Notes
|-------------------|--------------------------|----------------------------|---------------------------------------
| zip               | zip filename.zip -r dir  | unzip filename.zip         | Compatible with windows
| tar               | tar -cvf filname dir     | tar -xvf filename          | Tape ARchive
| gzip              | gzip filename            | gunzip filename            | .gz extension (very common, fast)
| bzip2             | bzip2 filename           | bunzip2 filename           | .bz or .bz2 extension (slower, but better compression)
| rar               | rar a filename dir       | rar x filename             | .rar (compatible with WinRAR)
| tar / gzip        | tar -czvf filename dir   | tar -xzvf filename         | Combines tar (many files to single file) and gzip (compression) .tar.gz or .tgz extension
| tar / bzip2       | tar -cjvf filename dir   | tar -xjvf filename         | Combines tar (many files to single file) and bzip2 (compression) .tar.bz2 or .tbz

## Networking

| Command                      | Meaning     | What it does
|------------------------------|-------------|----------------
| ip addr show                 | ip          | Lists IP address of interfaces (NIC card, wifi, virtual interfaces for VMs)
| ifconfig                     | interface config | Old version of ip addr show
| ping [ip/host]               | ping        | Sends ICMP packet, waits for response.  Is this server online?
| netstat -ant                 | network status   | Lists all current network connections
| netstat -lnp                 |                  | Lists all listening connections
| nmap                         | network map      | Lists devices / ports on network.  DO NOT USE AT SCHOOL / SETS OFF ALARMS
| nc                           | net cat          | Connects to a TCP port on a devices to send / receive text (no authentication / encryption)
| socat                        | stream cat       | Fancier (more complicated) version of netcat
| wget [url]                   | www get          | Download file from internet
| curl                         | client url       | Transfer data from a server (many uses, search for usages on web)
| wireshark                    | Wireshark        | Capture (or view) network traffice (pcap files)
| tcpdump                      | TCP dump         | Command line tool to create pcaps


## Commands for system maintenance

| adduser username             | Adds a user to the system
| deluser username             | Deletes a user from the system
| addgroup groupname           | Adds a group to the sytem
| adduser username groupname   | Adds an existing user to the group
| passwd                       | Change your password
| passwd username              | Changes the password of another user (must run as root)
| man commandname              | Shows the built-in manual for the command.  Press q to exit
| man -k subjorcmd             | Search for man pages
| mkdir dirname                | Makes a directory named dirname
| rm filename                  | Removes / deletes a single file (not a directory though)
| rmdir dirname                | Removes a single directory (must be empty)
| rm -rf dirname               | Deletes a file/directory recursively (all subdirectories) without asking / prompting (force). BE CAREFUL WITH THIS.
| sudo command                 | Runs the command as root (if the current user has sudo privledges)
| sudo -i                      | Create a root shell (don't need to sudo every root command / worry about passwords).  BE CAREFUL WITH THIS.
| exit                         | Exit shell (exit root shell if you started a root shell)
| apt install pkgname          | Install a package (Ubuntu / Debian systems)
| apt remove pkgname           | Removes a package (Ubuntu / Debian systems)
| ps aux                       | List all processes currenty running
| pstree                       | Tree view of running linux processes
| netstat -lp                  | List all listening connections / show processes
| lsof                         | List open files
| file filename                | Will try to tell you what type of file something is
#| find directory -name '*.mp3' | Will list any files in the directory that end in .mp3
| dpkg-query -l                | Lists installed packages
| apt search ftpd              | Lists available packages to install that have ftpd in their name
| top                          | Lists of processes running / CPU usage.  htop similar but nicer, not usually installed by default

## man (Manual)

Sometimes a single command / topic will have many different manual pages.  For example, if you search for printf

```
man -k printf
printf (1)           - format and print data
printf (3)           - formatted output conversion
```

The number in parens is the "page".  Page 1 for printf is the printf shell command.  Page 3 printf is the printf command
from C/C++.  There are man instances where a single topic has more than 1 man page.  Press Q to quit

# Pipes

You can send the output of 1 command into a second command.  Unix/Linux philososphy is to have many simple commands
or applications that do 1 simple task. But the user can combine them using pipes for much more powerful uses.

```
netstat -lp | less
ls | grep jpg
```

The output of netstat would only be shown 1 page at a time because less paginates the output.
The ls command would only show files/dirs that have jpg in them because grep is searching for jpg in output of ls

# Shell Notes

* Directories or files that start with a dot / period are hidden.  You must use ls with the -a switch to see hidden files
* If your shell changes prompt, you may have started an unterminated quote or something, press ctrl-c to cancel command
* If a command is taking forever, ctrl-c to cancel command
* If shell acting weird, or changes to unreadable text, you can try reset command to fix, else just close terminal and start new one

# Server / Daemon applications

A daemon application is usually something that runs in the background (like a Windows service appliation).  Many daemon
applications note this by ending with the letter d.  So ftp package / application is an FTP client and is proably safe
for a user to have on a system, having pure-ftpd would be the server, and is not usually on a secure system.

Common server applications that are very secure

* openssh-server: Secure encrypted remote shell access.  Admins often change the system to use a non-standard port for SSH to make it less obvious.

Common server applications you usually don't want

* telnetd, rlogin, rsh: Remote shell access, lacks encryption
* tftpd, vsftpd, pure-ftpd, proftpd: FTP servers
* linuxvnc, tightvncserver, x11vnc: Remote desktop service, generally not considered secure
* xrdp: Remote desktop service
* samba, nfs-common, nfs-kernel-server: File sharing
* xinetd, inetd: Starts services on demand
* finger: allows someone to query user info from system
* sendmail: email transer (shouldn't be on user system)
* apache, nginx: HTTP (web) servers, (shouldn't be on user system)

# File sharing tools

* transmission: Common torrent application
* *torrent: Generally anything with torrent in the name
* mldonkey, aMule, gnutella: Tools for P2P networking like in the 1990s
* youtube-dl: Downloads videos from youtube

# Hacking tools

I've listed the following ones that I think you might see / common

* *crack: Password cracking tools
* john: Password cracking
* ncaptools, pcaputils, tcpdump: Network sniffing
* wireshark: Network sniffing
* nmap: Network mapping
* hydra: Network logon cracker

For a really complete list of tools, google debian forensics metapackage.  It has almost a hundred tools that might be
considered hacking tools by the scoring engine.

# Service control

Systemd is what controls what is running on modern linux systems.  

```
systemctl list-units --type=service
```

Start, stop, restart:
```
systemctl start clamav-freshclam.service
systemctl stop auditd.service
systemctl restart clamav-freshclam.service
```

# Tools to install

* clamav, clamtk: Antivirus
* ufw, gufw: Firewall

# Updating packages

This could take a while depending on how out of data a system is.  You won't be able to install / remove packages
while the updates are running, but you can generally do most other things.

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

