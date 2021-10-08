# Forensic Question 1:

```
netstat -nlp
```

netcat running, listening on a port

# Forensic Question 2:

Is john on the system?

which john to determine the full path for john

# Invalid users?

System settings / Users applications.

```
ls /home
sudo cat /etc/passwd
sudo cat /etc/shadow
```

Users credence and gellert don't belong.
Users tina and jacob don't have passwords set

```
deluser credence
deluser gellert
rm -rf /home/credence
rm -rf /home/gellert
```

Set passwd for users without them

```
passwd tina
passwd jacob
```

** This scored me points, but Tina still able to login without a password, wat!? **

theseus user missing, add him

```
adduser theseus
```

queenie shouldn't be an adminstrative user
She is in the sudo group

```
cat /etc/group

deluser queenie sudo
```

# Command format
deluser user group
Services / Daemons we don't want

```
netstat -lp
ps aux
```

See vsftpd and smbd running, those aren't allowed.  Uninstall the applications.

```
apt remove samba vsftpd
```

That netcat thing that is running, where is that.

Not sure how I found it, but it was in crontab

```
sudo crontab -l
sudo crontab -e 
```

# Auto updates

Set Ubuntu auto-updates to auto install every day

# Firewall

```
ufw enable
```

# Bad files

Searched user directories using find.

```
rm /home/jacob/Documents/payroll.xlsx
```

Remove autologin user

(from the gui control for user settings could remove it)

or editting
/etc/lightdm/lightdm.conf

Make the username in autologin-user=<username> a blank user

Add allow-guest=false

** This only scored points if I applied the fix in /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf **

# Update password security requirements

```
vi /etc/login.defs
```

Set max password age (PASS_MAX_DAYS) to 90, min (PASS_MIN_DAYS) to 10, and warn (PASS_WARN_AGE) to 7.
Max login tries to 5 (this is supposed to get overrridden by PAM confgiguration)

```
vi /etc/pam.d/common-auth
```

Per cyber training materials, add the following:

```
auth required pam_tally2.so deny=5 onerr=fail unlock_time=1800
```

Remember passwords > 3

Per google, edit /etc/pam.d/common-password

change
   password required pam_pwhceck.so nullok
to
   password required pam_pwcheck.so nullok remember=3

This scored me points, but doesn't actually work..... fail.....


# Remove bad apps

```
apt remove john
```



# Weird things they do:

I didn't figure this out on my own, i got this via cheating...

Remove google.com from /etc/hosts


