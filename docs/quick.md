# Notes

### Run Deploy Dagster locally (ROUGH)
Dagster needs a docker instance to run Gleanerio. We usually do this in a remote container.
Basically, you can run a single workflow with the UI from that workflows directory with a `dagster run`

You will need to deploy dagster contiainers to portainer, for a docker swarm
0. get the portatinaer url, and auth token 
0.  SSH to the  make hosting the docker.

1. Pull scheduler repo
2. cd dagster/implnets/deployment
3. create a copy of envFile.env and **edit env variables**
   * PROJECT=eco
   * GLEANERIO_MINIO_ADDRESS and other GLEANERIO_MINIO_* variables
   * GLEANERIO_GRAPH_URL, GLEANERIO_GRAPH_NAMESPACE, GLEANERIO_GRAPH_SUMMARY_NAMESPACE
   * GLEANERIO_DOCKER_URL, GLEANERIO_PORTAINER_APIKEY
   * SCHED_HOSTNAME defaults to sched
5. as noted as noted in (Compose, Environment and Docker API Assets), deploy the configuration to s3. 
6. ~~create network and volumes needed `dagster_setup_docker.sh`~~
7. manually add configs to docker: 

| name | suggested name      | env variable name                 |
|------|---------------------|-----------------------------------|
|  gleaner   | gleaner-{project}   | GLEANERIO_DOCKER_GLEANER_CONFIG   |
| nabu  | nabu-{project}      | GLEANERIO_DOCKER_NABU_CONFIG      |
| workspace  | workspace-{project} | GLEANERIO_DOCKER_WORKSPACE_CONFIG |
|   dagster   | dagster    | GLEANERIO_DOCKER_DAGSTER_CONFIG   |

dagster from:dagster/implnets/deployment/dagster.yaml

7. add configs to S3/Minio. 
   8. scheduler/configs/gleanerconfig.yml
   9. scheduler/configs/tenant.yml
8. then you can run a command. in runConfigs there are PyCharm run files
   11. `cd dagster/implnets/workflows/ingest`
   12. `dagster run`

**NEED MORE EXAMPLES**

