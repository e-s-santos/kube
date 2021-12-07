#/bin/bash
export path=/home/teste/lab
cd $path

for i in back conecta cron front ingress; do cd $i; ./exec.sh; cd ..; done 
