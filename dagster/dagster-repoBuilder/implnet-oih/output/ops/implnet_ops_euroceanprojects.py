from dagster import op, graph, get_dagster_logger
import subprocess
import os

@op
def euroceanprojects_index(context):
    cwd = os.getcwd()
    print(cwd)
    get_dagster_logger().info(f"CWD is {cwd} ")
    returned_value = subprocess.run('./gleaner.bin -cfg gleanerconfig.yaml  --source euroceanprojects', shell=True, cwd='/usr/src/app')
    # returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/gleanerconfig.yaml  --source euroceanprojects', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    get_dagster_logger().info(f"Gleaner notes are  {returned_value} ")
    r = str('returned value:{}'.format(returned_value))
    get_dagster_logger().info(f"Gleaner notes are  {r} ")
    return r

@op
def euroceanprojects_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s summoned/euroceanprojects', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def euroceanprojects_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/nabuconfig.yaml  prune -s prov/euroceanprojects', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_euroceanprojects():
    harvest = euroceanprojects_index()
    load1 = euroceanprojects_rdf(harvest)
    load2 = euroceanprojects_prov(load1)


