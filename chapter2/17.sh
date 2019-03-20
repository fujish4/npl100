#!/bin/sh

cut --fields=1 hightemp.txt | sort | uniq > esult_test.txt

python 17.py | sort > result.txt

diff --report-identical-files result.txt result_text.txt