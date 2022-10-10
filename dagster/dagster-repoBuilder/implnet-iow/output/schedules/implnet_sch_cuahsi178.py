from dagster import schedule

from jobs.implnet_jobs_cuahsi178 import implnet_job_cuahsi178

@schedule(cron_schedule="0 16 * * 0", job=implnet_job_cuahsi178, execution_timezone="US/Central")
def implnet_sch_cuahsi178(_context):
    run_config = {}
    return run_config
