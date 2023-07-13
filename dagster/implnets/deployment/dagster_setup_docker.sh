#!/bin/bash
# https://dockerswarm.rocks/traefik/
helpFunction()
{
   echo "setup dagster network and volume"
   echo "Usage: $0 -e envfile  -u"
   echo -e "\t-e envfile to use"

   exit 1 # Exit script after printing help
}


while getopts "e:u" opt
do
   case "$opt" in
      e ) envfile="$OPTARG" ;;

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
    export $(cat ${envfile} | xargs)
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
if  `docker network inspect ${GLEANER_HEADLESS_NETWORK} | grep -q "swarm"` ; then
   echo ${GLEANER_HEADLESS_NETWORK} netowrk exists as swarm
else
   echo Above Error \" No such network: \" is OK.
   echo creating network
   if `docker network create -d overlay --attachable ${GLEANER_HEADLESS_NETWORK}`; then
     echo 'Created network ${GLEANER_HEADLESS_NETWORK}'
   else
    echo "ERROR: *** Failed to create network. Non-local setup needs to be a swarm "
    exit 1
  fi
fi

#echo NOTE: Verify that the traefik_proxy network  SCOPE is swarm

docker volume create ${GLEANER_CONFIG_VOLUME}

echo added network  ${GLEANER_HEADLESS_NETWORK}  and aolume ${GLEANER_CONFIG_VOLUME}

