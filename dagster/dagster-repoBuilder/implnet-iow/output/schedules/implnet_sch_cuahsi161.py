from dagster import schedule

from jobs.implnet_jobs_cuahsi161 import implnet_job_cuahsi161

@schedule(cron_schedule="0 22 * * 0", job=implnet_job_cuahsi161, execution_timezone="US/Central")
def implnet_sch_cuahsi161(_context):
    run_config = {}
    return run_config
