from dagster import schedule

from jobs.implnet_jobs_dams1 import implnet_job_dams1

@schedule(cron_schedule="0 0 * * 3", job=implnet_job_dams1, execution_timezone="US/Central")
def implnet_sch_dams1(_context):
    run_config = {}
    return run_config
