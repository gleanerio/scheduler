from dagster import schedule

from jobs.implnet_jobs_cuahsi114 import implnet_job_cuahsi114

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi114, execution_timezone="US/Central")
def implnet_sch_cuahsi114(_context):
    run_config = {}
    return run_config
