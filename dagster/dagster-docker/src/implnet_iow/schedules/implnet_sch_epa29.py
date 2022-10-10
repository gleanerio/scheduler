from dagster import schedule

from jobs.implnet_jobs_epa29 import implnet_job_epa29

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_epa29, execution_timezone="US/Central")
def implnet_sch_epa29(_context):
    run_config = {}
    return run_config
