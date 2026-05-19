#!/bin/bash
# This script runs the nr-softmodem command for 10 seconds, terminates it,
# waits 3 seconds for the USRP hardware to release, and repeats.

# Absolute path to the ran_build directory
TARGET_DIR="/root/richard/openairinterface5g/cmake_targets/ran_build/build"

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory $TARGET_DIR does not exist."
    exit 1
fi

cd "$TARGET_DIR" || exit 1

echo "Starting nr-softmodem loop. Press Ctrl+C in this terminal to stop the loop."

# Counter for tracking runs
count=0

while true; do
    count=$((count+1))
    echo "=================================================="
    echo "Starting run #$count at $(date)"
    echo "=================================================="
    
    # We use sudo timeout to run the command for exactly 10 seconds.
    # --signal=2 sends SIGINT (equivalent to Ctrl+C) to terminate cleanly.
    sudo timeout --signal=2 10 ./nr-softmodem \
        -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.usrpb210.conf \
        --gNBs.[0].min_rxtxtime 6 \
        -E \
        --continuous-tx \
        --log_config.PRACH_debug \
        --telnetsrv \
        --telnetsrv.shrmod o1 \
        2>&1 | awk '{ cmd = "date +\"[%Y-%m-%d %H:%M:%S.%3N]\""; cmd | getline ts; close(cmd); print ts, $0; fflush(); }' >> ~/OAI_gNB.log

    echo "Run #$count finished/terminated. Waiting 3 seconds for USRP to release..."
    sleep 3
done
