#!/bin/bash

tmp_dir=$(mktemp -d -t drb-XXXXXXXXXX)
echo $tmp_dir

## declare an array variable for all the source names
#declare -a arr=("element1" "element2" "element3")
arr=($(grep name: oih_local.yaml | grep -v propername | awk '{print $2}' ))

## now loop through the above array
for SOURCE in "${arr[@]}"
do
   # or do whatever with individual element of the array
   cp ./templates/implnet_ops_SOURCEVAL.py $tmp_dir/implnet_ops_$SOURCE.py
   cp ./templates/implnet_jobs_SOURCEVAL.py $tmp_dir/implnet_jobs_$SOURCE.py
   cp ./templates/implnet_sch_SOURCEVAL.py $tmp_dir/implnet_sch_$SOURCE.py

   sed -i  's/SOURCEVAL/'$SOURCE'/g' $tmp_dir/*

   mv $tmp_dir/implnet_ops_$SOURCE.py ./output/ops
   mv $tmp_dir/implnet_jobs_$SOURCE.py ./output/jobs
   mv $tmp_dir/implnet_sch_$SOURCE.py ./output/schedules
done

rm -rf $tmp_dir

