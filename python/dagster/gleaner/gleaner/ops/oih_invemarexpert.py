from dagster import op, graph
import subprocess

@op
def invemarexpert(context):
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source invemarexpert', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def invemarexpert_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/invemarexpert', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def invemarexpert_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/invemarexpert', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_invemarexpert():
    harvest = invemarexpert()
    load1 = invemarexpert_rdf(harvest)
    load2 = invemarexpert_prov(load1)


