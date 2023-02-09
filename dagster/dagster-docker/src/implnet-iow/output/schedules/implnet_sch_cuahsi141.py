from dagster import schedule

from jobs.implnet_jobs_cuahsi141 import implnet_job_cuahsi141

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_cuahsi141, execution_timezone="US/Central")
def implnet_sch_cuahsi141(_context):
    run_config = {}
    return run_config
