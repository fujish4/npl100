#!/bin/sh

cut --fields=1 hightemp.txt > col1_test.txt
diff --report-identical-files col1.txt col1_test.txt

cut --fields=2 hightemp.txt > col2_test.txt
diff --report-identical-files col2.txt col2_test.txt