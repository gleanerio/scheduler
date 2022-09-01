from dagster import op, graph
import subprocess

@op
def marinetraining(context):
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source marinetraining', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def marinetraining_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/marinetraining', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def marinetraining_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/marinetraining', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_marinetraining():
    harvest = marinetraining()
    load1 = marinetraining_rdf(harvest)
    load2 = marinetraining_prov(load1)


