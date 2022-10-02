from dagster import op, graph
import subprocess

@op
def edmerp(context):
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source edmerp', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def edmerp_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/edmerp', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def edmerp_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/edmerp', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_edmerp():
    harvest = edmerp()
    load1 = edmerp_rdf(harvest)
    load2 = edmerp_prov(load1)


