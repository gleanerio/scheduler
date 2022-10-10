from dagster import schedule

from jobs.implnet_jobs_cuahsi135 import implnet_job_cuahsi135

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_cuahsi135, execution_timezone="US/Central")
def implnet_sch_cuahsi135(_context):
    run_config = {}
    return run_config
