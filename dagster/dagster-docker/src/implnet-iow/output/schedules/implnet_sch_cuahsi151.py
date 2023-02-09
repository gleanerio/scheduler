from dagster import schedule

from jobs.implnet_jobs_cuahsi151 import implnet_job_cuahsi151

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi151, execution_timezone="US/Central")
def implnet_sch_cuahsi151(_context):
    run_config = {}
    return run_config
