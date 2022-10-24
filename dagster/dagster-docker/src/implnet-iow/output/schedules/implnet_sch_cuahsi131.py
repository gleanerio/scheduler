from dagster import schedule

from jobs.implnet_jobs_cuahsi131 import implnet_job_cuahsi131

@schedule(cron_schedule="0 15 * * 0", job=implnet_job_cuahsi131, execution_timezone="US/Central")
def implnet_sch_cuahsi131(_context):
    run_config = {}
    return run_config
