from dagster import op, graph
import subprocess

@op
def obps(context):
    # returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source obps', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    returned_value = subprocess.call('./gleaner.bin. -cfg /gleaner/wd/rundir/oih_local.yaml  --source obps', shell=True, cwd='/usr/src/app')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def obps_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/obps', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def obps_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/obps', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_obps():
    harvest = obps()
    load1 = obps_rdf(harvest)
    load2 = obps_prov(load1)


