# Competition_Olympics-Billiard
---

## Environment

Olympics-Billiard is one of the AI-Olympics testbeds built on [`olympics-engine`](https://github.com/jidiai/olympics_engine).  
Two teams (red and blue) start at one side of the table and on the other side of the table lies a pile of balls in equal numbers of red and blue.
On four coners there are holes drawn as green line such that the player scores if the ball of its color touch the green line and receive penlity
if the player itself touch the green line. The game end when reaching maximum step (500 time-step) or when either player manage to hit all the ball
of its color into the hole.

<img src='./img/billiard_competition_render.gif'>

---
## Dependency

>conda create -n olympics python=3.8.5

>conda activate olympics

>pip install -r requirements.txt

---

## Run a game

>python olympics_engine/main.py

---


## How to test submission

You can locally test your submission. At Jidi platform, we evaluate your submission as same as *run_log.py*

For example,

>python run_log.py --my_ai "rl" --opponent "random"

in which you are controlling agent 1 which is green.

## Ready to submit

1. Random policy --> *agents/random/submission.py*
2. RL policy --> *all files in agents/rl*

