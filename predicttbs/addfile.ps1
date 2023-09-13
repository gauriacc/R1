$tbsname='USERS'
$filename=$args[0]
$filesize=$args[1]
echo exit | sqlplus -s sys/tiger123 as sysdba "@C:\temp\addfile.sql" $tbsname $filename $filesize
