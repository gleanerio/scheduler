# Deployment


## About

This file documents that elements needed for the deployment of a Dagster with Gleaner / Nabu
execution code into Docker / Portainer.

There are a set of required files:

* env variables file
* gleaner/nabu configuration files, without any passwords, servers. Those are handled in the env variables
* docker compose file
* docker networks and volumes for the compose files
*  three files uploaded to docker as configs
    * gleanerconfigs.yaml gleaner/nabu
    * nabuconfigs.yaml - gleaner/nabu
    * workspace.yaml -- dagster
* (opptional/advanced) add a compose_project_PROJECT_override.yaml file with additional containers

PROJECT variable is used to define what files to use, and define, and to setup a separate 'namespace' in traefik labels.

## PORTAINER API KEY

note on how to do this.
''


## Start
For production environments, script, `dagster_setup_docker.sh`  should create the networks, volumes, and 
upload configuration files

1) setup a project in configs directory, if one des not exist
    2)   add gleanerconfig.yaml, nabuconfig.yaml, and workspace.yaml (NOTE NEED A TEMPLATE FOR THIS)
1) copy envFile.env to .env, and edit
2) run  dagster_setup_docker.sh
3) go to  portainer, create a stack with the compose_project.yaml and the variables from the .env file
4) go to https://sched.{HOST}/
5) run a small test dataset.


