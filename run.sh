#!/usr/bin/env bash

cd ./src

chmod a+x my_word_count.py
chmod a+x my_running_median.py

python my_word_count.py ../wc_input ../wc_output/wc_result.txt
python my_running_median.py ../wc_input ../wc_output/med_result.txt
