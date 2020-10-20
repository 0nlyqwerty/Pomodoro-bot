# Pomodoro bot

---

## What is Pomodoro bot?

Pomodoro bot support `Pomodoro Timer` for increase work - efficiency!  
[Pomodoro Technique is ...](https://en.wikipedia.org/wiki/Pomodoro_Technique)  
You can build and run Pomodoro bot on discord via this repo :)

## How can I build bot?

It's super easy.

1. Clone [this](https://github.com/0nlyqwerty/Pomodoro-bot.git) repo to your local

```
clone https://github.com/0nlyqwerty/Pomodoro-bot.git
```

2. Put your bot `token` value into `token.txt` file
3. Build `pomodoro_bot.py` like

```
python pomodoro_bot.py
```

4. Invite your bot to server that you want to use

## How can I use bot?

Here is some command that Pomodoro bot support

### 1. Pomodoro bot help

**!pmdr_help**  
　 → Send Pomodoro command help message to calling channel  
ex) !pmdr_help  
![help_sc](/images/readme_img_help.png)

### 2. Start Pomodoro timer

**!pmdr_start** `Work minute` `Break minute`  
　 → Start pomodoro timer. Start `Break minute` timer after `Work minute` timer. It also notify each time done via send message with mention to calling channel  
ex) !pmdr_start 25 5   
![start_sc](/images/readme_img_start.png)

※ You can't use this command while pomodoro timer already working   
![already_sc](/images/readme_img_already.png)

Notify via message with mention   
![work_done_sc](/images/readme_img_work_done.png)  
...  
![break_done_sc](/images/readme_img_already.png)

### 3. Stop Pomodoro timer

**!pmdr_stop**  
　 → Stop pomodoro timer  
ex) !pmdr_stop  
![stop_sc](/images/readme_img_stop.png)
