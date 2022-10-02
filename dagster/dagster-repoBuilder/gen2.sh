#!/bin/bash

## declare an array variable for all the source names
#declare -a arr=("element1" "element2" "element3")
arr=($(grep name: oih_local.yaml | grep -v propername | awk '{print $2}' ))

echo "from dagster import repository"

## now loop through the above array
for SOURCE in "${arr[@]}"
do
   echo "from gleaner.jobs.implnet_jobs_$SOURCE import implnet_job_$SOURCE"
   echo "from gleaner.schedules.implnet_sch_$SOURCE  import implnet_sch_$SOURCE"
   ja+=("implnet_job_$SOURCE")
   sa+=("implnet_sch_$SOURCE")
done

echo " "

echo "@repositry"
echo "def gelaner():"

(IFS=",$IFS"; printf '\tjobs = [%s]\n' "${ja[*]}")
(IFS=",$IFS"; printf '\tschedules = [%s]\n' "${sa[*]}")

echo "        return jobs + schedules"

