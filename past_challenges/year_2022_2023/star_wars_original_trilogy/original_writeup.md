# Star Wars: The Original Trilogy

The 2nd in a series of 3 progressively more difficult challenges.  Game has 2
pseudorandom star wars characters have a battle.  The students are given the
source code (python) for the game to exampine. You are supposed to guess
the winner correctly 7 times in a row.

The second challenge that source has been modified to fix the bug in the PRNG.
Instead of using a fixed seed, this game now uses a seed that is based on the
number of seconds elapsed since Unix epoch.

## Hints

* Try running the diff to tool to compare the 2 versions and see how each
  version differs (maybe also suggest meld or kompare for the diffing)
* A PRNG will always give the same pseudo random numbers if the seed is not
  changed
* Ask the student to explain how the seed is determined for this challenge

## Solution

Diff the source of this version against the prequel source version.

```
$ diff battle.py ../7_star_wars_prequel/battle.py 
5,8c5,6
< gNames = [ "Boba Fett",
<            "Darth Vader",
<            "Princess Leia",
<            "Luke Skywalker",
---
> gNames = [ "Darth Maul",
>            "Obi-Wan",
10c8,10
<            "Yoda" ]
---
>            "Yoda",
>            "Queen Amidala",
>            "Jar Jar Binks" ]
42d41
<       time.sleep(10)
72c71
<       random.seed(int(time.time()))
---
>       random.seed(0)
```

Some of the character names have changed, but that isn't a big deal.  The
interesting part of this challenge is how the PRNG is seeded.  The int()
function of the time value ensures that the time is a whole number of
seconds.

Play 2 games side by side, and start them within 1 second of each other.  You
can either script the execute of 2 terminal windows or just have 2 people try it
at the same time.  If each game starts with the same 2 characters battling,
you likely have 2 game instances running with an identical PRNG sequence.

Now it's just like the first challenge.  Play a turn in game A and notice who
wins.  In game B choose the winner that you know wins.  Repeat 7 times.

```
wildcat{jedi_mind_trick_of_defeating_prng}
```
