#!/bin/sh

python3 clean.py
python3 test-insert_one.py
python3 test-find_one.py
python3 profiling.py
