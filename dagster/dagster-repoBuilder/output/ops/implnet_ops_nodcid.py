from dagster import op, graph, get_dagster_logger
import subprocess
import os

@op
def nodcid_index(context):
    cwd = os.getcwd()
    print(cwd)
    get_dagster_logger().info(f"CWD is {cwd} ")
    returned_value = subprocess.run('./gleaner.bin -cfg gleanerconfig.yaml  --source nodcid', shell=True, cwd='/usr/src/app')
    # returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/gleanerconfig.yaml  --source nodcid', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    get_dagster_logger().info(f"Gleaner notes are  {returned_value} ")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def nodcid_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s summoned/nodcid', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def nodcid_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s prov/nodcid', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_nodcid():
    harvest = nodcid_index()
    load1 = nodcid_rdf(harvest)
    load2 = nodcid_prov(load1)


