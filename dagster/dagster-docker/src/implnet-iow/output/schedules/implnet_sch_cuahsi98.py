from dagster import schedule

from jobs.implnet_jobs_cuahsi98 import implnet_job_cuahsi98

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi98, execution_timezone="US/Central")
def implnet_sch_cuahsi98(_context):
    run_config = {}
    return run_config
