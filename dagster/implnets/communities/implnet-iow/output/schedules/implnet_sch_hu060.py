from dagster import schedule

from jobs.implnet_jobs_hu060 import implnet_job_hu060

@schedule(cron_schedule="0 15 * * 1", job=implnet_job_hu060, execution_timezone="US/Central")
def implnet_sch_hu060(_context):
    run_config = {}
    return run_config
