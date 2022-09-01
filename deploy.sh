#!/usr/bin/env bash

function run_cmd() {
    ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ubuntu@$SERVER_IP "$*"
}

eval $(ssh-agent)
ssh-add - <<< $SSH_KEY
run_cmd "git -C PruRobot fetch origin master"
run_cmd "git -C PruRobot reset --hard origin/master"
run_cmd "sudo systemctl restart prurobot"
eval $(ssh-agent -k)
