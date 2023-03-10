#!/bin/bash
cd $(dirname $0)
for id in `ps -ef|grep "xxx" | grep -v "grep" |awk '{print $2}'`
do
kill -9 $id
echo "kill $id"
done

#切换conda/pipenv...
source ~/anaconda3/etc/profile.d/conda.sh
conda activate garage_manager
nohup python xxx.py > nohup.out 2>&1 &
