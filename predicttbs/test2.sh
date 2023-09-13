#!/bin/bash

#while read -r line
#do
#first=`date -d $line  +%Y-%m-%d`
#echo $first >> datafile1
#
#done < datefile
#B=`sed -n '1p' datafile1`
#echo $B
#firstdt=`echo $(date -d $B +%s)`
#echo $firstdt
#while read -r line
#do
#days=`echo $(( ($(date -d $line +%s) - $(date -d $B +%s)) / 86400 ))`
#echo $days >> datafile2

#done < datafile1
sed -i '1i days' datafile2
sed -i -e 's/^/,/' datafile2


