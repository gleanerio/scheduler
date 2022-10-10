from dagster import op, graph, get_dagster_logger
import subprocess
import os

@op
def name59_index(context):
    cwd = os.getcwd()
    print(cwd)
    get_dagster_logger().info(f"CWD is {cwd} ")
    returned_value = subprocess.run('./gleaner.bin -cfg gleanerconfig.yaml  --source name59', shell=True, cwd='/usr/src/app')
    # returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/gleanerconfig.yaml  --source name59', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    get_dagster_logger().info(f"Gleaner notes are  {returned_value} ")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def name59_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s summoned/name59', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def name59_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s prov/name59', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_name59():
    harvest = name59_index()
    load1 = name59_rdf(harvest)
    load2 = name59_prov(load1)

