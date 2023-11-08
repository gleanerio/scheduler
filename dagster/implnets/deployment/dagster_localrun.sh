#!/bin/bash
# https://dockerswarm.rocks/traefik/
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


if [ ! $envfile ]
  then
     envfile=".env"
#      envfile="portainer.env"
fi

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

## need to docker (network|volume) ls | grep (traefik_proxy|traefik_proxy) before these calll
## or an error will be thrown
#echo "This message is OK **Error response from daemon: network with name traefik_proxy already exists.** "
if [  "$(docker network ls  | grep ${GLEANERIO_DOCKER_HEADLESS_NETWORK})" ] ; then
   echo ${GLEANERIO_DOCKER_HEADLESS_NETWORK} netowrk exists;
else
   echo creating network
   if [ "$(docker info | grep Swarm | sed 's/Swarm: //g' | tr -d ' ')" == "inactive"  ]; then
        echo Not Swarm
        if `docker network create -d bridge --attachable ${GLEANERIO_DOCKER_HEADLESS_NETWORK}`; then
           echo 'Created network ${GLEANERIO_DOCKER_HEADLESS_NETWORK}'
        else
           echo "ERROR: *** Failed to create local network. "
            exit 1
        fi
   else
        echo Is Swarm
        if `docker network create -d overlay --attachable ${GLEANERIO_DOCKER_HEADLESS_NETWORK}`; then
          echo 'Created network ${GLEANERIO_DOCKER_HEADLESS_NETWORK}'
        else
            echo "ERROR: *** Failed to create swarm network.  "
            exit 1
        fi
   fi

fi


#echo NOTE: Verify that the traefik_proxy network  SCOPE is swarm


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
