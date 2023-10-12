

# RUNNING LOCALLY
* You need to point at a docker STACK, or portainer endpoint... A local workstation docker is usually not a STACK.
* set the ENV variables;  I use the env file plugin in pycharm 
* 
`cd dagster/implnets/generatedCode/implnet-eco/output
python -m dagster dev `

## To run a job:
`cd dagster/implnets/generatedCode/implnet-eco/output
python -m dagster job execute -f jobs/implnet_jobs_ecrr_examples.py  -j implnet_jobs_ecrr_examples`

## also can just be dagster
cd dagster/implnets/generatedCode/implnet-eco/output
(do some magic env: eg `export $(sed  '/^[ \t]*#/d' $envfile |  sed '/^$/d' | xargs)` )
* dagster job list -w workspace.yaml 
* dagster job execute -f jobs/implnet_jobs_ecrr_examples.py  -j implnet_jobs_ecrr_examples
