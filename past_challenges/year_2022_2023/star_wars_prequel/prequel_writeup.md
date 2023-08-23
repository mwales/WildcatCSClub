# Star Wars: The Prequels

The start of a series of 3 progressively more difficult challenges.  Game has 2
pseudorandom star wars characters have a battle.  The students are given the
source code (python) for the game to exampine. You are supposed to guess
the winner correctly 7 times in a row.

The first game seeds the PRNG with a fixed value.  Thus everygame has the same
exact outcome

## Hints

* Try to play the game a few times and see if you notice any patterns
* A PRNG will always give the same pseudo random numbers if the seed is not
  changed

## Solution

Play 2 games side by side.  Play a turn in game A and notice who wins.  In game
B choose the winner that you know wins.  Repeat 7 times.

```
wildcat{star_wars_ep_1_was_also_pretty_bad}
```
