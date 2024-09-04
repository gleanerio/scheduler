#!/bin/bash
# https://dockerswarm.rocks/traefik/
set -euxo pipefail

helpFunction()
{
   echo "setup dagster networks"
   echo "Usage: $0 -e envfile  -u"
   echo -e "\t-e envfile to use"
   echo -e "\t-u DO NOT RUN detached"
   exit 1 # Exit script after printing help
}
detached=true

while getopts "e:u" opt
do
   case "$opt" in
      e ) envfile="$OPTARG" ;;
      u ) detached=false ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done


envfile=".env"

if [ -f $envfile ]
  then
    echo "using " $envfile
    export $(sed  '/^[ \t]*#/d' $envfile |  sed '/^$/d' | xargs)

  else
    echo "missing environment file. pass flag, or copy and edit file"
    echo "cp envFile.env .env"
    echo "OR"
    echo "cp {yourenv}.env .env"

    exit 1
fi

echo DO NOT FORGET TO USE pygen/makefile REGNERATE THE CODE.

echo run as detached: $detached

if [ -f compose_local_${PROJECT}_override.yaml ]
  then
    override_file="-f compose_local_${PROJECT}_override.yaml"
  else
    override_file=""
fi
# uses swarm :
if [ "$detached" = true  ]
  then
    docker compose -p dagster  --env-file $envfile  -f compose_local.yaml  $override_file up  -d
  else
    docker compose -p dagster --env-file $envfile  -f compose_local.yaml  $override_file up
fi

echo DO NOT FORGET TO USE pygen/makefile REGNERATE THE CODE.
