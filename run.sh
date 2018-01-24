#!/bin/bash


while [ 1 -eq 1 ]; do

    # trap ctrl-c and call ctrl_c()
    trap ctrl_c INT

    function ctrl_c() {
        kill $p1;
    }

    python main.py &
    p1=$!

    git fetch > build_log.txt 2>&1
    if [ -s build_log.txt ]
    then
        # kill process
        echo "Updates detected, restarting...";
        ctrl_c;
    fi
    sleep 20;
done

exit;
