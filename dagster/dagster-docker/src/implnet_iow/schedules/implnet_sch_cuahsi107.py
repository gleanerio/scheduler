from dagster import schedule

from jobs.implnet_jobs_cuahsi107 import implnet_job_cuahsi107

@schedule(cron_schedule="0 14 * * 0", job=implnet_job_cuahsi107, execution_timezone="US/Central")
def implnet_sch_cuahsi107(_context):
    run_config = {}
    return run_config
