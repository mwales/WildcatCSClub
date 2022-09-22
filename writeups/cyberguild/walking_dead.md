# Walking Dead Ubuntu Image

An even older 12.04 Ubuntu Image

No scoring system built in, just has a spreadsheet documenting required configuration changes to make it secure

Changes that they recommended that I haven't seen yet in other challenges:

# Accounts and passwords

To lock an account of a user:

```
sudo passwd -l zombie_username
```

Not sure why I wouldn't just delete the account if I thought they were a malicious user

Can view the password status of a user

```
passwd --status username
```

Shows login name, password status as (L)ocked or (NP)o password, 
date of last change, min age, max age, warning period, inactivity period


