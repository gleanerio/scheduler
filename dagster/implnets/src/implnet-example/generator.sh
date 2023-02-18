#!/bin/bash

echo "USAGE:  ./generator.sh ./path/to/gleanerconfig.yaml"
echo "---  building src diretory "

# TODO
# take the input file as a CLI arg
# take the output directory as a CLI arg

# set up vars
REPOFILE="./output/repositories/repository.py"
WORKSPACEFILE="./output/workspace.yaml"
#HOUR=0

# set up temp directory
tmp_dir=$(mktemp -d -t drb-XXXXXXXXXX)
#echo $tmp_dir

# declare an array variable for all the source names
arr=($(grep name: $1 | grep -v propername | awk '{print $3}' ))

# Vars to spread sources over multiple days (here 7)
AL=$((${#arr[@]}-1))  # take off one since we range from 0 not 1
INC=$((24*7/$AL))  # Spread over a week

# now loop through the array of Gleaner sources
#for SOURCE in "${arr[@]}"
for i in $(seq 0 $AL)
do
    SOURCE=${arr[$i]}
    Q=$(( ($i * $INC)/24))
    Q2=$((Q%7))
    R=$(( ($i * $INC)%24 ))

    # or do whatever with individual element of the array
    cp ./templates/implnet_ops_SOURCEVAL.py $tmp_dir/implnet_ops_$SOURCE.py
    cp ./templates/implnet_jobs_SOURCEVAL.py $tmp_dir/implnet_jobs_$SOURCE.py
    cp ./templates/implnet_sch_SOURCEVAL.py $tmp_dir/implnet_sch_$SOURCE.py

    sed -i  's/SOURCEVAL/'$SOURCE'/g' $tmp_dir/*

    # update the default cron string in the schedule file
    # this cron line only runs on Sunday (0), but we can run dagster graphs
    # through the web UI
    #    MODHOUR=$(($HOUR%23))  # 0 and 24 are the same on the clock, so mod 23
    #    HOUR=`expr $HOUR + 1`
    sed -i  's|0 24 \* \* \*|0 '$R' \* \* '$Q2'|g' $tmp_dir/implnet_sch_$SOURCE.py

    mkdir --parents ./output/ops/;  mv $tmp_dir/implnet_ops_$SOURCE.py ./output/ops
    mkdir --parents ./output/jobs/;  mv $tmp_dir/implnet_jobs_$SOURCE.py ./output/jobs
    mkdir --parents ./output/schedules/;  mv $tmp_dir/implnet_sch_$SOURCE.py ./output/schedules
done

rm -rf $tmp_dir

echo "---  building repository file "
mkdir --parents ./output/repositories/;

# single > to erase old files...
echo "from dagster import repository" > $REPOFILE

## now loop through the source array
for SOURCE in "${arr[@]}"
do
   echo "from jobs.implnet_jobs_$SOURCE import implnet_job_$SOURCE"   >> $REPOFILE
   echo "from schedules.implnet_sch_$SOURCE  import implnet_sch_$SOURCE"   >> $REPOFILE
   ja+=("implnet_job_$SOURCE")
   sa+=("implnet_sch_$SOURCE")
done

echo " "   >> $REPOFILE

echo "@repository"   >> $REPOFILE
echo "def gleaner():"   >> $REPOFILE
(IFS=",$IFS"; printf '\tjobs = [%s]\n' "${ja[*]}")  >> $REPOFILE
(IFS=",$IFS"; printf '\tschedules = [%s]\n' "${sa[*]}") >> $REPOFILE
echo " "   >> $REPOFILE
echo -e "\treturn jobs + schedules"   >> $REPOFILE


# Build workspace file

echo "load_from:
  - python_file:
      relative_path: \"repositories/repository.py\"
      working_directory: .
">> $WORKSPACEFILE
