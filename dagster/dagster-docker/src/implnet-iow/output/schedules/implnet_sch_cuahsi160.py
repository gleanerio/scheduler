from dagster import schedule

from jobs.implnet_jobs_cuahsi160 import implnet_job_cuahsi160

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi160, execution_timezone="US/Central")
def implnet_sch_cuahsi160(_context):
    run_config = {}
    return run_config
