#!/bin/bash

# Kill existing nr-softmodem processes
echo "Checking for existing nr-softmodem processes..."

# Show processes before killing
PROCESSES=$(ps aux | grep nr-softmodem | grep -v grep)
if [ -n "$PROCESSES" ]; then
    echo "Found processes to kill:"
    echo "$PROCESSES"
    echo ""
    
    # Get PIDs
    PIDS=$(pgrep -x nr-softmodem)
    echo "Killing PIDs: $PIDS"
    
    sudo pkill -9 nr-softmodem
    sleep 2
    
    # Verify all processes are killed
    if pgrep -x nr-softmodem > /dev/null; then
        echo "Warning: Some processes still running. Force killing..."
        sudo killall -9 nr-softmodem 2>/dev/null
        sleep 1
    fi
    
    echo "All nr-softmodem processes stopped."
else
    echo "No existing nr-softmodem processes found."
fi
echo "Starting gNB..."

# Change to the build directory
cd ~/openairinterface5g/cmake_targets/ran_build/build

# Run nr-softmodem with specified configuration
# sudo ./nr-softmodem -O /home/oaignb/richard-config/OAI_gNB_twoFDM.conf \
#     --gNBs.[0].min_rxtxtime 6 \
#     -E \
#     --continuous-tx \
#     --log_config.PRACH_debug \
#     --telnetsrv \
#     --telnetsrv.shrmod o1 \
#     > ~/OAI_gNB.log 2>&1

sudo ./nr-softmodem -O /home/oaignb/richard-config/OAI_gNB_twoFDM.conf \
    --gNBs.[0].min_rxtxtime 6 \
    -E \
    --continuous-tx \
    --log_config.PRACH_debug \
    --telnetsrv \
    --telnetsrv.shrmod o1 \
    2>&1 | awk '{ cmd = "date +\"[%Y-%m-%d %H:%M:%S.%3N]\""; cmd | getline ts; close(cmd); print ts, $0; fflush(); }' > ~/OAI_gNB.log
