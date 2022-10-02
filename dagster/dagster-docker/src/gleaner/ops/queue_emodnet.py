from dagster import op
import subprocess

@op
def emodnet():
    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_queue.yaml  --source emodnet', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    r = str('returned value:{}'.format(returned_value))

    return r
