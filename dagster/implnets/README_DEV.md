
Note: Moved the dagster.yaml that defines the container based configuraiton to deployment.


To start a dev instance, you can type

set the environment variables in deploymnet/envFile.env 
   * 
   * if using jetbrains/pycharm, use a shell script, and add the env variables.


`dagster dev --workspace workspace_dev.yaml`


You can go to deployment, and get the code reloaded by reloading the definitions.

## Using local deployment and containers

in deploy, you can use the dagster_local.sh

when combined with the proper env, it will use the workflows.yaml in config/$PROJECT/workflows.yam
a
In prep for using a service that can mount the gleaner/nabu configs, the local 
also creates 'file' configs using   config/$PROJECT/gleanerconfig.yaml and  config/$PROJECT/nabuconfig.yaml


