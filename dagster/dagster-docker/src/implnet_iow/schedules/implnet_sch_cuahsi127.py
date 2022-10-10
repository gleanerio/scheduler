from dagster import schedule

from jobs.implnet_jobs_cuahsi127 import implnet_job_cuahsi127

@schedule(cron_schedule="0 11 * * 0", job=implnet_job_cuahsi127, execution_timezone="US/Central")
def implnet_sch_cuahsi127(_context):
    run_config = {}
    return run_config
