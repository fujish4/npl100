#!/bin/sh

sort hightemp.txt --key=3, --numeric-sort --reverse > result_test.txt
python 18.py > result.txt
diff --report-identical-files result.txt result_test.txt