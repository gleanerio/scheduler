from dagster import op, graph
import subprocess

from gleaner.assets.oih_assets import asset_ee
from gleaner.ops.oih_checksite import check_sitemap


@op
def oih_asset_euroceanevent():
        return "euroceanevent"

@op
def euroceanevents(context, status: int):
    if status != 0:
        print("there is an error with the site map we should not run")
        raise Exception("Error detected in provided siteamp or sitegraph")
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_local.yaml  --source euroceanevents', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))
    return r

@op
def euroceanevents_rdf(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s summoned/euroceanevents', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@op
def euroceanevents_prov(context, msg: str):
    returned_value = subprocess.call('./nabuDocker.sh  --cfg /nabu/wd/oihlocal.yaml  prune -s prov/euroceanevents', shell=True, cwd='/home/fils/src/Projects/gleaner.io/nabu/secret/cliNaboDocker')
    r = str('returned value:{}'.format(returned_value))
    return msg + r

@graph
def harvest_euroceanevents():
    # x = check_sitemap()
    # if x == 0 :
        harvest = euroceanevents(check_sitemap(oih_asset_euroceanevent()))
        load1 = euroceanevents_rdf(harvest)
        load2 = euroceanevents_prov(load1)


