#!/bin/bash
sleep 5
tmux new-session -d -s rosc 'roscore'
tmux new-session -d -s inst 'rosrun athena insta.py'
tmux new-session -d -s serv 'rosrun athena servo.py'
while true
do
sess=$(tmux ls | wc -l)
if [[ $sess < 3 ]]
then
tmux kill-server
tmux new-session -d -s rosc 'roscore'
tmux new-session -d -s inst 'rosrun athena insta.py'
tmux new-session -d -s serv 'rosrun athena servo.py'
fi
echo $sess
sleep 0.5
done
