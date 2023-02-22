# Competition_Olympics-Billiard
---

## Environment



---
## Dependency

>conda create -n olympics python=3.8.5

>conda activate olympics

>pip install -r requirements.txt

---

## Run a game

>python olympics_engine/main.py

---

## Train a baseline agent 

>python rl_trainer/main.py

You can also locally evaluate your trained model by executing:

>python evaluation_local.py --my_ai rl --opponent random --episode=50


## How to test submission

You can locally test your submission. At Jidi platform, we evaluate your submission as same as *run_log.py*

For example,

>python run_log.py --my_ai "rl" --opponent "random"

in which you are controlling agent 1 which is green.

## Ready to submit

1. Random policy --> *agents/random/submission.py*
2. RL policy --> *all files in agents/rl*

