from dagster import op, graph
import subprocess

@op
def cioos(context):
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_queue.yaml  --source cioosatlantic', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def cioos_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihqueue.yaml  prune -s summoned/cioosatlantic', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def cioos_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihqueue.yaml  prune -s prov/cioosatlantic', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest():
    harvest = cioos()
    load1 = cioos_rdf(harvest)
    load2 = cioos_prov(load1)


