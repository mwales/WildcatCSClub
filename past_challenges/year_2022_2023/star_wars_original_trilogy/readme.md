Name: Star Wars: Original Trilogy

Pre-requisite: [Star Wars Prequel Trilogy](../star_wars_prequel/readme.md)

Category:  Cryptography

Attachments:
* [battle.py](battle.py) : This is the main file to analyze
* [pictures.ans](pictures.ans) : Just put this file in the sam edirectory as battle.py
* [flag.txt](flag.txt) : You wouldn't have this file for the real challenge when  it's online

Message:

Well, that was embarassing. The challenge has been fixed now.

Now as soon as you connect to the server the PRNG gets seeded with the number
of seconds that have passed since Jan 1, 1970 (epoch).  So now everytime you
start the game you will get a different seed to start the game. Good luck
defeating that!  Ha Ha Ha

To get the flag for this challenge, you need to predict the winner of my Star
Wars battle game 7 times in a row!

Connect to the original trilogy battle game at the following port:

This challenge was hosted online, but now you can try it out by running battle.py on your own machine.

<details>
<summary>Click to reveal Hint #1</summary>
Try using the <b>diff</b> command to compare this version of the challenge versus
the last version of the challenge.  What parts are different?  What
differences are important?  And how can we exploit them?
</details>

<details>
<summary>Click to reveal Hint #2</summary>
We can either figure out how a PRNG works / changes state, or find a way
to seed 2 PRNGs with the same seed value, and watch the state of 1 of them
to predict the future state of the other.  How is the PRNG seeded?
</details>

[ Solution Write-up - CONTAINS SPOILERS](original_writeup.md)
