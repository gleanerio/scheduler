from dagster import op, graph, get_dagster_logger
import subprocess
import os

@op
def unavco_index(context):
    cwd = os.getcwd()
    print(cwd)
    get_dagster_logger().info(f"CWD is {cwd} ")
    returned_value = subprocess.run('./gleaner.bin -cfg gleanerconfig.yaml  --source unavco', shell=True, cwd='/usr/src/app')
    # returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/gleanerconfig.yaml  --source unavco', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    get_dagster_logger().info(f"Gleaner notes are  {returned_value} ")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def unavco_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s summoned/unavco', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def unavco_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s prov/unavco', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_unavco():
    harvest = unavco_index()
    # load1 = unavco_rdf(harvest)
    # load2 = unavco_prov(load1)

