from dagster import schedule

from jobs.implnet_jobs_cuahsi112 import implnet_job_cuahsi112

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_cuahsi112, execution_timezone="US/Central")
def implnet_sch_cuahsi112(_context):
    run_config = {}
    return run_config
