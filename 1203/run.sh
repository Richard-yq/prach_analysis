#!/bin/bash
cd "$(dirname "$0")"
python3 distance-result.py && open distance_attack_results.png distance_success_rate.png
