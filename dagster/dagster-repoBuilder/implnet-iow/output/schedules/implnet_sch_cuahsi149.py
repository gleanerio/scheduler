from dagster import schedule

from jobs.implnet_jobs_cuahsi149 import implnet_job_cuahsi149

@schedule(cron_schedule="0 10 * * 0", job=implnet_job_cuahsi149, execution_timezone="US/Central")
def implnet_sch_cuahsi149(_context):
    run_config = {}
    return run_config
