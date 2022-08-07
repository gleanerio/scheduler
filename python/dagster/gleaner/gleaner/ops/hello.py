from dagster import op
import subprocess

@op
def hello():
    """
    An op definition. This example op outputs a single string.

    For more hints about writing Dagster ops, see our documentation overview on Ops:
    https://docs.dagster.io/concepts/ops-jobs-graphs/ops
    """

    #cmd = "git --version"
    # cmd - ""

    returned_value = subprocess.call('./gleanerDocker.sh -cfg /gleaner/wd/rundir/oih_queue.yaml  --source cioosatlantic', shell=True, cwd='/home/fils/src/gomods/gleaner/secret/dockercli')
    # returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    r = str('returned value:{}'.format(returned_value))

    return r
