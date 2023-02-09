from dagster import schedule

from jobs.implnet_jobs_cuahsi155 import implnet_job_cuahsi155

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi155, execution_timezone="US/Central")
def implnet_sch_cuahsi155(_context):
    run_config = {}
    return run_config
