from dagster import schedule

from jobs.implnet_jobs_cuahsi99 import implnet_job_cuahsi99

@schedule(cron_schedule="0 6 * * 0", job=implnet_job_cuahsi99, execution_timezone="US/Central")
def implnet_sch_cuahsi99(_context):
    run_config = {}
    return run_config
