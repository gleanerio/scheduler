from dagster import schedule

from jobs.implnet_jobs_cuahsi144 import implnet_job_cuahsi144

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_cuahsi144, execution_timezone="US/Central")
def implnet_sch_cuahsi144(_context):
    run_config = {}
    return run_config
