from dagster import schedule

from jobs.implnet_jobs_cuahsi180 import implnet_job_cuahsi180

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi180, execution_timezone="US/Central")
def implnet_sch_cuahsi180(_context):
    run_config = {}
    return run_config
