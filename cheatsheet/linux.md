# Common Linux Commands

| Command                      | What it does
|------------------------------|-------------
| ls                           | List files in directory
| cd dirname                   | Change directory to dirname
| cd ..                        | Go back one directory
| cat filename                 | Print the contents of the file to the screen (don't do this with binary files, zips, etc)
| less filename                | Print the contents of a file, but you can PgDown/PgUp to read a large file
| gedit filename               | Open text editor gedit (easy to use) to edit file named filename
| nano filename                | Open command line text editor to edit a file named filename
| vi filename                  | Open command line text editor to edit a file. NOT EASY TO USE! If something tells you to use vi, try using gedit or nano instead!
| rm filename                  | Remove a file
| mv filenameold fnnew         | Moves / Renames a file from old name to new name
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
| find directory -name '*.mp3' | Will list any files in the directory that end in .mp3
| dpkg-query -l                | Lists installed packages
| apt search ftpd              | Lists available packages to install that have ftpd in their name
| top                          | Lists of processes running / CPU usage.  htop similar but nicer, not usually installed by default

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
* john: Password crackign
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

