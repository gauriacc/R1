#!/bin/bash
#Add used and days column from Jenkins to output.csv file

echo "used,days" > /home/ansiblecontrol/predicttbs/output.csv
echo $used,$days >> /home/ansiblecontrol/predicttbs/output.csv

# Remove blank lines in dataset file
 sed -i '/^$/d' predict.csv

# Calculate WL for the dates
awk 'NR-1{print $0-p}{p=$0}' predict.csv > pred.csv
sed  -i '1i wl' pred.csv
sed -i -e 's/^/,/' pred.csv
paste --delimiter='' predict.csv pred.csv > predictinp.csv

# Calculate no of days for each row with reference to first row
# extract the date column in another file
cut -d',' -f2 predictinp.csv|sed '1d' > datafile
while read -r line
do
first=`date -d $line  +%Y-%m-%d`
echo $first >> datafile1

done < datafile
B=`sed -n '1p' datafile1`
echo $B
firstdt=`echo $(date -d $B +%s)`
echo $firstdt
while read -r line
do
days=`echo $(( ($(date -d $line +%s) - $(date -d $B +%s)) / 86400 ))`
echo $days >> datafile2

done < datafile1
sed -i '1i days' datafile2
sed -i -e 's/^/,/' datafile2
 paste --delimiter='' predictinp.csv datafile2 > predictinp1.csv
