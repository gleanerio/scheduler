from dagster import op, graph
import subprocess
import sys, os

from gleaner.ops.oih_checksite import check_sitemap


@op
def euroceanexpert(context):
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source euroceanexpert', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def euroceanexpert_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/euroceanexpert', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def euroceanexpert_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/euroceanexpert', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_euroceanexpert():
    # if check_sitemap() != 0:
    #     # sys.exit(os.EX_SOFTWARE)
    #     # exit(1)
    #     print("bad")
    # else:
        harvest = euroceanexpert()
        load1 = euroceanexpert_rdf(harvest)
        load2 = euroceanexpert_prov(load1)


