#!/bin/bash
sleep 5
tmux new-session -d -s ath 'roscore'
tmux new-session -d -s inst 'rosrun athena insta.py'
tmux new-session -d -s serv 'rosrun athena servo.py'
