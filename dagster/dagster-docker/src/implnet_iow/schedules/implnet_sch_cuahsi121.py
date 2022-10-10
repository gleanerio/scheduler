from dagster import schedule

from jobs.implnet_jobs_cuahsi121 import implnet_job_cuahsi121

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_cuahsi121, execution_timezone="US/Central")
def implnet_sch_cuahsi121(_context):
    run_config = {}
    return run_config
