from dagster import schedule

from jobs.implnet_jobs_cuahsi159 import implnet_job_cuahsi159

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi159, execution_timezone="US/Central")
def implnet_sch_cuahsi159(_context):
    run_config = {}
    return run_config
