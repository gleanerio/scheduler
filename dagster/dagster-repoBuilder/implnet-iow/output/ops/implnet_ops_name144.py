from dagster import op, graph, get_dagster_logger
import subprocess
import os

@op
def name144_index(context):
    cwd = os.getcwd()
    print(cwd)
    get_dagster_logger().info(f"CWD is {cwd} ")
    returned_value = subprocess.run('./gleaner.bin -cfg gleanerconfig.yaml  --source name144', shell=True, cwd='/usr/src/app')
    # returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/gleanerconfig.yaml  --source name144', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    get_dagster_logger().info(f"Gleaner notes are  {returned_value} ")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def name144_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s summoned/name144', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def name144_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s prov/name144', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_name144():
    harvest = name144_index()
    load1 = name144_rdf(harvest)
    load2 = name144_prov(load1)

