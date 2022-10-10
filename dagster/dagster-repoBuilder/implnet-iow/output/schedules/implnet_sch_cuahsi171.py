from dagster import schedule

from jobs.implnet_jobs_cuahsi171 import implnet_job_cuahsi171

@schedule(cron_schedule="0 9 * * 0", job=implnet_job_cuahsi171, execution_timezone="US/Central")
def implnet_sch_cuahsi171(_context):
    run_config = {}
    return run_config
