from dagster import schedule

from jobs.implnet_jobs_nmwdi22 import implnet_job_nmwdi22

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_nmwdi22, execution_timezone="US/Central")
def implnet_sch_nmwdi22(_context):
    run_config = {}
    return run_config
