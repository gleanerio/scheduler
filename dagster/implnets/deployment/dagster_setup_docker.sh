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
if [  "$(docker network ls  | grep -${GLEANERIO_DOCKER_HEADLESS_NETWORK})" ] ; then
   echo ${GLEANERIO_DOCKER_HEADLESS_NETWORK} netowrk exists;
else
   echo creating network
   if [ "$(docker info | grep Swarm | sed 's/Swarm: //g')" == "inactive" ]; then
        echo Not Swarm
        if `docker network create -d bridge --attachable ${GLEANERIO_DOCKER_HEADLESS_NETWORK}`; then
           echo 'Created network ${GLEANERIO_DOCKER_HEADLESS_NETWORK}'
        else
           echo "ERROR: *** Failed to create local network. "
           # exit 1
        fi
   else
        echo Is Swarm
        if `docker network create -d overlay --attachable ${GLEANERIO_DOCKER_HEADLESS_NETWORK}`; then
          echo 'Created network ${GLEANERIO_DOCKER_HEADLESS_NETWORK}'
        else
            echo "ERROR: *** Failed to create swarm network.  "
            #exit 1
        fi
   fi

fi

#echo NOTE: Verify that the traefik_proxy network  SCOPE is swarm

echo added network  ${GLEANERIO_DOCKER_HEADLESS_NETWORK}

docker volume create dagster-postgres
docker volume create dagster-storage

if [  "$(docker config ls  | grep -${GLEANERIO_GLEANER_CONFIG_PATH})" ] ; then
   echo ${GLEANERIO_GLEANER_CONFIG_PATH} config exists;
else
   echo creating config

      if `docker config create gleaner-${PROJECT} ../configs/${PROJECT}/gleanerconfig.yaml`; then
         echo 'Created gleaner config gleaner-${PROJECT} ${GLEANERIO_GLEANER_CONFIG_PATH}'
      else
         echo "ERROR: *** Failed to create docker/potainer config. gleaner-${PROJECT} ${GLEANERIO_GLEANER_CONFIG_PATH}"
         echo "see if config exists "
         # exit 1
      fi
fi

if [  "$(docker config ls  | grep -${GLEANERIO_NABU_CONFIG_PATH})" ] ; then
   echo ${GLEANERIO_NABU_CONFIG_PATH} config exists;
else
   echo creating config

      if `docker config create nabu-${PROJECT} ../configs/${PROJECT}/nabuconfig.yaml`; then
         echo 'Created gleaner config  nabu-${PROJECT} ${GLEANERIO_NABU_CONFIG_PATH}'
      else
         echo "ERROR: *** Failed to create  create docker/potainer config. nabu-${PROJECT} ${GLEANERIO_NABU_CONFIG_PATH} "
         echo "see if config exists "
         # exit 1
      fi
fi

if [  "$(docker config ls  | grep -${GLEANERIO_WORKSPACE_CONFIG_PATH})" ] ; then
   echo ${GLEANERIO_WORKSPACE_CONFIG_PATH} config exists;
else
   echo creating config

      if `docker config create workspace-${PROJECT} ../configs/${PROJECT}/workspace.yaml`; then
         echo 'Created gleaner config  workspace-${PROJECT} ${GLEANERIO_WORKSPACE_CONFIG_PATH}'
      else
         echo "ERROR: *** Failed to create create docker/potainer config. workspace-${PROJECT} ${GLEANERIO_WORKSPACE_CONFIG_PATH}"
        echo "see if config exists "
        #  exit 1
      fi
fi

if [  "$(docker config ls  | grep -${GLEANERIO_WORKSPACE_CONFIG_PATH})" ] ; then
   echo ${GLEANERIO_WORKSPACE_CONFIG_PATH} config exists;
else
   echo creating config

      if `docker config create workspace-${PROJECT} ../configs/${PROJECT}/workspace.yaml`; then
         echo 'Created gleaner config  workspace-${PROJECT} ${GLEANERIO_WORKSPACE_CONFIG_PATH}'
      else
         echo "ERROR: *** Failed to create create docker/potainer config. workspace-${PROJECT} ${GLEANERIO_WORKSPACE_CONFIG_PATH}"
        echo "see if config exists "
        #  exit 1
      fi
fi
