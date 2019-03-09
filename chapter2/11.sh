#!/bin/sh

sed 's/\t/ /g' hightemp.txt
tr '\t' ' ' < hightemp.txt
expand --tabs=1 hightemp.txt