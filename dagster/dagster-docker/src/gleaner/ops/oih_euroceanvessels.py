from dagster import op, graph
import subprocess

@op
def euroceanvessels(context):
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source euroceanvessels', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def euroceanvessels_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/euroceanvessels', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def euroceanvessels_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/euroceanvessels', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_euroceanvessels():
    harvest = euroceanvessels()
    load1 = euroceanvessels_rdf(harvest)
    load2 = euroceanvessels_prov(load1)


